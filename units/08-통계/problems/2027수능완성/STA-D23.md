---
id: STA-D23
unit: 08-통계
topic: 이항분포의 평균과 분산
level: 2점
difficulty: 하
source: 2027 수능완성 실전 모의고사 2회 23번
exam: 2027-수능완성
origin: 기출
core: "E(X) = np 로 p를 먼저 구한 뒤 V(X) = np(1−p)에 넣는다"
tags: [이항분포,평균,분산]
status: seed
added: 2026-09-07
answer: ③
---

## 문제

<p>확률변수 <span class="m">X</span>가 이항분포
<span class="m">B(64, p)</span>를 따르고
<span class="m">E(X) = 16</span>일 때,
<span class="m">V(X)</span>의 값은?</p>

<div class="choices"><span>① 4</span><span>② 8</span><span>③ 12</span>
<span>④ 16</span><span>⑤ 20</span></div>

## 발상

<b>이항분포의 평균과 분산은 공식 두 개로 끝난다.</b>
확률변수 <span class="m">X</span>가 이항분포
<span class="m">B(n, p)</span>를 따르면</p>
<p class="m">E(X) = np, &nbsp; V(X) = np(1 − p)</p>
<p><b>두 공식에 공통으로 들어 있는 것이 <span class="m">np</span>이다.</b>
평균이 주어졌으므로 <span class="m">np = 16</span>임을 이미 알고 있고,
분산은 여기에 <span class="m">(1 − p)</span>만 곱하면 된다.
그러므로 <span class="m">p</span>만 구하면 된다.

## 풀이

<p><span class="step">① 시행 횟수와 확률을 확인한다.</span>
확률변수 <span class="m">X</span>가 이항분포
<span class="m">B(64, p)</span>를 따르므로
<span class="m">n = 64</span>이다.</p>

<p><span class="step">② 평균 공식으로 p를 구한다.</span>
이항분포의 평균은 <span class="m">E(X) = np</span>이다.</p>
<p class="m">E(X) = 64p = 16</p>
<p class="m">p = 16/64 = 1/4</p>

<p><span class="step">③ 1 − p를 구한다.</span></p>
<p class="m">1 − p = 1 − 1/4 = 3/4</p>

<p><span class="step">④ 분산을 구한다.</span>
이항분포의 분산은 <span class="m">V(X) = np(1 − p)</span>이다.
<span class="m">np = E(X) = 16</span>임을 이미 알고 있으므로
그대로 쓴다.</p>
<p class="m">V(X) = np(1 − p) = 16 × (3/4) = 12</p>
<p class="m">답 ③</p>

## 함정

<b><span class="m">V(X) = np</span>로 쓰면 안 된다.</b>
평균은 <span class="m">np</span>이고 분산은
<span class="m">np(1 − p)</span>이다.
<span class="m">(1 − p)</span>를 빠뜨리면
<span class="m">16</span>이 되어 ④번을 고르게 된다.
선택지에 <span class="m">16</span>이 들어 있는 이유가 바로 이것이다.<br><br>

<b><span class="m">p</span>와 <span class="m">1 − p</span>를 바꿔 쓰지 않는다.</b>
<span class="m">p = 1/4</span>이고
<span class="m">1 − p = 3/4</span>이다.
바꿔 넣으면 <span class="m">64 × (3/4) × (1/4) = 12</span>로
우연히 같은 값이 나오지만, 이는 곱셈이라 순서가 바뀌어도
같기 때문일 뿐이다. <span class="m">p</span>를 구하는 단계에서
<span class="m">64p = 16</span>을 <span class="m">64(1 − p) = 16</span>으로
잘못 놓으면 <span class="m">p = 3/4</span>이 되어 답이 달라진다.

## 노하우

<b>이항분포 문제는 <span class="m">np</span>를 통째로 하나의 값으로 본다.</b>
<span class="m">V(X) = np(1 − p)</span>에서
<span class="m">np</span>는 평균이므로,
<b>평균이 주어지면 그 값을 그대로 대입</b>하면 된다.
<span class="m">64 × (1/4) × (3/4)</span>처럼 다시 곱하지 않아도 되므로
계산이 짧아지고 실수도 줄어든다.<br><br>

<b>표준편차를 물으면 분산에 근호를 씌운다.</b>
<span class="m">σ(X) = √(V(X))</span>이다.
이 문제에서 표준편차를 물었다면
<span class="m">√12 = 2√3</span>이 답이 된다.
<b>무엇을 묻는지 마지막에 한 번 더 확인한다.</b>
