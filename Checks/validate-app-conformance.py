#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, sys
from evidence_contract import load_execution_report, check_execution_result
ALLOWED_MODES={'static','unit','ui','runtime','exception'}
AI_PROFILES={'advisory','derived','action-capable','adaptive'}
AI_EXECUTION={'on-device','cloud','hybrid'}
AI_RUNTIME_KIND={'model','deterministic'}
AI_FALLBACK_KIND={'none','model','deterministic'}
AI_CAPS={'hasGeneratedAssistance','hasAIReleaseReview','hasOnDeviceAI','hasCloudAI','hasAITools','hasAdaptiveAI','hasAIPersonalization'}
# Missing risk-capability declarations may not silently mean N/A at release.
RC_REVIEW_CAPABILITIES={
    'hasPersistedData','hasSyncOrBackup','hasAppLock','hasProductionBackend',
    'hasCloudSharingOrAccessControl','hasPersistentSharedContent','hasRemoteInviteShareAccessFlow',
    'hasPortableBackup','hasUserRestore','hasAppUpdateNotice',
    'hasGeneratedAssistance','hasAIReleaseReview','hasOnDeviceAI','hasCloudAI',
    'hasAITools','hasAdaptiveAI','hasAIPersonalization',
    'hasAuthoritativeFunctionalSources','hasPostReleaseMonitoring'
}
SCREEN_REQUIREMENTS={
    'hasSettings':['SCREEN-SETTINGS','SCREEN-ABOUT'],
    'hasSearch':['SCREEN-SEARCH'], 'hasDetails':['SCREEN-DETAIL'], 'hasForms':['SCREEN-FORM'],
    'hasSheets':['SCREEN-SHEET'], 'hasFullscreen':['SCREEN-FULLSCREEN'], 'hasOnboarding':['SCREEN-ONBOARDING'],
    'hasStateSurfaces':['SCREEN-STATES'], 'hasBottomNavigation':['SCREEN-BOTTOM-NAV'],
}
def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def condition_applies(cond,caps,phase):
    if cond=='always': return True
    if isinstance(cond,dict):
        if 'anyOf' in cond: return any(condition_applies(x,caps,phase) for x in cond['anyOf'])
        if 'allOf' in cond: return all(condition_applies(x,caps,phase) for x in cond['allOf'])
        if 'phase' in cond: return phase == cond['phase']
        if 'capability' in cond: return caps.get(cond['capability']) == cond.get('equals')
        if 'anyCapability' in cond: return any(bool(caps.get(k)) for k in cond['anyCapability'])
        if 'allCapabilities' in cond: return all(bool(caps.get(k)) for k in cond['allCapabilities'])
        if 'bottomNavigationMode' in cond: return caps.get('bottomNavigationMode','none') == cond['bottomNavigationMode']
    return False
def applicable(rule,caps,phase): return condition_applies(rule.get('appliesWhen','always'),caps,phase)
def read_text(p):
    try: return p.read_text(encoding='utf-8')
    except UnicodeDecodeError: return ''
