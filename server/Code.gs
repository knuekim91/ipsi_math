/**
 * ipsi_math — 로그인 · 진도 동기화 서버 (Google Apps Script)
 *
 * 배포 방법은 server/README.md 참고.
 *
 * 스프레드시트 두 장을 쓴다. (없으면 처음 실행할 때 자동으로 만든다)
 *   users  : id | name | salt | hash | role | created
 *   state  : user | json | at
 *
 * 요청은 전부 POST 이고 본문은 JSON 문자열이다.
 * Content-Type 은 반드시 text/plain 이어야 한다.
 * (application/json 으로 보내면 브라우저가 사전 요청을 보내는데
 *  Apps Script 는 그것에 응답하지 못해 CORS 오류가 난다.)
 */

var ROUNDS = 1000;                 // 비밀번호 해시 반복 횟수
var TOKEN_DAYS = 60;               // 로그인 유지 기간

// ─────────────────────────────────────────────────────────────
// 처음 한 번 — 편집기에서 직접 실행한다
// ─────────────────────────────────────────────────────────────
/**
 * 편집기 위쪽에서 이 함수를 골라 [실행] 을 누르면
 *  1) 권한 승인 창이 떠서 미리 승인할 수 있고
 *  2) 데이터 시트를 미리 만들어 주소를 찍어 준다.
 * 안 해도 첫 가입 때 자동으로 만들어지지만, 미리 해 두면 확인이 쉽다.
 */
function setup() {
  usersSheet();
  stateSheet();
  tokenSheet();
  var url = book().getUrl();
  var code = props().getProperty('INVITE_CODE');
  Logger.log('데이터 시트 : ' + url);
  Logger.log('초대코드    : ' + (code || '(아직 없음 — 프로젝트 설정에서 INVITE_CODE 를 넣으세요)'));
  return url;
}

// ─────────────────────────────────────────────────────────────
// 진입점
// ─────────────────────────────────────────────────────────────
function doGet() {
  return out({ ok: true, service: 'ipsi_math', ver: 1 });
}

