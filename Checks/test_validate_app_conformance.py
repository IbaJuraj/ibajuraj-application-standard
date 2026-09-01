import json, subprocess, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VALIDATOR=ROOT/'Checks/validate-app-conformance.py'
CAT=json.loads((ROOT/'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))


def condition_applies(cond, caps):
    if cond == 'always': return True
    if isinstance(cond, dict):
        if 'anyOf' in cond: return any(condition_applies(x,caps) for x in cond['anyOf'])
        if 'allOf' in cond: return all(condition_applies(x,caps) for x in cond['allOf'])
        if 'capability' in cond: return caps.get(cond['capability']) == cond.get('equals')
        if 'anyCapability' in cond: return any(bool(caps.get(k)) for k in cond['anyCapability'])
        if 'allCapabilities' in cond: return all(bool(caps.get(k)) for k in cond['allCapabilities'])
        if 'bottomNavigationMode' in cond: return caps.get('bottomNavigationMode','none') == cond['bottomNavigationMode']
    return False
def applies(rule, caps):
    return condition_applies(rule.get('appliesWhen','always'), caps)

SCREEN_REQ={
    'hasSettings':['SCREEN-SETTINGS','SCREEN-ABOUT'], 'hasSearch':['SCREEN-SEARCH'],
    'hasDetails':['SCREEN-DETAIL'], 'hasForms':['SCREEN-FORM'], 'hasSheets':['SCREEN-SHEET'],
    'hasFullscreen':['SCREEN-FULLSCREEN'], 'hasOnboarding':['SCREEN-ONBOARDING'],
    'hasStateSurfaces':['SCREEN-STATES'], 'hasBottomNavigation':['SCREEN-BOTTOM-NAV']
}

class ValidatorTests(unittest.TestCase):
    def make_app(self, caps=None, omit=None, pending=None, localization=False, omit_screen=None, pending_screen=None):
        td=tempfile.TemporaryDirectory(); r=Path(td.name)
        (r/'STANDARD_VERSION').write_text('1.7.0\n')
        (r/'evidence.txt').write_text('Bundle CFBundleShortVersionString CFBundleVersion IbaJuraj Apps ij.root.title ij.navigation.header ij.bottomnav.container')
        (r/'RUNTIME_ACCEPTANCE.md').write_text('# Runtime\n')
        base={'hasSettings':False,'hasAppearance':False,'hasCustomThemes':False,'hasLocalization':False,
              'hasBottomNavigation':False,'bottomNavigationMode':'none','hasBottomPrimaryAction':False,'hasFixedBottomControls':False,
              'supportsIPad':False,'requiresIPadCompatibilityTest':False,'supportsResizableWindow':False,
              'hasCalculatorKeypad':False,'hasForms':False,'hasAdvancedFormFields':False,'hasPersistedData':False,
              'hasSyncOrBackup':False,'hasAuthoritativeVersionedData':False,'hasAppLock':False,'hasGeneratedAssistance':False,
              'hasTranslucentSurfaces':False,'hasSearch':False,'hasDetails':False,'hasSheets':False,'hasFullscreen':False,
              'hasOnboarding':False,'hasStateSurfaces':False}
        if caps: base.update(caps)
        rules={}
        for x in CAT['rules']:
            if x['level'] not in ('MUST','MUST NOT') or not applies(x,base): continue
            rid=x['id']; mode=x.get('defaultVerification','static')
            if mode=='static': rules[rid]={'mode':'static','status':'implemented','evidence':{'files':['evidence.txt']}}
            elif mode=='unit': rules[rid]={'mode':'unit','status':'implemented','test':'UnitTests/'+rid}
            elif mode=='ui': rules[rid]={'mode':'ui','status':'implemented','test':'UITests/'+rid}
            else: rules[rid]={'mode':'runtime','status':'implemented','runtimeGate':'RUNTIME_ACCEPTANCE.md#'+rid}
        if omit: rules.pop(omit,None)
        if pending and pending in rules: rules[pending]={'mode':rules[pending]['mode'],'status':'pending'}
        req={'SCREEN-ROOT'}
        for cap,fams in SCREEN_REQ.items():
            if base.get(cap): req.update(fams)
        families={f:{'status':'pass','screens':[f+' Fixture'],'evidence':['RUNTIME_ACCEPTANCE.md#'+f]} for f in sorted(req)}
        if omit_screen: families.pop(omit_screen,None)
        if pending_screen in families: families[pending_screen]['status']='pending'
        manifest={'standardVersion':'1.7.0','app':{'name':'Fixture','productId':'fixture'},'capabilities':base,
                  'screenAudit':{'families':families},'rules':rules,'exceptions':{}}
        if localization:
            (r/'sk.lproj').mkdir(); (r/'en.lproj').mkdir()
            (r/'sk.lproj/Localizable.strings').write_text('"about" = "O aplikácii";\n"version" = "Verzia";\n')
            (r/'en.lproj/Localizable.strings').write_text('"about" = "About";\n"version" = "Version";\n')
            manifest['localization']={'files':['sk.lproj/Localizable.strings','en.lproj/Localizable.strings'],'requiredKeys':['about','version']}
        (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(manifest))
        return td,r

    def runv(self,r):
        return subprocess.run(['python3',str(VALIDATOR),'--app-root',str(r),'--standard-root',str(ROOT)],capture_output=True,text=True)

    def test_complete_fixture_passes(self):
        td,r=self.make_app()
        try: self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

    def test_missing_always_rule_fails(self):
        td,r=self.make_app(omit='STD-CONF-001')
        try: self.assertEqual(self.runv(r).returncode,1)
        finally: td.cleanup()

    def test_conditional_custom_nav_rule_is_enforced(self):
        td,r=self.make_app({'hasBottomNavigation':True,'bottomNavigationMode':'custom'},omit='STD-NAV-010')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-NAV-010 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_anyof_condition_for_fixed_bottom_controls_is_enforced(self):
        td,r=self.make_app({'hasFixedBottomControls':True},omit='STD-VIEWPORT-003')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-VIEWPORT-003 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_all_capabilities_condition_is_enforced(self):
        td,r=self.make_app({'hasBottomNavigation':True,'bottomNavigationMode':'native','hasForms':True},omit='STD-FORM-006')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-FORM-006 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_release_blocking_pending_returns_two(self):
        td,r=self.make_app(pending='STD-ADAPT-001')
        try: self.assertEqual(self.runv(r).returncode,2)
        finally: td.cleanup()

    def test_missing_required_screen_family_fails(self):
        td,r=self.make_app({'hasSettings':True},omit_screen='SCREEN-ABOUT')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-SCREEN-001 missing screen family SCREEN-ABOUT',p.stdout)
        finally: td.cleanup()

    def test_pending_screen_family_returns_two(self):
        td,r=self.make_app(pending_screen='SCREEN-ROOT')
        try: self.assertEqual(self.runv(r).returncode,2)
        finally: td.cleanup()

    def test_localization_parity_passes(self):
        td,r=self.make_app({'hasLocalization':True},localization=True)
        try: self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

if __name__=='__main__': unittest.main()
