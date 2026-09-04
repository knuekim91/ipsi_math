# -*- coding: utf-8 -*-
"""
ipsi_math - 웹앱 생성기

units/*/problems/*.md 를 읽어 하나의 HTML 학습 앱(dist/webapp.html)을 만든다.
이 파일을 Artifact로 게시하면 나은이가 폰/태블릿에서 열어 쓸 수 있다.

문항이 추가될 때마다 다시 실행하고, 같은 파일 경로로 재게시하면 URL이 유지된다.

  python build/make_webapp.py
"""
import datetime as dt
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist", "webapp.html")

UNIT_LABEL = {
    "01-지수로그": "지수·로그", "02-삼각함수": "삼각함수", "03-수열": "수열",
    "04-극한연속": "극한·연속", "05-미분": "미분", "06-적분": "적분",
    "07-경우의수확률": "경우의 수·확률", "08-통계": "통계",
}


def parse(path):
    raw = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    meta, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            for line in raw[4:end].split("\n"):
                if ":" in line and not line.lstrip().startswith("#"):
                    k, v = line.split(":", 1)
                    v = v.strip().strip('"').strip("'")
                    meta[k.strip()] = v
            body = raw[end + 5:]
    sec, cur = {}, None
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip(); sec[cur] = []
        elif cur:
            sec[cur].append(line)
    for k in sec:
        sec[k] = "\n".join(sec[k]).strip()
    return meta, sec


def collect():
    out = []
    for unit in sorted(os.listdir(os.path.join(ROOT, "units"))):
        pdir = os.path.join(ROOT, "units", unit, "problems")
        if not os.path.isdir(pdir):
            continue
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            meta, sec = parse(os.path.join(pdir, fn))
            out.append({
                "id": meta.get("id", fn[:-3]),
                "unit": unit,
                "unitLabel": UNIT_LABEL.get(unit, unit),
                "topic": meta.get("topic", ""),
                "level": meta.get("level", ""),
                "diff": meta.get("difficulty", ""),
                "source": meta.get("source", ""),
                "core": meta.get("core", ""),
                "answer": meta.get("answer", ""),
                "q": sec.get("문제", ""),
                "idea": sec.get("발상", ""),
                "sol": sec.get("풀이", ""),
                "alt": sec.get("다른 풀이", ""),
                "trap": sec.get("함정", ""),
                "know": sec.get("노하우", ""),
            })
    return out