function doPost(e) {
  var req;
  try {
    req = JSON.parse(e.postData.contents);
  } catch (err) {
    return out({ ok: false, error: 'bad_request' });
  }

  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
  } catch (err) {
    return out({ ok: false, error: 'busy' });
  }

  try {
    switch (req.action) {
      case 'signup': return out(signup(req));
      case 'login':  return out(login(req));
      case 'pull':   return out(pull(req));
      case 'push':   return out(push(req));
      case 'logout': return out(logout(req));
      default:       return out({ ok: false, error: 'unknown_action' });
    }
  } catch (err) {
    return out({ ok: false, error: 'server_error', detail: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function out(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

// ─────────────────────────────────────────────────────────────
// 시트
// ─────────────────────────────────────────────────────────────
function book() {
  var id = props().getProperty('SHEET_ID');
  if (id) return SpreadsheetApp.openById(id);
  var ss = SpreadsheetApp.create('ipsi_math 데이터');
  props().setProperty('SHEET_ID', ss.getId());
  return ss;
}

function props() { return PropertiesService.getScriptProperties(); }

function sheet(name, header) {
  var ss = book();
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.appendRow(header);
    sh.setFrozenRows(1);
  }
  return sh;
}

function usersSheet() { return sheet('users', ['id', 'name', 'salt', 'hash', 'role', 'created']); }
function stateSheet() { return sheet('state', ['user', 'json', 'at']); }
function tokenSheet() { return sheet('tokens', ['token', 'user', 'expires']); }

function findRow(sh, col, value) {
  var last = sh.getLastRow();
  if (last < 2) return 0;
  var vals = sh.getRange(2, col, last - 1, 1).getValues();
  for (var i = 0; i < vals.length; i++) {
    if (String(vals[i][0]) === String(value)) return i + 2;
  }
  return 0;
}

// ─────────────────────────────────────────────────────────────
// 비밀번호 · 토큰
// ─────────────────────────────────────────────────────────────
function hashPw(pw, salt) {
  var h = salt + '|' + pw;
  for (var i = 0; i < ROUNDS; i++) {
    h = Utilities.base64Encode(
      Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, h, Utilities.Charset.UTF_8));
  }
  return h;
}

function randHex(n) {
  var s = '';
  for (var i = 0; i < n; i++) s += Math.floor(Math.random() * 16).toString(16);
  return s;
}

/** 길이가 같을 때 앞에서 끊지 않고 끝까지 비교한다 */
function sameSecret(a, b) {
  a = String(a); b = String(b);
  if (a.length !== b.length) return false;
  var diff = 0;
  for (var i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function issueToken(userId) {
  var sh = tokenSheet();
  var t = randHex(48);
  var exp = Date.now() + TOKEN_DAYS * 86400000;
  sh.appendRow([t, userId, exp]);
  return t;
}

function userOfToken(token) {
  if (!token) return null;
  var sh = tokenSheet();
  var r = findRow(sh, 1, token);
  if (!r) return null;
  var row = sh.getRange(r, 1, 1, 3).getValues()[0];
  if (Number(row[2]) < Date.now()) { sh.deleteRow(r); return null; }
  return String(row[1]);
}

// ─────────────────────────────────────────────────────────────
// 기능
// ─────────────────────────────────────────────────────────────
function signup(req) {
  var invite = props().getProperty('INVITE_CODE');
  if (!invite) return { ok: false, error: 'no_invite_configured' };
  if (!sameSecret(String(req.invite || ''), invite)) return { ok: false, error: 'bad_invite' };

  var id = String(req.id || '').trim().toLowerCase();
  var pw = String(req.pw || '');
  var name = String(req.name || '').trim() || id;
  if (!/^[a-z0-9_.-]{3,20}$/.test(id)) return { ok: false, error: 'bad_id' };
  if (pw.length < 8) return { ok: false, error: 'short_pw' };

  var sh = usersSheet();
  if (findRow(sh, 1, id)) return { ok: false, error: 'taken' };

  var salt = randHex(32);
  var role = sh.getLastRow() < 2 ? 'admin' : 'student';   // 첫 사람이 관리자
  sh.appendRow([id, name, salt, hashPw(pw, salt), role, new Date()]);

  return { ok: true, token: issueToken(id), id: id, name: name, role: role };
}

function login(req) {
  var id = String(req.id || '').trim().toLowerCase();
  var pw = String(req.pw || '');
  var sh = usersSheet();
  var r = findRow(sh, 1, id);
  if (!r) return { ok: false, error: 'bad_login' };

  var row = sh.getRange(r, 1, 1, 5).getValues()[0];
  if (!sameSecret(hashPw(pw, row[2]), row[3])) return { ok: false, error: 'bad_login' };

  return { ok: true, token: issueToken(id), id: id, name: String(row[1]), role: String(row[4]) };
}

function logout(req) {
  var sh = tokenSheet();
  var r = findRow(sh, 1, String(req.token || ''));
  if (r) sh.deleteRow(r);
  return { ok: true };
}

function readState(userId) {
  var sh = stateSheet();
  var r = findRow(sh, 1, userId);
  if (!r) return {};
  try { return JSON.parse(sh.getRange(r, 2).getValue() || '{}'); } catch (e) { return {}; }
}

function writeState(userId, obj) {
  var sh = stateSheet();
  var r = findRow(sh, 1, userId);
  var json = JSON.stringify(obj);
  if (r) sh.getRange(r, 2, 1, 2).setValues([[json, Date.now()]]);
  else sh.appendRow([userId, json, Date.now()]);
}

function pull(req) {
  var me = userOfToken(req.token);
  if (!me) return { ok: false, error: 'no_session' };
  return { ok: true, state: readState(me) };
}

/**
 * 문항별로 at(수정 시각)이 더 큰 쪽을 남긴다.
 * 기기 두 대에서 따로 고쳐도 최신 것만 살아남는다.
 */
function push(req) {
  var me = userOfToken(req.token);
  if (!me) return { ok: false, error: 'no_session' };

  var cur = readState(me);
  var inc = req.state || {};
  for (var k in inc) {
    if (!Object.prototype.hasOwnProperty.call(inc, k)) continue;
    var a = cur[k], b = inc[k];
    if (!a || Number(b && b.at || 0) >= Number(a.at || 0)) cur[k] = b;
  }
  writeState(me, cur);
  return { ok: true, state: cur };
}
