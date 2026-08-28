import json, subprocess, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VALIDATOR=ROOT/'Checks/validate-app-conformance.py'
CAT=json.loads((ROOT/'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))


def applies(rule, caps):
    cond=rule['appliesWhen']
    if cond == 'always':
        return True
    if 'capability' in cond:
        return caps.get(cond['capability']) == cond.get('equals')
    if 'anyCapability' in cond:
        return any(bool(caps.get(k)) for k in cond['anyCapability'])
    if 'bottomNavigationMode' in cond:
        return caps.get('bottomNavigationMode','none') == cond['bottomNavigationMode']
    return False

class ValidatorTests(unittest.TestCase):
    def make_app(self, caps=None, omit=None, pending=None, localization=False):
        td=tempfile.TemporaryDirectory(); r=Path(td.name)
        (r/'STANDARD_VERSION').write_text('1.7.0\n')
        (r/'evidence.txt').write_text('Bundle CFBundleShortVersionString CFBundleVersion IbaJuraj Apps ij.bottomnav.container')
        (r/'RUNTIME_ACCEPTANCE.md').write_text('# Runtime\n')
        base={'hasSettings':False,'hasAppearance':False,'hasCustomThemes':False,'hasLocalization':False,
              'hasBottomNavigation':False,'bottomNavigationMode':'none','hasBottomPrimaryAction':False,
              'supportsIPad':False,'requiresIPadCompatibilityTest':False,'supportsResizableWindow':False,
              'hasCalculatorKeypad':False,'hasForms':False,'hasAdvancedFormFields':False,'hasPersistedData':False,
              'hasSyncOrBackup':False,'hasAuthoritativeVersionedData':False,'hasAppLock':False,'hasGeneratedAssistance':False}
        if caps: base.update(caps)
        rules={}
        for x in CAT['rules']:
            if x['level'] not in ('MUST','MUST NOT') or not applies(x,base): continue
            rid=x['id']; mode=x['defaultVerification']
            if mode=='static': rules[rid]={'mode':'static','status':'implemented','evidence':{'files':['evidence.txt']}}
            elif mode=='unit': rules[rid]={'mode':'unit','status':'implemented','test':'UnitTests/'+rid}
            elif mode=='ui': rules[rid]={'mode':'ui','status':'implemented','test':'UITests/'+rid}
            else: rules[rid]={'mode':'runtime','status':'implemented','runtimeGate':'RUNTIME_ACCEPTANCE.md#'+rid}
        if omit: rules.pop(omit,None)
        if pending and pending in rules: rules[pending]={'mode':rules[pending]['mode'],'status':'pending'}
        manifest={'standardVersion':'1.7.0','app':{'name':'Fixture','productId':'fixture'},'capabilities':base,'rules':rules,'exceptions':{}}
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
        td,r=self.make_app({'hasBottomNavigation':True,'bottomNavigationMode':'custom'},omit='STD-NAV-003')
        try:
            p=self.runv(r)
            self.assertEqual(p.returncode,1)
            self.assertIn('STD-NAV-003 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_release_blocking_pending_returns_two(self):
        td,r=self.make_app(pending='STD-ADAPT-001')
        try: self.assertEqual(self.runv(r).returncode,2)
        finally: td.cleanup()

    def test_localization_parity_passes(self):
        td,r=self.make_app({'hasLocalization':True},localization=True)
        try: self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

if __name__=='__main__': unittest.main()