def parse_strings_keys(text): return set(re.findall(r'^\s*"((?:\\.|[^"\\])+)"\s*=',text,flags=re.M))
def screen_requirements(caps):
    req={'SCREEN-ROOT'}
    for cap,fams in SCREEN_REQUIREMENTS.items():
        if caps.get(cap): req.update(fams)
    return sorted(req)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--app-root',required=True); ap.add_argument('--standard-root',required=True); ap.add_argument('--phase',choices=['development','release-candidate','post-release'],default='release-candidate'); args=ap.parse_args()
    app=Path(args.app_root).resolve(); std=Path(args.standard_root).resolve(); errors=[]; warnings=[]
    mp=app/'STANDARD_CONFORMANCE.json'
    if not mp.is_file(): print('FAIL STD-CONF-001 – missing STANDARD_CONFORMANCE.json'); return 1
    m=load(mp); cat=load(std/'CONFORMANCE_CATALOG.json')
    if m.get('standardVersion')!=cat.get('standardVersion'): errors.append('STD-CONF-001 standardVersion mismatch')
    if cat.get('candidate'):
        if m.get('standardCandidate')!=cat.get('candidate'): errors.append('STD-CONF-001 standardCandidate mismatch')
    elif m.get('standardCandidate') not in (None,''):
        errors.append('STD-CONF-001 stable standard must not pin a release candidate')
    sv=app/'STANDARD_VERSION'
    if sv.exists() and sv.read_text().strip()!=cat.get('standardVersion'): errors.append('STD-CONF-001 STANDARD_VERSION pin mismatch')
    caps=m.get('capabilities',{}); entries=m.get('rules',{}); exceptions=m.get('exceptions',{})
    # All declared feature switches must be bools: string "false" is truthy.
    known = set(json.loads((std/'STANDARD_CONFORMANCE_TEMPLATE.json').read_text(encoding='utf-8'))['capabilities'])
    for flag, value in caps.items():
        if flag not in known: warnings.append(f'STD-CONF-001 unknown capability {flag}')
        elif flag == 'bottomNavigationMode':
            if value not in ('native', 'custom', 'none'):
                errors.append('STD-NAV-001 invalid bottomNavigationMode')
        elif type(value) is not bool:
            errors.append(f'STD-CONF-001 {flag} must be a boolean')
    for flag in sorted(RC_REVIEW_CAPABILITIES-set(caps)):
        message=f'STD-CONF-003 {flag} missing: declare true/false after source capability review (no implicit N/A)'
        if args.phase=='release-candidate': errors.append(message)
        else: warnings.append(message)
    if caps.get('hasCloudSharingOrAccessControl') and caps.get('hasPersistentSharedContent') is False:
        warnings.append('STD-SHARE-001 REVIEW – confirm access-only flow has no persistent recipient-shared records')
    if caps.get('hasPersistentSharedContent') and not caps.get('hasCloudSharingOrAccessControl'):
        errors.append('STD-SHARE-001 hasPersistentSharedContent requires hasCloudSharingOrAccessControl=true')
    execution_report = load_execution_report(app,m,cat,args.phase,errors)
    ai=m.get('ai',{}); features=ai.get('features',[]) if isinstance(ai,dict) else []
    ai_declared=any(bool(caps.get(k)) for k in AI_CAPS)
    if ai_declared and not features: errors.append('STD-AI-002 AI capability declared but ai.features is empty or missing')
    if features and not ai_declared: errors.append('STD-AI-002 ai.features declared without an AI capability flag')
    ids=set()
    for item in features:
        if not isinstance(item,dict): errors.append('STD-AI-002 ai.features item must be an object'); continue
        fid=item.get('id'); profile=item.get('riskProfile'); execution=item.get('execution')
        runtime_kind=item.get('runtimeKind'); fallback_kind=item.get('fallbackKind')
        if not isinstance(fid,str) or not fid.strip(): errors.append('STD-AI-002 AI feature missing stable id')
        elif fid in ids: errors.append(f'STD-AI-002 duplicate AI feature id {fid}')
        else: ids.add(fid)
        if profile not in AI_PROFILES: errors.append(f'STD-AI-002 {fid or "<unknown>"} invalid AI riskProfile {profile}')
        if execution not in AI_EXECUTION: errors.append(f'STD-AI-005 {fid or "<unknown>"} invalid AI execution {execution}')
        if runtime_kind not in AI_RUNTIME_KIND: errors.append(f'STD-AI-005 {fid or "<unknown>"} invalid AI runtimeKind {runtime_kind}')
        if fallback_kind not in AI_FALLBACK_KIND: errors.append(f'STD-AI-005 {fid or "<unknown>"} invalid AI fallbackKind {fallback_kind}')
    if any(isinstance(x,dict) and x.get('execution') in {'on-device','hybrid'} for x in features) and not caps.get('hasOnDeviceAI'): errors.append('STD-AI-005 on-device/hybrid AI feature requires hasOnDeviceAI=true')
    if any(isinstance(x,dict) and x.get('execution') in {'cloud','hybrid'} for x in features) and not caps.get('hasCloudAI'): errors.append('STD-AI-005 cloud/hybrid AI feature requires hasCloudAI=true')
    if any(isinstance(x,dict) and x.get('riskProfile')=='action-capable' for x in features) and not caps.get('hasAITools'): errors.append('STD-AI-003 action-capable AI feature requires hasAITools=true')
    if any(isinstance(x,dict) and x.get('riskProfile')=='adaptive' for x in features) and not caps.get('hasAdaptiveAI'): errors.append('STD-AI-007 adaptive AI feature requires hasAdaptiveAI=true')
    if any(isinstance(x,dict) and x.get('personalization') is True for x in features) and not caps.get('hasAIPersonalization'): errors.append('STD-AI-007 personalized AI feature requires hasAIPersonalization=true')
    ars=[r for r in cat.get('rules',[]) if r.get('level') in ('MUST','MUST NOT') and applicable(r,caps,args.phase)]
    recommendations=m.get('recommendations',{})
    if not isinstance(recommendations,dict):
        errors.append('STD-CONF-003 recommendations must be an object')
        recommendations={}
    for advice in cat.get('rules',[]):
        if advice.get('level')!='SHOULD' or not applicable(advice,caps,args.phase): continue
        rid=advice['id']; decision=recommendations.get(rid)
        if not isinstance(decision,dict) or decision.get('decision') not in {'adopted','deferred'}:
            warnings.append(f'{rid} SHOULD decision missing/invalid (adopted or deferred; never release-blocking)')
        elif decision.get('decision')=='deferred' and not str(decision.get('reason') or '').strip():
            warnings.append(f'{rid} SHOULD deferred without rationale (non-blocking)')
    passed=exc=pending=0
    for r in ars:
        rid=r['id']; e=entries.get(rid)
        if not e:
            if args.phase=='development':
                warnings.append(f'{rid} development declaration missing – PENDING, not release PASS')
                pending+=1
            else: errors.append(f'{rid} missing conformance entry')
            continue
        mode=e.get('mode'); status=e.get('status')
        if mode not in ALLOWED_MODES: errors.append(f'{rid} invalid mode {mode}'); continue
        if status not in {'implemented','pending','exception'}: errors.append(f'{rid} invalid status {status}'); continue
        if status=='exception' or mode=='exception':
            adr=exceptions.get(rid,{}).get('adr')
            if not adr or not (app/adr).is_file(): errors.append(f'{rid} exception missing existing ADR')
            else: exc+=1
            continue
        if status=='pending': warnings.append(f'{rid} pending'); pending += int(r.get('releaseBlocking',True) or args.phase=='post-release'); continue
        if mode=='static':
            ev=e.get('evidence',{}); files=ev.get('files',[])
            if not files: errors.append(f'{rid} static evidence has no files'); continue
            ok=True; joined=''
            for rel in files:
                p=app/rel
                if not p.is_file(): errors.append(f'{rid} missing evidence file {rel}'); ok=False
                else: joined+='\n'+read_text(p)
            for t in ev.get('containsAll',[]):
                if t not in joined: errors.append(f'{rid} missing token: {t}'); ok=False
            if ev.get('containsAny') and not any(t in joined for t in ev['containsAny']): errors.append(f'{rid} none of containsAny found'); ok=False
            for t in ev.get('notContains',[]):
                if t in joined: errors.append(f'{rid} forbidden token found: {t}'); ok=False
            if ok: passed+=1
        elif mode in {'unit','ui','runtime'}:
            check = e.get('runtimeGate') if mode == 'runtime' else e.get('test')
            if not isinstance(check, str) or not check.strip():
                errors.append(f'{rid} {mode} evidence missing test/runtimeGate')
                continue
            if mode == 'runtime':
                f = check.split('#',1)[0]
                if f and not (app/f).is_file():
                    errors.append(f'{rid} runtime gate file missing: {f}')
                    continue
            verified = check_execution_result(app,execution_report,rid,mode,check,errors,warnings)
            if verified: passed += 1
            else: pending += int(r.get('releaseBlocking',True) or args.phase=='post-release')
    screen_pending=0
    if args.phase=='release-candidate':
        screen=m.get('screenAudit',{}).get('families',{})
        required=screen_requirements(caps); screen_pending=0
        for fam in required:
            entry=screen.get(fam)
            if not isinstance(entry,dict): errors.append(f'STD-SCREEN-001 missing screen family {fam}'); continue
            screens=entry.get('screens',[])
            if not isinstance(screens,list) or not [x for x in screens if isinstance(x,str) and x.strip()]: errors.append(f'STD-SCREEN-001 {fam} has no concrete screens')
            state=entry.get('status')
            if state not in {'pass','pending','exception'}: errors.append(f'STD-SCREEN-002 {fam} invalid status {state}'); continue
            if state=='pending': warnings.append(f'STD-SCREEN-002 {fam} pending'); screen_pending+=1
            elif state=='exception':
                adr=entry.get('adr')
                if not adr or not (app/adr).is_file(): errors.append(f'STD-SCREEN-002 {fam} exception missing existing ADR')
            elif state=='pass':
                ev=entry.get('evidence',[])
                if not ev:
                    errors.append(f'STD-SCREEN-003 {fam} pass has no evidence')
                    continue
                for item in ev:
                    f=item.split('#',1)[0]
                    if f and not (app/f).is_file(): errors.append(f'STD-SCREEN-003 {fam} evidence file missing: {f}')
                if not check_execution_result(app,execution_report,fam,'ui',ev[0],errors,warnings):
                    screen_pending += 1
    elif args.phase=='development':
        screen=m.get('screenAudit',{}).get('families',{})
        for fam in screen_requirements(caps):
            if not isinstance(screen.get(fam),dict) or screen[fam].get('status')!='pass':
                screen_pending+=1
                warnings.append(f'STD-SCREEN-002 {fam} deferred until release-candidate acceptance')
    loc=m.get('localization',{}); lfiles=loc.get('files',[])
    if lfiles:
        ks=[]
        for rel in lfiles:
            p=app/rel
            if not p.is_file(): errors.append(f'STD-LOC-001 missing localization file {rel}')
            else: ks.append((rel,parse_strings_keys(read_text(p))))
        if ks:
            base=ks[0][1]
            for rel,keys in ks[1:]:
                if keys!=base: errors.append(f'STD-LOC-001 localization key mismatch: {rel}')
            for k in loc.get('requiredKeys',[]):
                for rel,keys in ks:
                    if k not in keys: errors.append(f'STD-LOC-001 required key {k} missing in {rel}')
    if args.phase=='release-candidate':
        for path in app.rglob('*'):
            if path.name=='.DS_Store' or 'xcuserdata' in path.parts or '__pycache__' in path.parts or path.suffix=='.pyc':
                errors.append(f'STD-RELEASE-005 release-root hygiene violation: {path.relative_to(app)}')
    mode=caps.get('bottomNavigationMode','none')
    if caps.get('hasBottomNavigation') and mode not in {'native','custom'}: errors.append('STD-NAV-001 invalid bottomNavigationMode')
    if not caps.get('hasBottomNavigation') and mode!='none': errors.append('STD-NAV-001 bottomNavigationMode must be none')
    label=f"IbaJuraj Standard {cat.get('standardVersion')} {cat.get('candidate') or ''}".strip()
    if errors:
        print(f'FAIL – {label} phase={args.phase} app conformance'); [print(' -',x) for x in errors]; [print(' !',x) for x in warnings]
        print(f'applicable MUST: {len(ars)} / pass-like: {passed} / exceptions: {exc} / rule pending: {pending} / screen pending: {screen_pending}'); return 1
    if pending or screen_pending:
        print(f'PENDING – {label} phase={args.phase} app conformance (not a PASS)')
        [print(' !',x) for x in warnings]
        print(f'applicable MUST: {len(ars)} / evidence PASS: {passed} / exceptions: {exc} / rule pending: {pending} / screen pending: {screen_pending}')
        if args.phase=='development':
            print('DEVELOPMENT REPORT ONLY – unresolved evidence is non-blocking; release approval is NOT implied')
            return 0
        print('NOT RELEASE-READY – required evidence pending')
        return 2
    print(f'PASS – {label} phase={args.phase} app conformance declaration/evidence')
    [print(' !',x) for x in warnings]
    print(f'applicable MUST: {len(ars)} / evidence PASS: {passed} / exceptions: {exc} / release-blocking rule pending: {pending} / screen pending: {screen_pending}')
    return 0
if __name__=='__main__': sys.exit(main())
