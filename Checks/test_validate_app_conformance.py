import hashlib, json, subprocess, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VALIDATOR=ROOT/'Checks/validate-app-conformance.py'
CAT=json.loads((ROOT/'CONFORMANCE_CATALOG.json').read_text(encoding='utf-8'))
STANDARD_VERSION=CAT['standardVersion']
STANDARD_CANDIDATE=CAT.get('candidate')


def condition_applies(cond, caps, phase='release-candidate'):
    if cond == 'always': return True
    if isinstance(cond, dict):
        if 'anyOf' in cond: return any(condition_applies(x,caps,phase) for x in cond['anyOf'])
        if 'allOf' in cond: return all(condition_applies(x,caps,phase) for x in cond['allOf'])
        if 'phase' in cond: return phase == cond['phase']
        if 'capability' in cond: return caps.get(cond['capability']) == cond.get('equals')
        if 'anyCapability' in cond: return any(bool(caps.get(k)) for k in cond['anyCapability'])
        if 'allCapabilities' in cond: return all(bool(caps.get(k)) for k in cond['allCapabilities'])
        if 'bottomNavigationMode' in cond: return caps.get('bottomNavigationMode','none') == cond['bottomNavigationMode']
    return False

def applies(rule, caps, phase='release-candidate'):
    return condition_applies(rule.get('appliesWhen','always'), caps, phase)

SCREEN_REQ={
    'hasSettings':['SCREEN-SETTINGS','SCREEN-ABOUT'], 'hasSearch':['SCREEN-SEARCH'],
    'hasDetails':['SCREEN-DETAIL'], 'hasForms':['SCREEN-FORM'], 'hasSheets':['SCREEN-SHEET'],
    'hasFullscreen':['SCREEN-FULLSCREEN'], 'hasOnboarding':['SCREEN-ONBOARDING'],
    'hasStateSurfaces':['SCREEN-STATES'], 'hasBottomNavigation':['SCREEN-BOTTOM-NAV']
}