TEMPLATE = r"""<title>수능 수학 발상 트레이너</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Sans+KR:wght@300;400;500;600&display=swap">
<style>
:root{
  --paper:#EEF0F5; --card:#FFF; --ink:#151F38; --ink2:#4E5972; --ink3:#7A849A;
  --rule:#D2D8E4; --rule2:#E6EAF1; --indigo:#2E3F73;
  --mark:rgba(240,222,64,.55); --markline:#C9B32A;
  --ok:#2A6A58; --okbg:rgba(42,106,88,.10);
  --warn:#9A6B12; --warnbg:rgba(154,107,18,.11);
  --stop:#A33A29; --stopbg:rgba(163,58,41,.10);
  --shadow:0 1px 2px rgba(21,31,56,.06);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0E121B; --card:#161C29; --ink:#E8EBF2; --ink2:#9BA5BA; --ink3:#7A849A;
  --rule:#2A3242; --rule2:#222937; --indigo:#A6B8EC;
  --mark:rgba(231,211,74,.22); --markline:#8E7F22;
  --ok:#7CC7AE; --okbg:rgba(124,199,174,.12);
  --warn:#DFB765; --warnbg:rgba(223,183,101,.12);
  --stop:#E39683; --stopbg:rgba(227,150,131,.12);
  --shadow:none;
}}
:root[data-theme="dark"]{
  --paper:#0E121B; --card:#161C29; --ink:#E8EBF2; --ink2:#9BA5BA; --ink3:#7A849A;
  --rule:#2A3242; --rule2:#222937; --indigo:#A6B8EC;
  --mark:rgba(231,211,74,.22); --markline:#8E7F22;
  --ok:#7CC7AE; --okbg:rgba(124,199,174,.12);
  --warn:#DFB765; --warnbg:rgba(223,183,101,.12);
  --stop:#E39683; --stopbg:rgba(227,150,131,.12);
  --shadow:none;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:'IBM Plex Sans KR',system-ui,'Malgun Gothic',sans-serif;
  font-size:15px;line-height:1.7;-webkit-font-smoothing:antialiased;
  padding-bottom:104px}
.wrap{max-width:720px;margin:0 auto;padding:0 16px}
/* 터치 기기: 탭 시 회색 깜빡임·글자 선택·더블탭 확대 방지 */
button,textarea{-webkit-tap-highlight-color:transparent;touch-action:manipulation}
button{-webkit-user-select:none;user-select:none}
/* 태블릿에서는 본문을 한 단계 키운다 */
@media (min-width:768px){
  body{font-size:16px}
  .wrap{max-width:768px;padding:0 24px}
}
h1,h2,h3{font-family:'Gowun Batang',Georgia,serif;font-weight:700;margin:0;text-wrap:balance}
.m,.stem i{font-family:Georgia,'Times New Roman','Gowun Batang',serif}
.eyebrow{font-size:10.5px;font-weight:600;letter-spacing:.16em;color:var(--ink3)}

/* ---- 헤더 ---- */
header{padding:26px 0 18px;border-bottom:1px solid var(--rule)}
header h1{font-size:26px;letter-spacing:-.01em}
.dday{display:flex;align-items:baseline;gap:10px;margin-top:12px;flex-wrap:wrap}
.ddnum{font-family:Georgia,serif;font-size:34px;font-weight:700;line-height:1;color:var(--indigo);font-variant-numeric:tabular-nums}
.ddtxt{font-size:12.5px;color:var(--ink2)}
.syncline{margin-top:10px;font-size:11.5px;color:var(--ink3);display:flex;align-items:center;gap:6px}
.dot{width:6px;height:6px;border-radius:50%;background:var(--ink3);flex:none}
.dot.on{background:var(--ok)}

/* ---- 진도 요약 ---- */
.summary{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--rule);
  border:1px solid var(--rule);margin:18px 0}
.summary div{background:var(--card);padding:12px 10px;text-align:center}
.summary .n{font-family:Georgia,serif;font-size:23px;font-weight:700;line-height:1.2;font-variant-numeric:tabular-nums}
.summary .l{font-size:11px;color:var(--ink3);margin-top:2px}
.summary .ok .n{color:var(--ok)} .summary .warn .n{color:var(--warn)} .summary .stop .n{color:var(--stop)}

/* ---- 필터 ---- */
.filters{display:flex;gap:7px;overflow-x:auto;padding:14px 0 4px;margin:0 -16px;
  padding-left:16px;padding-right:16px;scrollbar-width:none}
.filters::-webkit-scrollbar{display:none}
.fchip{flex:none;font-size:13px;padding:0 14px;min-height:40px;border:1px solid var(--rule);
  background:var(--card);color:var(--ink2);cursor:pointer;white-space:nowrap;border-radius:2px;
  font-family:inherit;display:inline-flex;align-items:center}
.fchip[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.fchip .c{opacity:.55;margin-left:5px;font-family:Georgia,serif}

/* ---- 문항 카드 ---- */
.list{margin-top:16px;display:flex;flex-direction:column;gap:9px}
.p{background:var(--card);border:1px solid var(--rule);box-shadow:var(--shadow)}
.p.s-ok{border-left:3px solid var(--ok)}
.p.s-mid{border-left:3px solid var(--warn)}
.p.s-no{border-left:3px solid var(--stop)}
.phead{width:100%;text-align:left;background:none;border:0;padding:13px 15px;cursor:pointer;
  display:flex;align-items:center;gap:9px;font-family:inherit;color:inherit;font-size:15px}
.ptitle{flex:1;min-width:0}
.ptopic{font-weight:500;display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pmeta{font-size:11px;color:var(--ink3);display:block;margin-top:1px}
.badge{flex:none;font-size:10px;padding:2px 6px;border:1px solid var(--rule);color:var(--ink3);border-radius:2px}
.badge.hard{color:var(--stop);border-color:color-mix(in srgb,var(--stop) 45%,transparent)}
.arrow{flex:none;width:0;height:0;border-left:5px solid var(--ink3);
  border-top:4px solid transparent;border-bottom:4px solid transparent;transition:transform .15s}
.p[open] .arrow,.p.open .arrow{transform:rotate(90deg)}
.pbody{padding:0 15px 15px;border-top:1px solid var(--rule2);display:none}
.p.open .pbody{display:block}

.stem{font-size:15px;line-height:1.85;padding-top:13px}
.stem p{margin:0 0 7px}
.cond{display:block;margin:8px 0;padding:8px 11px;border:1px solid var(--rule)}
.choices{display:flex;flex-wrap:wrap;gap:5px 18px;margin-top:8px;font-family:Georgia,serif}

.reveal{margin-top:12px;display:flex;gap:7px;flex-wrap:wrap}
.rbtn{font-size:13.5px;padding:0 18px;min-height:44px;border:1px solid var(--rule);background:var(--card);
  color:var(--ink2);cursor:pointer;font-family:inherit;border-radius:2px;
  display:inline-flex;align-items:center}
.rbtn:hover{color:var(--ink);border-color:var(--ink3)}
.rbtn[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}

.panel{display:none;margin-top:12px;font-size:14.5px;line-height:1.8;color:var(--ink2)}
.panel.on{display:block}
.panel p{margin:0 0 8px} .panel p:last-child{margin-bottom:0}
.panel .step{color:var(--ink);font-weight:500}
.panel ol{margin:0 0 8px;padding-left:19px}
.lab{display:block;font-size:10px;letter-spacing:.15em;font-weight:600;color:var(--indigo);margin-bottom:4px}
.pidea{padding-left:11px;border-left:2px solid var(--indigo)}
.palt{padding:11px 13px;border:1px dashed var(--ink3);margin:10px 0}
.palt .lab{color:var(--ink3)}
.ptrap{padding:10px 12px;background:var(--stopbg);border-left:2px solid var(--stop);color:var(--ink2)}
.ptrap .lab{color:var(--stop)}
.pknow{padding:11px 13px;border:1px solid var(--rule)}
.pknow .lab{color:var(--ink3)}
.pknow b{background:linear-gradient(transparent 58%,var(--mark) 58%)}
.pans{margin-top:10px;font-size:13px;color:var(--ink3)}
.pans b{font-family:Georgia,serif;font-size:16px;color:var(--indigo)}

/* ---- 상태 버튼 ---- */
.marks{margin-top:15px;padding-top:13px;border-top:1px solid var(--rule2)}
.marks .lab{color:var(--ink3);margin-bottom:7px}
.mrow{display:flex;gap:7px}
.mbtn{flex:1;font-size:14px;padding:4px;min-height:48px;border:1px solid var(--rule);background:var(--card);
  color:var(--ink2);cursor:pointer;font-family:inherit;border-radius:2px}
.mbtn[aria-pressed="true"]{font-weight:600}
.mbtn.ok[aria-pressed="true"]{background:var(--okbg);border-color:var(--ok);color:var(--ok)}
.mbtn.mid[aria-pressed="true"]{background:var(--warnbg);border-color:var(--warn);color:var(--warn)}
.mbtn.no[aria-pressed="true"]{background:var(--stopbg);border-color:var(--stop);color:var(--stop)}
.note{margin-top:9px;width:100%;font-family:inherit;font-size:16px;padding:11px 12px;
  border:1px solid var(--rule);background:var(--paper);color:var(--ink);resize:vertical;min-height:58px;
  line-height:1.6}
.note:focus{outline:2px solid var(--markline);outline-offset:-1px}
.notehint{font-size:11px;color:var(--ink3);margin-top:5px}

/* ---- 하단 바 ---- */
.bar{position:fixed;left:0;right:0;bottom:0;background:var(--card);border-top:1px solid var(--rule);
  padding:10px 16px calc(10px + env(safe-area-inset-bottom));z-index:30}
.barin{max-width:720px;margin:0 auto;display:flex;align-items:center;gap:12px;justify-content:space-between}
.barin span{font-size:12px;color:var(--ink2)}
.barin b{color:var(--stop)}
.barbtn{font-size:13.5px;padding:0 18px;min-height:44px;border:1px solid var(--ink);background:var(--ink);
  color:var(--paper);cursor:pointer;font-family:inherit;border-radius:2px;flex:none}
.barlink{flex:1;min-width:0;text-align:left;font-size:13px;color:var(--ink2);
  background:none;border:0;padding:0 4px 0 0;min-height:44px;cursor:pointer;font-family:inherit;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:400px){ .barlink{font-size:12.5px} }
.barlink b{color:var(--ink);font-weight:600}
.barlink .go{color:var(--indigo);font-weight:600;margin-left:6px;white-space:nowrap}
.barlink[disabled]{cursor:default;color:var(--ink3)}
.barlink[disabled] .go{display:none}
.p.flash{outline:3px solid var(--markline);outline-offset:-1px}
.barbtn[disabled]{opacity:.4;cursor:default}

/* ---- 모달 ---- */
.modal{position:fixed;inset:0;background:rgba(10,14,22,.55);z-index:40;display:none;
  align-items:flex-end;justify-content:center}
.modal.on{display:flex}
.sheet{background:var(--card);width:100%;max-width:720px;max-height:82vh;max-height:82dvh;overflow-y:auto;
  -webkit-overflow-scrolling:touch;border-top:2px solid var(--ink);
  padding:20px 18px calc(28px + env(safe-area-inset-bottom))}
.sheet h2{font-size:19px;margin-bottom:4px}
.sheet .sub{font-size:12.5px;color:var(--ink3);margin-bottom:16px}
.qitem{border-top:1px solid var(--rule2);padding:11px 0}
.qitem .t{font-weight:500;font-size:14px}
.qitem .m2{font-size:12px;color:var(--ink3);margin-top:2px}
.qitem .nt{font-size:13px;color:var(--ink2);margin-top:6px;padding:8px 10px;background:var(--paper)}
.close{margin-top:18px;width:100%;font-size:14px;min-height:48px;border:1px solid var(--rule);
  background:var(--card);color:var(--ink2);cursor:pointer;font-family:inherit}
.empty{color:var(--ink3);font-size:13.5px;padding:18px 0}

/* ---- 태블릿(아이패드) 가독성: 반드시 스타일시트 끝에 두어야 앞 규칙을 이긴다 ---- */
@media (min-width:768px){
  .stem{font-size:17px;line-height:1.9}
  .panel{font-size:16px;line-height:1.85}
  .phead{font-size:16px;padding:15px 17px}
  .pmeta{font-size:12px}
  .badge{font-size:11px}
  .choices{gap:7px 26px;font-size:17px}
  .cond{padding:10px 14px}
  .eyebrow{font-size:11.5px}
  header h1{font-size:30px}
  .summary .n{font-size:26px}
  .summary .l{font-size:12px}
  .syncline{font-size:12.5px}
  .barin span{font-size:13px}
  .notehint{font-size:12px}
}
:focus-visible{outline:2px solid var(--markline);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<div class="wrap">
  <header>
    <div class="eyebrow">수학Ⅰ · 수학Ⅱ · 확률과 통계</div>
    <h1>발상 트레이너</h1>
    <div class="dday">
      <span class="ddnum" id="dd">—</span>
      <span class="ddtxt">2027학년도 수능까지<br>2026년 11월 19일 (목)</span>
    </div>
    <div class="syncline"><span class="dot" id="syncdot"></span><span id="synctxt">불러오는 중…</span></div>
  </header>

  <div class="summary">
    <div class="ok"><div class="n" id="n-ok">0</div><div class="l">알겠음</div></div>
    <div class="warn"><div class="n" id="n-mid">0</div><div class="l">헷갈림</div></div>
    <div class="stop"><div class="n" id="n-no">0</div><div class="l">모르겠음</div></div>
  </div>

  <div class="filters" id="filters"></div>
  <div class="list" id="list"></div>
</div>

<div class="bar">
  <div class="barin">
    <button class="barlink" id="nextbtn">—</button>
    <button class="barbtn" id="reviewbtn">다시 볼 문항</button>
  </div>
</div>

<div class="modal" id="modal">
  <div class="sheet">
    <h2>다시 볼 문항</h2>
    <div class="sub">모르겠음·헷갈림으로 표시한 문항입니다. 이 목록이 다음 인쇄 세트가 됩니다.</div>
    <div id="reviewlist"></div>
    <button class="close" id="closebtn">닫기</button>
  </div>
</div>

<script>
const PROBLEMS = __DATA__;
const EXAM = new Date(2026, 10, 19);

/* ---------- D-day ---------- */
(function(){
  const today = new Date(); today.setHours(0,0,0,0);
  const d = Math.round((EXAM - today) / 86400000);
  document.getElementById('dd').textContent = d >= 0 ? 'D-' + d : 'D+' + (-d);
})();

/* ---------- 저장소: db 있으면 공유, 없으면 이 기기에만 ---------- */
const LS = 'ipsi_math_progress_v1';
let state = {};        // id -> {status, note, at}
let db = null;

function loadLocal(){
  try { state = JSON.parse(localStorage.getItem(LS) || '{}'); }
  catch(e){ state = {}; }
}
function saveLocal(){
  try { localStorage.setItem(LS, JSON.stringify(state)); } catch(e){}
}
function setSync(on, text){
  document.getElementById('syncdot').classList.toggle('on', !!on);
  document.getElementById('synctxt').textContent = text;
}

loadLocal();
setSync(false, '이 기기에만 저장됩니다');

(async function(){
  let cap = null;
  try { cap = await claude.use('db'); } catch(e){ cap = null; }
  if (!cap) return;
  db = cap;
  try {
    db.collection('progress').onSnapshot(function(snap){
      snap.docs.forEach(function(doc){
        const v = doc.data() || {};
        state[doc.id] = { status: v.status || '', note: v.note || '', at: v.at || '' };
      });
      saveLocal(); render();
      setSync(true, '진도가 함께 보는 사람과 공유됩니다');
    }, function(){ setSync(false, '이 기기에만 저장됩니다'); });
  } catch(e){ db = null; }
})();

function put(id, patch, opts){
  const cur = state[id] || { status:'', note:'' };
  const next = Object.assign({}, cur, patch, { at: new Date().toISOString() });
  state[id] = next;
  saveLocal();
  // 메모 저장은 silent — 목록을 다시 그리면 입력창이 파괴되어 포커스가 날아간다
  if (!(opts && opts.silent)) render();
  if (db) {
    db.doc('progress/' + id).set({
      status: next.status || '', note: next.note || '', at: next.at
    }).catch(function(){ setSync(false, '이 기기에만 저장됩니다'); });
  }
}

/* ---------- 렌더 ---------- */
let filter = 'all';
const pendingFlush = new Set();   // 아직 저장되지 않았을 수 있는 메모 입력창들
function flushAll(){ pendingFlush.forEach(function(f){ try { f(); } catch (e) {} }); }
document.addEventListener('visibilitychange', function(){ if (document.hidden) flushAll(); });
window.addEventListener('pagehide', flushAll);
const opened = new Set();
const shown = {};   // id -> {idea:bool, sol:bool}

const UNITS = [];
PROBLEMS.forEach(function(p){
  if (!UNITS.some(function(u){ return u.key === p.unit; }))
    UNITS.push({ key: p.unit, label: p.unitLabel });
});

function statusClass(s){
  return s === 'ok' ? 's-ok' : s === 'mid' ? 's-mid' : s === 'no' ? 's-no' : '';
}
function esc(s){
  return String(s == null ? '' : s)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;');
}

function renderFilters(){
  const el = document.getElementById('filters');
  const parts = ['<button class="fchip" data-f="all" aria-pressed="' + (filter==='all') +
    '">전체<span class="c">' + PROBLEMS.length + '</span></button>'];
  UNITS.forEach(function(u){
    const n = PROBLEMS.filter(function(p){ return p.unit === u.key; }).length;
    parts.push('<button class="fchip" data-f="' + esc(u.key) + '" aria-pressed="' +
      (filter===u.key) + '">' + esc(u.label) + '<span class="c">' + n + '</span></button>');
  });
  el.innerHTML = parts.join('');
  el.querySelectorAll('.fchip').forEach(function(b){
    b.onclick = function(){ filter = b.dataset.f; lastJumpId = null; render(); };
  });
}

function renderList(){
  const items = PROBLEMS.filter(function(p){ return filter === 'all' || p.unit === filter; });
  document.getElementById('list').innerHTML = items.map(function(p){
    const st = (state[p.id] || {}).status || '';
    const note = (state[p.id] || {}).note || '';
    const isOpen = opened.has(p.id);
    const sh = shown[p.id] || {};
    const hard = /상/.test(p.diff) && p.diff !== '중상';
    return '' +
    '<article class="p ' + statusClass(st) + (isOpen ? ' open' : '') + '" data-id="' + esc(p.id) + '">' +
      '<button class="phead" aria-expanded="' + isOpen + '">' +
        '<span class="arrow"></span>' +
        '<span class="ptitle"><span class="ptopic">' + esc(p.topic) + '</span>' +
          '<span class="pmeta">' + esc(p.unitLabel) + ' · ' + esc(p.source) + '</span></span>' +
        '<span class="badge' + (hard ? ' hard' : '') + '">' + esc(p.level) + '</span>' +
      '</button>' +
      '<div class="pbody">' +
        '<div class="stem">' + p.q + '</div>' +
        '<div class="reveal">' +
          '<button class="rbtn" data-r="idea" aria-pressed="' + !!sh.idea + '">발상</button>' +
          '<button class="rbtn" data-r="sol" aria-pressed="' + !!sh.sol + '">풀이와 정답</button>' +
        '</div>' +
        '<div class="panel pidea' + (sh.idea ? ' on' : '') + '" data-panel="idea">' +
          '<span class="lab">발상</span>' + p.idea + '</div>' +
        '<div class="panel' + (sh.sol ? ' on' : '') + '" data-panel="sol">' +
          '<span class="lab">풀이</span>' + p.sol +
          (p.alt ? '<div class="palt"><span class="lab">다른 풀이</span>' + p.alt + '</div>' : '') +
          (p.trap ? '<div class="ptrap"><span class="lab">함정</span>' + p.trap + '</div>' : '') +
          '<div class="pknow"><span class="lab">노하우</span>' + p.know + '</div>' +
          '<div class="pans">정답 <b>' + esc(p.answer) + '</b></div>' +
        '</div>' +
        '<div class="marks">' +
          '<span class="lab">풀고 나서 표시하기</span>' +
          '<div class="mrow">' +
            '<button class="mbtn ok" data-m="ok" aria-pressed="' + (st==='ok') + '">알겠음</button>' +
            '<button class="mbtn mid" data-m="mid" aria-pressed="' + (st==='mid') + '">헷갈림</button>' +
            '<button class="mbtn no" data-m="no" aria-pressed="' + (st==='no') + '">모르겠음</button>' +
          '</div>' +
          '<textarea class="note" placeholder="어디서 막혔는지 한 줄만 적어두면 다음 문제를 정확히 만들 수 있어요">' +
            esc(note) + '</textarea>' +
          '<div class="notehint">여기 적은 내용은 다음 세트를 만들 때 그대로 읽힙니다.</div>' +
        '</div>' +
      '</div>' +
    '</article>';
  }).join('');
  pendingFlush.clear();
  bind();
}

function bind(){
  document.querySelectorAll('.p').forEach(function(card){
    const id = card.dataset.id;
    card.querySelector('.phead').onclick = function(){
      if (opened.has(id)) opened.delete(id); else opened.add(id);
      render();
    };
    card.querySelectorAll('.rbtn').forEach(function(b){
      b.onclick = function(){
        const k = b.dataset.r;
        shown[id] = shown[id] || {};
        shown[id][k] = !shown[id][k];
        render();
      };
    });
    card.querySelectorAll('.mbtn').forEach(function(b){
      b.onclick = function(){
        const cur = (state[id] || {}).status || '';
        put(id, { status: cur === b.dataset.m ? '' : b.dataset.m });
      };
    });
    const ta = card.querySelector('.note');
    if (ta) {
      let t = null;
      const flush = function(){
        clearTimeout(t); t = null;
        if (((state[id] || {}).note || '') !== ta.value) put(id, { note: ta.value }, { silent: true });
      };
      ta.oninput = function(){ clearTimeout(t); t = setTimeout(flush, 400); };
      ta.onblur = flush;              // 입력창을 벗어날 때 확실히 저장
      pendingFlush.add(flush);        // 앱 전환·화면 닫힘 대비
    }
  });
}

function renderSummary(){
  let ok = 0, mid = 0, no = 0;
  PROBLEMS.forEach(function(p){
    const s = (state[p.id] || {}).status;
    if (s === 'ok') ok++; else if (s === 'mid') mid++; else if (s === 'no') no++;
  });
  document.getElementById('n-ok').textContent = ok;
  document.getElementById('n-mid').textContent = mid;
  document.getElementById('n-no').textContent = no;
  const left = PROBLEMS.length - ok - mid - no;
  const nb = document.getElementById('nextbtn');
  nb.innerHTML = left
    ? '아직 안 푼 문항 <b>' + left + '</b>개<span class="go">바로가기 →</span>'
    : '전부 표시했어요';
  nb.disabled = left === 0;
  const rb = document.getElementById('reviewbtn');
  rb.textContent = '다시 볼 문항 ' + (mid + no);
  rb.disabled = (mid + no) === 0;
}

// 어떤 이유로든 다시 그릴 때 입력 중이던 메모의 포커스와 커서 위치를 복원한다
function render(){
  const ae = document.activeElement;
  let keep = null;
  if (ae && ae.classList && ae.classList.contains('note')) {
    const card = ae.closest('.p');
    if (card) keep = { id: card.dataset.id, val: ae.value,
                       s: ae.selectionStart, e: ae.selectionEnd };
  }
  renderFilters(); renderList(); renderSummary();
  if (keep) {
    const ta = document.querySelector('.p[data-id="' + keep.id + '"] .note');
    if (ta) {
      if (ta.value !== keep.val) ta.value = keep.val;
      ta.focus();
      try { ta.setSelectionRange(keep.s, keep.e); } catch (err) {}
    }
  }
}
render();

/* ---------- 안 푼 문항으로 이동 ---------- */
function unsolvedIn(list){
  return list.filter(function(p){ return !((state[p.id] || {}).status); });
}
let lastJumpId = null;   // 마지막으로 이동한 문항 (스크롤 위치보다 안정적)

document.getElementById('nextbtn').onclick = function(){
  let pool = unsolvedIn(PROBLEMS.filter(function(p){ return filter === 'all' || p.unit === filter; }));
  if (!pool.length && filter !== 'all') {   // 지금 단원에 없으면 전체로 넓힌다
    filter = 'all'; lastJumpId = null; render();
    pool = unsolvedIn(PROBLEMS);
  }
  if (!pool.length) return;

  let start = 0;
  if (lastJumpId) {
    const i = pool.findIndex(function(p){ return p.id === lastJumpId; });
    if (i >= 0) {
      start = (i + 1) % pool.length;               // 바로 다음 안 푼 문항으로
    } else {
      // 방금 표시해서 목록에서 빠진 경우 -> 원래 있던 자리 다음부터
      const gone = PROBLEMS.findIndex(function(p){ return p.id === lastJumpId; });
      const j = pool.findIndex(function(p){ return PROBLEMS.indexOf(p) > gone; });
      start = j >= 0 ? j : 0;
    }
  }
  const target = pool[start];
  lastJumpId = target.id;

  opened.add(target.id);
  render();
  const el = document.querySelector('.p[data-id="' + target.id + '"]');
  if (!el) return;
  const smooth = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 12,
                    behavior: smooth ? 'smooth' : 'auto' });
  el.classList.add('flash');
  setTimeout(function(){ el.classList.remove('flash'); }, 1300);
};

/* ---------- 복습 목록 ---------- */
document.getElementById('reviewbtn').onclick = function(){
  const items = PROBLEMS.filter(function(p){
    const s = (state[p.id] || {}).status;
    return s === 'mid' || s === 'no';
  });
  document.getElementById('reviewlist').innerHTML = items.length ? items.map(function(p){
    const v = state[p.id] || {};
    return '<div class="qitem"><div class="t">' + esc(p.topic) + '</div>' +
      '<div class="m2">' + esc(p.unitLabel) + ' · ' + esc(p.id) + ' · ' +
      (v.status === 'no' ? '모르겠음' : '헷갈림') + '</div>' +
      (v.note ? '<div class="nt">' + esc(v.note) + '</div>' : '') + '</div>';
  }).join('') : '<div class="empty">아직 표시한 문항이 없습니다.</div>';
  document.getElementById('modal').classList.add('on');
};
document.getElementById('closebtn').onclick = function(){
  document.getElementById('modal').classList.remove('on');
};
document.getElementById('modal').onclick = function(e){
  if (e.target === this) this.classList.remove('on');
};
</script>
"""


def main():
    probs = collect()
    data = json.dumps(probs, ensure_ascii=False).replace("</script>", "<\\/script>")
    html = TEMPLATE.replace("__DATA__", data)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"생성: {OUT}")
    print(f"문항 {len(probs)}개, {len(html):,} bytes")
    print("→ 이 파일을 같은 경로로 재게시하면 URL이 유지됩니다.")


if __name__ == "__main__":
    main()
