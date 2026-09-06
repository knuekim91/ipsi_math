/* ipsi_math — 로그인과 진도 동기화
   config.js 의 IPSI_API 가 비어 있으면 이 파일은 아무것도 하지 않고,
   사이트는 지금까지처럼 이 기기의 localStorage 만 쓴다. */
(function () {
  "use strict";

  var API = (window.IPSI_API || "").trim();
  var SK = "ipsi_math_session";
  var OK_ = "ipsi_math_owner";     // 이 기기에 남은 진도가 누구 것인지
  var NL = String.fromCharCode(10);

  var me = null;                 // {token, id, name, role}
  try { me = JSON.parse(localStorage.getItem(SK) || "null"); } catch (e) { me = null; }

  function el(id) { return document.getElementById(id); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function toast(m) { if (window.IPSI && window.IPSI.toast) window.IPSI.toast(m); }

  /* ───────── 서버 부르기 ─────────
     Content-Type 을 text/plain 으로 보내야 사전 요청(preflight)이 생기지 않는다.
     Apps Script 는 사전 요청에 응답하지 못하므로 이 부분을 바꾸면 안 된다. */
  function call(action, body) {
    if (!API) return Promise.reject(new Error("no_api"));
    var payload = Object.assign({ action: action }, body || {});
    return fetch(API, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(payload)
    }).then(function (r) { return r.json(); });
  }

  var ERR = {
    bad_login: "아이디나 비밀번호가 맞지 않습니다",
    bad_invite: "초대코드가 맞지 않습니다",
    no_invite_configured: "서버에 초대코드가 설정되지 않았습니다",
    taken: "이미 있는 아이디입니다",
    bad_id: "아이디는 영문 소문자·숫자 3~20자로 만들어 주세요",
    short_pw: "비밀번호는 8자 이상으로 해 주세요",
    no_session: "로그인이 풀렸습니다. 다시 로그인해 주세요",
    busy: "서버가 바쁩니다. 잠시 뒤 다시 시도해 주세요"
  };
  function msg(e) { return ERR[e] || ("오류: " + e); }

  /* ───────── 세션 ───────── */
  function setMe(v) {
    me = v;
    try {
      if (v) localStorage.setItem(SK, JSON.stringify(v));
      else localStorage.removeItem(SK);
    } catch (e) {}
    paintAccount();
  }

  /* ───────── 동기화 ───────── */
  var pushTimer = null, pulling = false;

  function merge(local, remote) {
    var out = {}, k;
    for (k in remote) if (Object.prototype.hasOwnProperty.call(remote, k)) out[k] = remote[k];
    for (k in local) {
      if (!Object.prototype.hasOwnProperty.call(local, k)) continue;
      var a = out[k], b = local[k];
      if (!a || Number(b && b.at || 0) >= Number(a.at || 0)) out[k] = b;
    }
    return out;
  }

  function owner() { try { return localStorage.getItem(OK_) || ""; } catch (e) { return ""; } }
  function setOwner(v) { try { localStorage.setItem(OK_, v || ""); } catch (e) {} }

  function pull() {
    if (!me || pulling) return Promise.resolve();
    pulling = true;
    mark("동기화 중…");
    return call("pull", { token: me.token }).then(function (r) {
      if (!r.ok) {
        if (r.error === "no_session") { setMe(null); toast(msg(r.error)); }
        mark("연결 안 됨");
        return;
      }
      /* 이 기기에 남은 진도가 다른 사람 것이면 합치지 않는다.
         합치면 앞사람의 기록이 뒷사람 계정으로 넘어간다.
         한 번도 로그인한 적 없는 기기(주인 없음)일 때만 합친다. */
      var own = owner();
      var mine = (own === "" || own === me.id);
      var merged = mine ? merge(window.IPSI.all(), r.state || {}) : (r.state || {});
      if (!mine) toast("이 기기에 있던 다른 계정의 기록은 불러오지 않았습니다");
      setOwner(me.id);
      window.IPSI.replaceAll(merged);
      return call("push", { token: me.token, state: merged });
    }).then(function () {
      mark("동기화됨");
    }).catch(function () {
      mark("연결 안 됨");
    }).then(function () { pulling = false; });
  }

  function schedulePush() {
    if (!me) return;
    clearTimeout(pushTimer);
    mark("저장 중…");
    pushTimer = setTimeout(function () {
      call("push", { token: me.token, state: window.IPSI.all() })
        .then(function (r) {
          if (!r.ok && r.error === "no_session") { setMe(null); toast(msg(r.error)); }
          mark(r.ok ? "동기화됨" : "연결 안 됨");
        })
        .catch(function () { mark("연결 안 됨"); });
    }, 1500);
  }

  function mark(t) {
    var n = el("syncst");
    if (n) n.textContent = t;
  }

  /* ───────── 화면 ───────── */
  function paintAccount() {
    var box = el("acct");
    if (!box) return;
    if (!API) { box.innerHTML = ""; return; }

    if (!me) {
      box.innerHTML = '<button class="acbtn" id="openlogin">로그인</button>';
      el("openlogin").onclick = function () { openDlg("login"); };
      return;
    }
    box.innerHTML =
      '<span class="acwho"><b>' + esc(me.name) + '</b>' +
      '<i id="syncst">동기화됨</i></span>' +
      '<button class="acbtn ghost" id="dosync" title="지금 동기화">↻</button>' +
      '<button class="acbtn ghost" id="dologout">로그아웃</button>';
    el("dosync").onclick = function () { pull(); };
    el("dologout").onclick = function () {
      if (!confirm("로그아웃하면 이 기기에서는 동기화가 멈춥니다. 진행할까요?")) return;
      var t = me.token;
      setMe(null);
      call("logout", { token: t }).catch(function () {});
      toast("로그아웃했습니다");
    };
  }

  var mode = "login";
  function openDlg(m) {
    mode = m;
    var d = el("logindlg");
    paintDlg();
    d.classList.add("on");
    setTimeout(function () { var f = d.querySelector("input"); if (f) f.focus(); }, 50);
  }
  function closeDlg() { el("logindlg").classList.remove("on"); }

  function paintDlg() {
    var isNew = mode === "signup";
    el("logintitle").textContent = isNew ? "회원가입" : "로그인";
    el("loginbody").innerHTML =
      '<label>아이디<input id="f-id" autocomplete="username" ' +
        'placeholder="영문 소문자·숫자" autocapitalize="off" spellcheck="false"></label>' +
      '<label>비밀번호<input id="f-pw" type="password" ' +
        'autocomplete="' + (isNew ? "new-password" : "current-password") + '" ' +
        'placeholder="8자 이상"></label>' +
      (isNew
        ? '<label>이름<input id="f-name" placeholder="화면에 보일 이름"></label>' +
          '<label>초대코드<input id="f-inv" placeholder="아버지에게 받은 코드"></label>'
        : "") +
      '<div class="lerr" id="f-err"></div>';
    el("loginsubmit").textContent = isNew ? "가입하고 시작하기" : "로그인";
    el("loginswap").textContent = isNew ? "이미 계정이 있어요" : "처음이에요 (회원가입)";
    bindDlg();
  }

  function bindDlg() {
    var body = el("loginbody");
    Array.prototype.forEach.call(body.querySelectorAll("input"), function (i) {
      i.onkeydown = function (e) { if (e.key === "Enter") { e.preventDefault(); submit(); } };
    });
  }

  function submit() {
    var err = el("f-err");
    err.textContent = "";
    var id = (el("f-id").value || "").trim().toLowerCase();
    var pw = el("f-pw").value || "";
    if (!id || !pw) { err.textContent = "아이디와 비밀번호를 입력해 주세요"; return; }

    var isNew = mode === "signup";
    var body = { id: id, pw: pw };
    if (isNew) {
      body.name = (el("f-name").value || "").trim();
      body.invite = (el("f-inv").value || "").trim();
    }

    var btn = el("loginsubmit");
    btn.disabled = true;
    btn.textContent = "잠시만요…";

    call(isNew ? "signup" : "login", body).then(function (r) {
      if (!r.ok) { err.textContent = msg(r.error); return; }
      setMe({ token: r.token, id: r.id, name: r.name, role: r.role });
      closeDlg();
      toast(r.name + "님, 반갑습니다");
      return pull();
    }).catch(function () {
      err.textContent = "서버에 연결하지 못했습니다";
    }).then(function () {
      // 폼을 다시 그리면 오류 문구와 입력해 둔 값이 지워지므로 버튼만 되돌린다
      btn.disabled = false;
      btn.textContent = (mode === "signup") ? "가입하고 시작하기" : "로그인";
    });
  }

  /* ───────── 시작 ───────── */
  function boot() {
    if (!API) {                       // 서버 주소가 없으면 조용히 물러난다
      var b = el("acct");
      if (b) b.innerHTML = "";
      return;
    }
    el("loginsubmit").onclick = submit;
    el("loginswap").onclick = function () { mode = (mode === "login" ? "signup" : "login"); paintDlg(); };
    el("loginx").onclick = closeDlg;
    el("logindlg").addEventListener("click", function (e) {
      if (e.target === el("logindlg")) closeDlg();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeDlg();
    });

    paintAccount();
    window.IPSI.onChange = schedulePush;
    if (me) pull();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
