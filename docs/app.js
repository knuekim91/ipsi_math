/* ipsi_math — 학습 사이트
   진도는 이 기기에 저장된다. 로그인은 다음 단계에서 붙인다. */
(function () {
  "use strict";

  var D = window.DATA, P = D.problems, U = D.units, S = D.subjects;
  var EX = D.exams || [], YR = D.years || [];
  var LS = "ipsi_math_v2";
  var NL = String.fromCharCode(10);

  var state = {};
  try { state = JSON.parse(localStorage.getItem(LS) || "{}"); } catch (e) { state = {}; }
  function save() { try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {} }
  function st(id) { return state[id] || {}; }

  var view = "no";          // no | unit
  var query = "";
  var unitFilter = "";      // "" = 전체
  var yearFilter = "";      // "" = 전체 학년도
  var examFilter = "";      // "" = 그 학년도 전체
  var open = {};            // id -> {card, idea, sol}

  /* ───────── 유틸 ───────── */

  /* 주소로 쓸 수 있는 것만 통과시킨다. javascript: 같은 것은 막는다. */
  function safeUrl(u) {
    u = String(u == null ? "" : u).trim();
    if (!u) return "";
    if (/^[a-zA-Z][a-zA-Z0-9+.\-]*:/.test(u)) {          // 이미 스킴이 있으면
      if (!/^https?:\/\//i.test(u)) return "";           // http(s) 아니면 거절
    } else {
      u = "https://" + u;                                // 그냥 붙여넣은 주소
    }
    try {
      var x = new URL(u);
      return (x.protocol === "http:" || x.protocol === "https:") ? x.href : "";
    } catch (e) { return ""; }
  }

  /* 화면에 보여 줄 짧은 이름 (유튜브면 그렇게 적어 준다) */
  function urlLabel(u) {
    try {
      var h = new URL(u).hostname.replace(/^www\./, "");
      if (/youtu\.?be/.test(h)) return "YouTube";
      return h;
    } catch (e) { return "링크"; }
  }

  /* 문항 파일의 lecture 는 "제목 | 주소" 또는 "주소" */
  function fixedLec(p) {
    var raw = (p.lecture || "").trim();
    if (!raw) return null;
    var i = raw.lastIndexOf("|");
    var name = i > 0 ? raw.slice(0, i).trim() : "";
    var url = safeUrl(i > 0 ? raw.slice(i + 1) : raw);
    return url ? { url: url, name: name || urlLabel(url) } : null;
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function el(id) { return document.getElementById(id); }
  function tex(node) {
    if (!window.renderMathInElement) return;
    try {
      renderMathInElement(node, {
        delimiters: [{ left: "$", right: "$", display: false }],
        throwOnError: false, ignoredTags: ["script", "noscript", "style", "textarea"]
      });
    } catch (e) {}
  }
  function toast(msg) {
    var t = el("toast"); t.textContent = msg; t.classList.add("on");
    clearTimeout(toast._t); toast._t = setTimeout(function () { t.classList.remove("on"); }, 2000);
  }
  function copy(text, msg) {
    function done() { toast(msg); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
    } else fallback(text, done);
  }
  function fallback(text, done) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); done(); }
    catch (e) { toast("복사가 안 돼요. 길게 눌러 직접 복사하세요"); }
    document.body.removeChild(ta);
  }

  /* ───────── D-day & 진도 ───────── */
  function dday() {
    var e = D.exam.split("-");
    var exam = new Date(+e[0], +e[1] - 1, +e[2]);
    var t = new Date(); t.setHours(0, 0, 0, 0);
    return Math.round((exam - t) / 86400000);
  }
  function pool() {   // 학년도·시험 필터만 적용한 문항 (단원 개수의 기준)
    return P.filter(function (p) {
      if (yearFilter && p.year !== yearFilter) return false;
      if (examFilter && p.exam !== examFilter) return false;
      return true;
    });
  }
  function yearOf(id) {
    for (var i = 0; i < YR.length; i++) if (YR[i].id === id) return YR[i];
    return null;
  }
  function counts() {
    var c = { ok: 0, mid: 0, no: 0 };
    pool().forEach(function (p) { var s = st(p.id).status; if (c[s] !== undefined) c[s]++; });
    return c;
  }
  function paintHead() {
    var d = dday();
    el("dday").textContent = d >= 0 ? "D-" + d : "D+" + (-d);
    var c = counts();
    el("n-ok").textContent = c.ok; el("n-mid").textContent = c.mid; el("n-no").textContent = c.no;
    var pl = pool();
    el("cnt-all").textContent = pl.length;
    var seen = c.ok + c.mid + c.no, C = 2 * Math.PI * 86;
    var r = el("ring");
    r.style.strokeDasharray = C;
    r.style.strokeDashoffset = C * (1 - (pl.length ? seen / pl.length : 0));
  }

  /* ───────── 과목 · 단원 타일 ───────── */
  function paintUnits() {
    var pl = pool();
    function nOf(u) { return pl.filter(function (p) { return p.unit === u; }).length; }
    el("subject-grid").innerHTML = S.map(function (sub) {
      var total = 0;
      sub.units.forEach(function (u) { total += nOf(u); });
      var tiles = sub.units.map(function (u) {
        var m = U[u];
        var mine = pl.filter(function (p) { return p.unit === u; });
        var done = mine.filter(function (p) { return st(p.id).status; }).length;
        var pct = mine.length ? Math.round(done / mine.length * 100) : 0;
        return '<button class="utile" style="--h:' + m.hue + '" data-u="' + esc(u) + '"' +
          ' aria-pressed="' + (unitFilter === u) + '">' +
          '<span class="dot"></span>' +
          '<span class="un">' + esc(m.label) + '</span>' +
          '<span class="uc">' + mine.length + '문항 · ' + done + '개 표시</span>' +
          '<span class="ub"><i style="width:' + pct + '%"></i></span></button>';
      }).join("");
      return '<div class="subj"><div class="subj-t">' + esc(sub.key) +
        '<small>' + total + '문항</small></div>' +
        '<div class="ugrid" style="--n:' + sub.units.length + '">' + tiles + '</div></div>';
    }).join("");

    Array.prototype.forEach.call(document.querySelectorAll(".utile"), function (b) {
      b.onclick = function () {
        unitFilter = (unitFilter === b.dataset.u) ? "" : b.dataset.u;
        paintUnits(); paintFilters(); paintList();
        el("toolbar").scrollIntoView({ block: "start" });
      };
    });
  }

  /* ───────── 단원 필터 칩 ───────── */
  function paintExams() {
    var yr = el("yrow"), ex = el("exrow");
    if (!yr) return;

    /* 1단 — 학년도 (문항이 있는 학년도만) */
    var yp = ['<button class="yb" data-y="" aria-pressed="' + (yearFilter === "") +
      '">전체 <i>' + P.length + '</i></button>'];
    YR.forEach(function (y) {
      yp.push('<button class="yb" data-y="' + esc(y.id) + '" aria-pressed="' +
        (yearFilter === y.id) + '">' + esc(y.short) + ' <i>' + y.count + '</i></button>');
    });
    yr.innerHTML = yp.join("");
    var nowEl = el("ynow");
    if (nowEl) {
      var yy = yearFilter && yearOf(yearFilter);
      var lab = !yy ? "전체 " + P.length + "문항"
        : (examFilter ? yy.label + " · " + (function () {
            for (var i = 0; i < yy.exams.length; i++)
              if (yy.exams[i].id === examFilter) return yy.exams[i].label;
            return "";
          })() : yy.label);
      nowEl.textContent = lab;
    }
    Array.prototype.forEach.call(yr.querySelectorAll(".yb"), function (b) {
      b.onclick = function () {
        yearFilter = (yearFilter === b.dataset.y) ? "" : b.dataset.y;
        examFilter = "";                      // 학년도를 바꾸면 시험 선택은 푼다
        paintHead(); paintUnits(); paintExams(); paintFilters(); paintList();
      };
    });

    /* 2단 — 그 학년도의 시험 (학년도를 고른 뒤에만) */
    if (!ex) return;
    var y = yearFilter && yearOf(yearFilter);
    if (!y) { ex.innerHTML = ""; return; }
    var xp = ['<span class="lead">' + esc(y.label) + '</span>',
      '<button class="exb" data-e="" aria-pressed="' + (examFilter === "") +
      '">전체 <b>' + y.count + '</b></button>'];
    y.exams.forEach(function (e) {
      xp.push('<button class="exb" data-e="' + esc(e.id) + '" aria-pressed="' +
        (examFilter === e.id) + '">' + esc(e.label) + ' <b>' + e.count + '</b></button>');
    });
    ex.innerHTML = xp.join("");
    Array.prototype.forEach.call(ex.querySelectorAll(".exb"), function (b) {
      b.onclick = function () {
        examFilter = b.dataset.e;
        paintHead(); paintUnits(); paintExams(); paintFilters(); paintList();
      };
    });
  }

  function paintFilters() {
    var pl = pool();
    function nOf(u) { return pl.filter(function (p) { return p.unit === u; }).length; }
    var parts = ['<button class="fc" data-u="" aria-pressed="' + (unitFilter === "") +
      '" style="--h:220"><i></i>전체 ' + pl.length + '</button>'];
    Object.keys(U).sort().forEach(function (u) {
      if (!nOf(u)) return;
      parts.push('<button class="fc" data-u="' + esc(u) + '" style="--h:' + U[u].hue +
        '" aria-pressed="' + (unitFilter === u) + '"><i></i>' + esc(U[u].label) +
        " " + nOf(u) + "</button>");
    });
    parts.push('<span class="hits" id="hits"></span>');
    el("filt").innerHTML = parts.join("");
    Array.prototype.forEach.call(document.querySelectorAll(".fc"), function (b) {
      b.onclick = function () {
        unitFilter = b.dataset.u; paintUnits(); paintFilters(); paintList();
      };
    });
  }

  /* ───────── 목록 ───────── */
  function match(p) {
    if (yearFilter && p.year !== yearFilter) return false;
    if (examFilter && p.exam !== examFilter) return false;
    if (unitFilter && p.unit !== unitFilter) return false;
    if (query && (p.search || "").indexOf(query) < 0) return false;
    return true;
  }

  function card(p) {
    var s = st(p.id), o = open[p.id] || {};
    var h = U[p.unit].hue, cls = s.status ? " s-" + s.status : "";
    var body =
      '<div class="pbd">' +
        '<div class="stem">' + p.q + '</div>' +
        '<div class="acts">' +
          (p.idea ? '<button class="act" data-t="idea" aria-pressed="' + !!o.idea + '">핵심 아이디어</button>' : "") +
          (p.sol ? '<button class="act" data-t="sol" aria-pressed="' + !!o.sol + '">풀이와 정답</button>' : "") +
        '</div>' +
        (p.idea ? '<div class="pane' + (o.idea ? " on" : "") + '" data-p="idea">' +
          '<div class="idea"><span class="lab">핵심 아이디어</span>' + p.idea + '</div></div>' : "") +
        (p.sol ? '<div class="pane' + (o.sol ? " on" : "") + '" data-p="sol">' +
          '<div class="sol"><span class="lab">풀이</span>' + p.sol + '</div>' +
          (p.alt ? '<div class="alt"><span class="lab">다른 풀이</span>' + p.alt + '</div>' : "") +
          (p.trap ? '<div class="trap"><span class="lab">함정</span>' + p.trap + '</div>' : "") +
          (p.know ? '<div class="know"><span class="lab">노하우</span>' + p.know + '</div>' : "") +
          '<div class="ansbig"><span>정답</span><b>' + esc(p.answer) + '</b></div>' +
          '</div>' : "") +
        (function () {
          var fx = fixedLec(p), my = safeUrl(s.lec);
          var rows = "";
          if (fx) {
            rows += '<a class="lecrow fixed" href="' + esc(fx.url) + '" target="_blank"' +
              ' rel="noopener noreferrer"><i>▶</i><b>' + esc(fx.name) + '</b>' +
              '<span>추천</span></a>';
          }
          if (my) {
            rows += '<a class="lecrow" href="' + esc(my) + '" target="_blank"' +
              ' rel="noopener noreferrer"><i>▶</i><b>' + esc(urlLabel(my)) + '</b>' +
              '<span>' + esc(my.replace(/^https?:\/\//, "").slice(0, 46)) + '</span></a>';
          }
          return '<div class="lec"><span class="lab">추천 강좌</span>' + rows +
            '<div class="lecin">' +
              '<input class="lecurl" type="url" inputmode="url" autocomplete="off"' +
                ' placeholder="유튜브 등 강의 주소를 붙여 넣으세요"' +
                ' aria-label="추천 강좌 주소" value="' + esc(s.lec || "") + '">' +
              '<button class="lecsave">저장</button>' +
              (my ? '<button class="lecdel" aria-label="지우기">✕</button>' : "") +
            '</div>' +
            (my ? '<button class="lecshare">이 강좌를 모두에게 보이도록 요청하기</button>' : "") +
            '<div class="hint">여기에 넣은 주소는 <b>이 기기에만</b> 저장됩니다. ' +
            '둘 다 보이게 하려면 위 버튼으로 알려 주세요.</div></div>';
        })() +
        '<div class="react"><span class="lab">풀고 나서</span><div class="rrow">' +
          '<button class="rb ok" data-r="ok" aria-pressed="' + (s.status === "ok") + '">알겠음</button>' +
          '<button class="rb mid" data-r="mid" aria-pressed="' + (s.status === "mid") + '">헷갈림</button>' +
          '<button class="rb no" data-r="no" aria-pressed="' + (s.status === "no") + '">모르겠음</button>' +
        '</div>' +
        '<div class="ask' + ((s.status === "mid" || s.status === "no") ? " on" : "") + '">' +
          '<textarea placeholder="어디까지 알겠고 어디부터 막히는지 적어 주세요. 적은 그대로 전달됩니다.">' +
            esc(s.note || "") + '</textarea>' +
          '<button class="sendbtn">이 내용으로 문항 만들어 달라고 하기</button>' +
          '<div class="hint">누르면 문제와 메모가 한 덩어리로 정리됩니다. 복사하거나 공유로 보내세요.</div>' +
        '</div></div>' +
      '</div>';

    return '<article class="p' + cls + (o.card ? " on" : "") + '" style="--h:' + h +
      '" id="p-' + esc(p.id) + '" data-id="' + esc(p.id) + '">' +
      '<button class="phd" aria-expanded="' + !!o.card + '">' +
        '<span class="pno">' + p.no + '</span>' +
        '<span class="pt"><b>' + esc(p.topic) + '</b><span>' + esc(U[p.unit].label) +
          " · " + esc(p.source) + '</span></span>' +
        (p.origin && p.origin !== "기출"
          ? '<span class="bdg">' + esc(p.origin) + '</span>' : "") +
        '<span class="plv">' + esc(p.level) + '</span><span class="pmk"></span>' +
      '</button>' + body + '</article>';
  }

  function paintList() {
    var items = P.filter(match), host = el("list");
    var hits = el("hits");
    if (hits) hits.textContent = query ? "검색 결과 " + items.length + "개" : "";

    if (!items.length) {
      host.innerHTML = '<div class="empty"><b>찾는 문항이 없습니다</b>다른 낱말로 찾아보세요.</div>';
      return;
    }
    var html;
    if (view === "unit") {
      html = "";
      S.forEach(function (sub) {
        sub.units.forEach(function (u) {
          var mine = items.filter(function (p) { return p.unit === u; });
          if (!mine.length) return;
          html += '<div class="grouphd" id="u-' + esc(u) + '" style="--h:' + U[u].hue + '">' +
            '<span class="bar"></span>' + esc(U[u].label) +
            '<small>' + esc(sub.key) + ' · ' + mine.length + '문항</small></div>';
          html += mine.map(card).join("");
        });
      });
    } else if (!examFilter && EX.length > 1) {
      html = "";
      EX.forEach(function (e) {
        var mine = items.filter(function (p) { return p.exam === e.id; });
        if (!mine.length) return;
        html += '<div class="examhd" id="e-' + esc(e.id) + '"><b>' + esc(e.full) +
          '</b><small>' + mine.length + '문항</small></div>';
        html += mine.map(card).join("");
      });
    } else {
      html = items.map(card).join("");
    }
    host.innerHTML = html;
    tex(host);
    bind(host);
  }

  function bind(host) {
    Array.prototype.forEach.call(host.querySelectorAll(".p"), function (c) {
      var id = c.dataset.id;
      var o = open[id] = open[id] || {};

      c.querySelector(".phd").onclick = function () { o.card = !o.card; paintList(); };

      Array.prototype.forEach.call(c.querySelectorAll(".act"), function (b) {
        b.onclick = function () { o[b.dataset.t] = !o[b.dataset.t]; paintList(); };
      });

      Array.prototype.forEach.call(c.querySelectorAll(".rb"), function (b) {
        b.onclick = function () {
          var cur = st(id).status;
          state[id] = Object.assign({}, st(id), { status: cur === b.dataset.r ? "" : b.dataset.r });
          save(); paintHead(); paintUnits(); paintList();
        };
      });

      var ta = c.querySelector(".ask textarea");
      if (ta) {
        var t = null;
        var flush = function () {
          clearTimeout(t); t = null;
          if ((st(id).note || "") !== ta.value) {
            state[id] = Object.assign({}, st(id), { note: ta.value }); save();
          }
        };
        ta.oninput = function () { clearTimeout(t); t = setTimeout(flush, 400); };
        ta.onblur = flush;
      }

      var lu = c.querySelector(".lecurl");
      if (lu) {
        var saveLec = function () {
          var v = lu.value.trim();
          if (v && !safeUrl(v)) { toast("주소를 확인해 주세요"); return; }
          state[id] = Object.assign({}, st(id), { lec: v });
          save(); paintList();
          toast(v ? "저장했어요" : "지웠어요");
        };
        var sb = c.querySelector(".lecsave");
        if (sb) sb.onclick = saveLec;
        lu.onkeydown = function (e) { if (e.key === "Enter") { e.preventDefault(); saveLec(); } };
        var db = c.querySelector(".lecdel");
        if (db) db.onclick = function () { lu.value = ""; saveLec(); };
        var shb = c.querySelector(".lecshare");
        if (shb) shb.onclick = function () {
          var p = P.filter(function (x) { return x.id === id; })[0];
          shareLec(p, safeUrl(st(id).lec));
        };
      }

      var send = c.querySelector(".sendbtn");
      if (send) {
        var ready = function () {
          var s = st(id);
          return ((ta && ta.value.trim()) || s.status === "mid" || s.status === "no");
        };
        send.disabled = !ready();
        if (ta) ta.addEventListener("input", function () { send.disabled = !ready(); });
        send.onclick = function () {
          if (ta) { state[id] = Object.assign({}, st(id), { note: ta.value }); save(); }
          var p = P.filter(function (x) { return x.id === id; })[0];
          share(p);
        };
      }
    });
  }

  /* ───────── 질문 만들기 ───────── */
  var LABEL = { ok: "알겠음", mid: "헷갈림", no: "모르겠음" };
  function askText(p) {
    var s = st(p.id);
    var plain = p.q.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    var L = ["[ipsi_math 질문]",
      "문항: " + p.no + "번 · " + p.id + " · " + p.topic,
      "단원: " + U[p.unit].label + " / 출처: " + p.source + " / 배점: " + p.level];
    if (s.status) L.push("표시: " + (LABEL[s.status] || s.status));
    L.push("", "[문제]", plain, "", "[적은 것]", (s.note || "").trim() || "(없음)", "",
      "[요청] 위 메모에 맞춰 막힌 지점부터 세울 도입 문항과",
      "같은 수준의 유사문항을 만들어 주세요.");
    return L.join(NL);
  }
  function lecText(p, url) {
    return ["[ipsi_math 강좌]",
      "문항: " + p.no + "번 · " + p.id + " · " + p.topic,
      "출처: " + p.source,
      "링크: " + url,
      "",
      "[요청] 이 강좌를 문항 파일의 lecture 에 넣어 주세요."].join(NL);
  }
  function shareLec(p, url) {
    if (!url) return;
    var txt = lecText(p, url);
    if (navigator.share) {
      navigator.share({ title: "ipsi_math 강좌", text: txt }).then(
        function () { toast("보냈어요"); },
        function (e) { if (!e || e.name !== "AbortError") copy(txt, "복사했어요. 붙여넣어 보내세요"); });
    } else copy(txt, "복사했어요. Claude에게 붙여넣으세요");
  }

  function share(p) {
    var txt = askText(p);
    if (navigator.share) {
      navigator.share({ title: "ipsi_math 질문", text: txt }).then(
        function () { toast("보냈어요"); },
        function (e) { if (!e || e.name !== "AbortError") copy(txt, "복사했어요. 붙여넣어 보내세요"); });
    } else copy(txt, "복사했어요. Claude에게 붙여넣으세요");
  }

  /* ───────── 검색 · 보기 ───────── */
  var q = el("q"), box = q.parentNode;
  q.addEventListener("input", function () {
    query = q.value.trim().toLowerCase();
    box.classList.toggle("on", q.value !== "");
    paintList();
  });
  q.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { q.value = ""; query = ""; box.classList.remove("on"); paintList(); q.blur(); }
  });
  el("qx").onclick = function () { q.value = ""; query = ""; box.classList.remove("on"); paintList(); q.focus(); };

  Array.prototype.forEach.call(document.querySelectorAll(".vw"), function (b) {
    b.onclick = function () {
      view = b.dataset.view;
      Array.prototype.forEach.call(document.querySelectorAll(".vw"), function (x) {
        x.classList.toggle("on", x === b);
      });
      paintList();
    };
  });

  /* ───────── 시작 ───────── */
  paintHead(); paintUnits(); paintExams(); paintFilters(); paintList();

  /* 주소의 #p-12 (문항 번호) / #u-05-미분 (단원) 으로 바로 가기.
     페이지가 이미 열려 있을 때도 동작하도록 hashchange 를 함께 듣는다. */
  function gotoHash() {
    if (!location.hash) return;
    var target = decodeURIComponent(location.hash.slice(1));
    if (target.indexOf("p-") === 0) {
      var key = target.slice(2);
      var hit = P.filter(function (x) { return x.id === key; })[0];
      if (!hit && /^\d+$/.test(key)) {               // #p-21 같은 옛 주소
        var no = +key;
        hit = P.filter(function (x) {
          return x.no === no && (!yearFilter || x.year === yearFilter) &&
            (!examFilter || x.exam === examFilter);
        })[0] || P.filter(function (x) { return x.no === no; })[0];
      }
      if (hit) {
        if ((yearFilter && hit.year !== yearFilter) ||
            (examFilter && hit.exam !== examFilter)) {
          yearFilter = ""; examFilter = ""; paintHead(); paintExams();
        }
        if (unitFilter && hit.unit !== unitFilter) {   // 필터에 가려 있으면 푼다
          unitFilter = ""; paintUnits(); paintFilters();
        }
        target = "p-" + hit.id;
        open[hit.id] = Object.assign({}, open[hit.id], { card: true });
        paintList();
      }
    } else if (target.indexOf("u-") === 0) {
      view = "unit";
      Array.prototype.forEach.call(document.querySelectorAll(".vw"), function (x) {
        x.classList.toggle("on", x.dataset.view === "unit");
      });
      paintList();
    }
    setTimeout(function () {
      var n = document.getElementById(target);
      if (n) n.scrollIntoView({ block: "start" });
    }, 140);
  }
  window.addEventListener("hashchange", gotoHash);
  gotoHash();
})();