class ValidatorTests(unittest.TestCase):
    def make_app(self, caps=None, omit=None, pending=None, localization=False, omit_screen=None, pending_screen=None, phase='release-candidate'):
        td=tempfile.TemporaryDirectory(); r=Path(td.name)
        (r/'STANDARD_VERSION').write_text(STANDARD_VERSION+'\n')
        (r/'evidence.txt').write_text('Bundle CFBundleShortVersionString CFBundleVersion IbaJuraj Apps ij.root.title ij.navigation.header ij.bottomnav.container')
        (r/'RUNTIME_ACCEPTANCE.md').write_text('# Runtime\n')
        base={
            'hasSettings':False,'hasAppearance':False,'hasCustomThemes':False,'hasLocalization':False,'hasLocalizedSearch':False,
            'hasBottomNavigation':False,'bottomNavigationMode':'none','hasBottomPrimaryAction':False,'hasFixedBottomControls':False,
            'supportsIPad':False,'requiresIPadCompatibilityTest':False,'supportsResizableWindow':False,
            'hasCalculatorKeypad':False,'hasForms':False,'hasAdvancedFormFields':False,'hasPersistedData':False,
            'hasSyncOrBackup':False,'hasAuthoritativeVersionedData':False,'hasAuthoritativeFunctionalSources':False,
            'hasInAppLanguageSelector':False,
            'hasAppLock':False,'hasGeneratedAssistance':False,'hasAIReleaseReview':False,'hasOnDeviceAI':False,'hasCloudAI':False,
            'hasAITools':False,'hasAdaptiveAI':False,'hasAIPersonalization':False,'hasPostReleaseMonitoring':False,
            'hasTranslucentSurfaces':False,'hasSearch':False,'hasDetails':False,'hasSheets':False,'hasFullscreen':False,
            'hasOnboarding':False,'hasStateSurfaces':False,'hasProductionBackend':False,'hasRepresentativeUserData':False,
            'hasAsyncDerivedState':False,'hasDerivedState':False,'hasRemoteDestructiveOrAccessMutations':False,
            'hasCloudSharingOrAccessControl':False,'hasPersistentSharedContent':False,'hasRemoteInviteShareAccessFlow':False,
            'hasPortableBackup':False,'hasUserRestore':False,'hasAppUpdateNotice':False,
            'hasRelationshipBearingDeletion':False,'hasMaterialDeterministicEngine':False,
            'hasFeatureFlaggedPermissionedCapability':False,'hasCompactSurfaces':False
        }
        if caps: base.update(caps)
        ai_caps={'hasGeneratedAssistance','hasAIReleaseReview','hasOnDeviceAI','hasCloudAI','hasAITools','hasAdaptiveAI','hasAIPersonalization'}
        if any(bool(base.get(k)) for k in ai_caps) and not base.get('hasOnDeviceAI') and not base.get('hasCloudAI'):
            base['hasOnDeviceAI']=True
        rules={}
        for x in CAT['rules']:
            if x['level'] not in ('MUST','MUST NOT') or not applies(x,base,phase): continue
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
        ai_caps={'hasGeneratedAssistance','hasAIReleaseReview','hasOnDeviceAI','hasCloudAI','hasAITools','hasAdaptiveAI','hasAIPersonalization'}
        features=[]
        if any(bool(base.get(k)) for k in ai_caps):
            profile='adaptive' if base.get('hasAdaptiveAI') else ('action-capable' if base.get('hasAITools') else 'advisory')
            execution='hybrid' if base.get('hasOnDeviceAI') and base.get('hasCloudAI') else ('cloud' if base.get('hasCloudAI') else 'on-device')
            features=[{'id':'fixture.ai','riskProfile':profile,'execution':execution,'runtimeKind':'model','fallbackKind':'none','personalization':bool(base.get('hasAIPersonalization'))}]
        manifest={'standardVersion':STANDARD_VERSION,'standardCandidate':STANDARD_CANDIDATE,'app':{'name':'Fixture','productId':'fixture','version':'1.0.0','build':'42','sourceRevision':'a'*40},'capabilities':base,
                  'ai':{'features':features},'screenAudit':{'families':families},'rules':rules,'exceptions':{}}
        if localization:
            (r/'sk.lproj').mkdir(); (r/'en.lproj').mkdir()
            (r/'sk.lproj/Localizable.strings').write_text('"about" = "O aplikácii";\n"version" = "Verzia";\n')
            (r/'en.lproj/Localizable.strings').write_text('"about" = "About";\n"version" = "Version";\n')
            manifest['localization']={'files':['sk.lproj/Localizable.strings','en.lproj/Localizable.strings'],'requiredKeys':['about','version']}
        # Synthetic test-only execution record: not a product runtime PASS.
        (r/'Evidence').mkdir()
        artifact='Evidence/synthetic_execution.log'
        (r/artifact).write_text('Synthetic fixture evidence for validator regression, not Xcode or device runtime.\\n')
        digest=hashlib.sha256((r/artifact).read_bytes()).hexdigest()
        entries={}
        def result(mode,check):
            value={'status':'pass','mode':mode,'check':check,'executedAt':'2026-10-16T14:00:00+00:00',
                   'runner':'synthetic fixture runner','artifact':artifact,'artifactSha256':digest}
            if mode in ('ui','runtime'): value.update({'device':'Fixture iPhone','os':'Fixture iOS'})
            return value
        for rid,entry in rules.items():
            if entry.get('status')!='implemented': continue
            mode=entry['mode']
            if mode in ('unit','ui','runtime'):
                entries[rid]=result(mode,entry.get('runtimeGate') if mode=='runtime' else entry.get('test'))
        for fam,entry in families.items():
            if entry.get('status')=='pass': entries[fam]=result('ui',entry['evidence'][0])
        execution={'schemaVersion':1,'standardVersion':STANDARD_VERSION,'standardCandidate':STANDARD_CANDIDATE,
                   'phase':phase,'app':manifest['app'].copy(),'sourceRevision':'a'*40,'results':entries}
        (r/'Evidence/STANDARD_EXECUTION_RESULTS.json').write_text(json.dumps(execution))
        manifest['executionEvidence']={'file':'Evidence/STANDARD_EXECUTION_RESULTS.json'}
        (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(manifest))
        return td,r

    def runv(self,r,phase='release-candidate'):
        return subprocess.run(['python3',str(VALIDATOR),'--app-root',str(r),'--standard-root',str(ROOT),'--phase',phase],capture_output=True,text=True)

    def test_complete_fixture_passes(self):
        td,r=self.make_app()
        try: self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

    def test_missing_always_rule_fails(self):
        td,r=self.make_app(omit='STD-CONF-001')
        try: self.assertEqual(self.runv(r).returncode,1)
        finally: td.cleanup()

    def test_candidate_pin_semantics(self):
        td,r=self.make_app()
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            if STANDARD_CANDIDATE:
                m['standardCandidate']='WRONG-CANDIDATE'
                expected='standardCandidate mismatch'
            else:
                m['standardCandidate']='RC2'
                expected='stable standard must not pin a release candidate'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn(expected,p.stdout)
        finally: td.cleanup()

    def test_conditional_custom_nav_rule_is_enforced(self):
        td,r=self.make_app({'hasBottomNavigation':True,'bottomNavigationMode':'custom'},omit='STD-NAV-010')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-NAV-010 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_all_capabilities_condition_is_enforced(self):
        td,r=self.make_app({'hasBottomNavigation':True,'bottomNavigationMode':'native','hasForms':True},omit='STD-FORM-006')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-FORM-006 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_deterministic_rule_is_enforced(self):
        td,r=self.make_app({'hasMaterialDeterministicEngine':True},omit='STD-TEST-001')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-TEST-001 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_async_remote_invite_rule_is_enforced_when_present(self):
        if not any(x.get('id')=='STD-ASYNC-002' for x in CAT['rules']):
            self.skipTest('STD-ASYNC-002 is not present in this standard version')
        td,r=self.make_app({'hasRemoteInviteShareAccessFlow':True},omit='STD-ASYNC-002')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-ASYNC-002 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_authoritative_source_rule_is_enforced_when_present(self):
        if not any(x.get('id')=='STD-AUTH-SOURCE-001' for x in CAT['rules']):
            self.skipTest('STD-AUTH-SOURCE-001 is not present in this standard version')
        td,r=self.make_app({'hasAuthoritativeFunctionalSources':True},omit='STD-AUTH-SOURCE-001')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-AUTH-SOURCE-001 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_ai_release_review_rules_are_enforced_when_present(self):
        if not any(x.get('id')=='STD-AI-003' for x in CAT['rules']):
            self.skipTest('STD-AI-003 is not present in this standard version')
        td,r=self.make_app({'hasAIReleaseReview':True},omit='STD-AI-003')
        try:
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('STD-AI-003 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_ai_feature_metadata_is_required(self):
        td,r=self.make_app({'hasGeneratedAssistance':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']={'features':[]}
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('ai.features is empty or missing',p.stdout)
        finally: td.cleanup()

    def test_ai_runtime_kind_is_required_and_valid(self):
        td,r=self.make_app({'hasGeneratedAssistance':True,'hasOnDeviceAI':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']['features'][0].pop('runtimeKind',None)
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('invalid AI runtimeKind None',p.stdout)
        finally: td.cleanup()

    def test_ai_fallback_kind_is_required_and_valid(self):
        td,r=self.make_app({'hasGeneratedAssistance':True,'hasOnDeviceAI':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']['features'][0]['fallbackKind']='future-kind'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('invalid AI fallbackKind future-kind',p.stdout)
        finally: td.cleanup()

    def test_deterministic_ai_fallback_metadata_is_accepted(self):
        td,r=self.make_app({'hasGeneratedAssistance':True,'hasOnDeviceAI':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']['features'][0]['fallbackKind']='deterministic'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,0)
        finally: td.cleanup()

    def test_action_capable_ai_requires_tool_capability(self):
        td,r=self.make_app({'hasGeneratedAssistance':True,'hasOnDeviceAI':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']['features'][0]['riskProfile']='action-capable'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('requires hasAITools=true',p.stdout)
        finally: td.cleanup()

    def test_adaptive_ai_requires_adaptive_capability(self):
        td,r=self.make_app({'hasGeneratedAssistance':True,'hasOnDeviceAI':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text()); m['ai']['features'][0]['riskProfile']='adaptive'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r); self.assertEqual(p.returncode,1); self.assertIn('requires hasAdaptiveAI=true',p.stdout)
        finally: td.cleanup()
    def test_post_release_rule_is_enforced_when_capability_present(self):
        if not any(x.get('id')=='STD-POSTRELEASE-001' for x in CAT['rules']):
            self.skipTest('STD-POSTRELEASE-001 is not present in this standard version')
        td,r=self.make_app({'hasPostReleaseMonitoring':True},omit='STD-POSTRELEASE-001',phase='post-release')
        try:
            p=self.runv(r,'post-release'); self.assertEqual(p.returncode,1); self.assertIn('STD-POSTRELEASE-001 missing conformance entry',p.stdout)
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


    def test_rc4_rules_are_non_applicable_when_capabilities_are_disabled(self):
        td,r=self.make_app()
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            for rid in ('STD-BACKUP-001','STD-BACKUP-002','STD-SHARE-001','STD-UPDATE-001'):
                self.assertNotIn(rid,m['rules'])
            self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

    def test_rc4_capabilities_require_their_specific_rule(self):
        for flag,rid in (
            ('hasPortableBackup','STD-BACKUP-001'),
            ('hasUserRestore','STD-BACKUP-002'),
            ('hasPersistentSharedContent','STD-SHARE-001'),
            ('hasAppUpdateNotice','STD-UPDATE-001'),
        ):
            with self.subTest(capability=flag,rule=rid):
                td,r=self.make_app({**({ 'hasCloudSharingOrAccessControl':True } if flag=='hasPersistentSharedContent' else {}),flag:True},omit=rid)
                try:
                    p=self.runv(r)
                    self.assertEqual(p.returncode,1,p.stdout)
                    self.assertIn(rid+' missing conformance entry',p.stdout)
                finally: td.cleanup()

    def test_rc4_restore_is_independent_of_export(self):
        td,r=self.make_app({'hasUserRestore':True,'hasPortableBackup':False})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            self.assertIn('STD-BACKUP-002',m['rules'])
            self.assertNotIn('STD-BACKUP-001',m['rules'])
            self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

    def test_rc4_new_capability_flags_reject_non_boolean_values(self):
        for flag in ('hasPortableBackup','hasUserRestore','hasAppUpdateNotice'):
            with self.subTest(capability=flag):
                td,r=self.make_app()
                try:
                    m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
                    m['capabilities'][flag]='false'
                    (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
                    p=self.runv(r)
                    self.assertEqual(p.returncode,1,p.stdout)
                    self.assertIn(flag+' must be a boolean',p.stdout)
                finally: td.cleanup()


    def test_release_only_rules_are_not_in_development_phase(self):
        td,r=self.make_app(phase='development')
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            for rid in ('STD-RELEASE-006','STD-DIAG-001','STD-DIAG-002','STD-RELEASE-007',
                        'STD-TEST-002','STD-UI-001','STD-EVIDENCE-002'):
                self.assertNotIn(rid,m['rules'])
            p=self.runv(r,'development')
            self.assertEqual(p.returncode,0,p.stdout)
        finally: td.cleanup()

    def test_rc_phase_missing_release_rule_fails(self):
        td,r=self.make_app(omit='STD-DIAG-001')
        try:
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('STD-DIAG-001 missing conformance entry',p.stdout)
        finally: td.cleanup()

    def test_phase_mismatch_rejects_replayed_execution_report(self):
        td,r=self.make_app(phase='development')
        try:
            p=self.runv(r,'release-candidate')
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('execution evidence phase mismatch',p.stdout)
        finally: td.cleanup()

    def test_shared_access_without_shared_content_does_not_force_content_parity(self):
        td,r=self.make_app({'hasCloudSharingOrAccessControl':True,'hasPersistentSharedContent':False})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            self.assertIn('STD-CLOUD-002',m['rules'])
            self.assertNotIn('STD-SHARE-001',m['rules'])
            self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

    def test_shared_content_requires_access_control_capability(self):
        td,r=self.make_app({'hasPersistentSharedContent':True,'hasCloudSharingOrAccessControl':False})
        try:
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('hasPersistentSharedContent requires hasCloudSharingOrAccessControl=true',p.stdout)
        finally: td.cleanup()

    def test_language_selector_rule_is_conditional(self):
        rule=next(x for x in CAT['rules'] if x['id']=='STD-LOC-005')
        self.assertFalse(applies(rule,{'hasLocalization':True,'hasInAppLanguageSelector':False}))
        self.assertTrue(applies(rule,{'hasLocalization':True,'hasInAppLanguageSelector':True}))

    def test_missing_execution_report_is_not_a_pass(self):
        td,r=self.make_app()
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            m.pop('executionEvidence')
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r)
            self.assertEqual(p.returncode,2,p.stdout)
            self.assertIn('PENDING – execution evidence absent',p.stdout)
        finally: td.cleanup()

    def test_declared_test_reference_without_result_is_not_pass(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            del evidence['results']['STD-COMPONENT-001']
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,2,p.stdout)
            self.assertIn('STD-COMPONENT-001 PENDING – no executed result',p.stdout)
        finally: td.cleanup()

    def test_fail_result_is_not_pass(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            evidence['results']['STD-COMPONENT-001']['status']='fail'
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('execution status is not PASS',p.stdout)
        finally: td.cleanup()

    def test_mismatched_build_is_rejected(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            evidence['app']['build']='43'
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('execution evidence app.build mismatch',p.stdout)
        finally: td.cleanup()

    def test_mismatched_source_revision_is_rejected(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            evidence['sourceRevision']='b'*40
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('sourceRevision mismatch',p.stdout)
        finally: td.cleanup()

    def test_execution_artifact_tampering_is_rejected(self):
        td,r=self.make_app()
        try:
            (r/'Evidence/synthetic_execution.log').write_text('mutated artifact after PASS report')
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('execution artifact SHA256 mismatch',p.stdout)
        finally: td.cleanup()

    def test_runtime_device_context_is_required(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            evidence['results']['STD-COMPONENT-001'].pop('device',None)
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('missing device',p.stdout)
        finally: td.cleanup()

    def test_screen_pass_requires_execution_proof(self):
        td,r=self.make_app()
        try:
            file=r/'Evidence/STANDARD_EXECUTION_RESULTS.json'
            evidence=json.loads(file.read_text())
            evidence['results'].pop('SCREEN-ROOT')
            file.write_text(json.dumps(evidence))
            p=self.runv(r)
            self.assertEqual(p.returncode,2,p.stdout)
            self.assertIn('SCREEN-ROOT PENDING – no executed result',p.stdout)
        finally: td.cleanup()

    def test_execution_file_must_stay_inside_app_root(self):
        td,r=self.make_app()
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            m['executionEvidence']['file']='../../secrets.json'
            (r/'STANDARD_CONFORMANCE.json').write_text(json.dumps(m))
            p=self.runv(r)
            self.assertEqual(p.returncode,1,p.stdout)
            self.assertIn('file missing or unsafe path',p.stdout)
        finally: td.cleanup()

    def test_post_release_must_is_not_a_pre_release_blocker(self):
        td,r=self.make_app({'hasPostReleaseMonitoring':True})
        try:
            m=json.loads((r/'STANDARD_CONFORMANCE.json').read_text())
            self.assertNotIn('STD-POSTRELEASE-001',m['rules'])
            self.assertEqual(self.runv(r).returncode,0)
        finally: td.cleanup()

if __name__=='__main__': unittest.main()
