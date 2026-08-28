#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, sys
ALLOWED_MODES={'static','unit','ui','runtime','exception'}
def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def applicable(rule,caps):
    cond=rule.get('appliesWhen','always')
    if cond=='always': return True
    if isinstance(cond,dict):
        if 'capability' in cond: return caps.get(cond['capability']) == cond.get('equals')
        if 'anyCapability' in cond: return any(bool(caps.get(k)) for k in cond['anyCapability'])
        if 'bottomNavigationMode' in cond: return caps.get('bottomNavigationMode','none') == cond['bottomNavigationMode']
    return False
def read_text(p):
    try: return p.read_text(encoding='utf-8')
    except UnicodeDecodeError: return ''
def parse_strings_keys(text): return set(re.findall(r'^\s*"((?:\\.|[^"\\])+)"\s*=',text,flags=re.M))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--app-root',required=True); ap.add_argument('--standard-root',required=True); args=ap.parse_args()
    app=Path(args.app_root).resolve(); std=Path(args.standard_root).resolve(); errors=[]; warnings=[]
    mp=app/'STANDARD_CONFORMANCE.json'
    if not mp.is_file(): print('FAIL STD-CONF-001 – missing STANDARD_CONFORMANCE.json'); return 1
    m=load(mp); cat=load(std/'CONFORMANCE_CATALOG.json')
    if m.get('standardVersion')!=cat.get('standardVersion'): errors.append('STD-CONF-001 standardVersion mismatch')
    sv=app/'STANDARD_VERSION'
    if sv.exists() and sv.read_text().strip()!=cat.get('standardVersion'): errors.append('STD-CONF-001 STANDARD_VERSION pin mismatch')
    caps=m.get('capabilities',{}); entries=m.get('rules',{}); exceptions=m.get('exceptions',{})
    ars=[r for r in cat.get('rules',[]) if r.get('level') in ('MUST','MUST NOT') and applicable(r,caps)]
    passed=exc=pending=0
    for r in ars:
        rid=r['id']; e=entries.get(rid)
        if not e: errors.append(f'{rid} missing conformance entry'); continue
        mode=e.get('mode'); status=e.get('status')
        if mode not in ALLOWED_MODES: errors.append(f'{rid} invalid mode {mode}'); continue
        if status not in {'implemented','pending','exception'}: errors.append(f'{rid} invalid status {status}'); continue
        if status=='exception' or mode=='exception':
            adr=exceptions.get(rid,{}).get('adr')
            if not adr or not (app/adr).is_file(): errors.append(f'{rid} exception missing existing ADR')
            else: exc+=1
            continue
        if status=='pending': warnings.append(f'{rid} pending'); pending += int(r.get('releaseBlocking',True)); continue
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
        elif mode in {'unit','ui'}:
            if not e.get('test'): errors.append(f'{rid} {mode} evidence missing test')
            else: passed+=1
        elif mode=='runtime':
            gate=e.get('runtimeGate')
            if not gate: errors.append(f'{rid} runtime evidence missing runtimeGate')
            else:
                f=gate.split('#',1)[0]
                if f and not (app/f).is_file(): errors.append(f'{rid} runtime gate file missing: {f}')
                else: passed+=1
    loc=m.get('localization',{}); lfiles=loc.get('files',[])
    if lfiles:
        ks=[]
        for rel in lfiles:
            p=app/rel
            if not p.is_file(): errors.append(f'STD-LOC-001 missing localization file {rel}')
            else: ks.append((rel,parse_strings_keys(read_text(p))))
        if ks:
            base=ks[0][1]
            for rel,s in ks[1:]:
                if s!=base: errors.append(f'STD-LOC-001 localization key mismatch: {rel}')
            for k in loc.get('requiredKeys',[]):
                for rel,s in ks:
                    if k not in s: errors.append(f'STD-LOC-001 required key {k} missing in {rel}')
    for p in app.rglob('*'):
        if p.name=='.DS_Store' or 'xcuserdata' in p.parts: errors.append(f'STD-RELEASE-001 hygiene violation: {p.relative_to(app)}')
    mode=caps.get('bottomNavigationMode','none')
    if caps.get('hasBottomNavigation') and mode not in {'native','custom'}: errors.append('STD-NAV-001 invalid bottomNavigationMode')
    if not caps.get('hasBottomNavigation') and mode!='none': errors.append('STD-NAV-001 bottomNavigationMode must be none')
    if errors:
        print('FAIL – IbaJuraj Standard 1.7.0 app conformance')
        [print(' -',x) for x in errors]; [print(' !',x) for x in warnings]
        print(f'applicable MUST: {len(ars)} / pass-like: {passed} / exceptions: {exc} / pending: {pending}'); return 1
    print('PASS – IbaJuraj Standard 1.7.0 app conformance declaration/evidence')
    [print(' !',x) for x in warnings]
    print(f'applicable MUST: {len(ars)} / evidence PASS: {passed} / exceptions: {exc} / release-blocking pending: {pending}')
    if pending: print('NOT RELEASE-READY – release-blocking gates pending'); return 2
    return 0
if __name__=='__main__': sys.exit(main())
