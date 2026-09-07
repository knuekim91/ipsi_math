---
id: DIF-C11
unit: 05-미분
topic: 위치·속도·가속도와 운동 방향
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 11번
exam: 2027-수능완성
origin: 기출
core: "운동 방향이 바뀌는 순간은 속도가 0이 되면서 부호가 바뀌는 때다"
tags: [속도,가속도,속력,운동방향]
status: seed
added: 2026-09-07
answer: ⑤
---

## 문제

<p>시각 <span class="m">t = 0</span>일 때 원점을 출발하여 수직선 위를 움직이는 점
<span class="m">P</span>가 있다. 시각이 <span class="m">t (t ≥ 0)</span>일 때
점 <span class="m">P</span>의 위치 <span class="m">x</span>가</p>
<p class="eqx m">x = (1/6)t<sup>4</sup> − 4t<sup>2</sup> + 6t</p>
<p>이다. &lt;보기&gt;에서 옳은 것만을 있는 대로 고른 것은?</p>
<span class="cond">ㄱ. 시각 <span class="m">t = 1</span>일 때 점 <span class="m">P</span>의 속도는
<span class="m">−2/3</span>이다.<br><br>
ㄴ. <span class="m">1 ≤ t ≤ 3</span>에서 점 <span class="m">P</span>의 속력의 최댓값은
<span class="m">14/3</span>이다.<br><br>
ㄷ. 점 <span class="m">P</span>가 마지막으로 운동 방향을 바꾸는 순간
점 <span class="m">P</span>의 가속도는 <span class="m">10</span>이다.</span>
<div class="choices"><span>① ㄴ</span><span>② ㄷ</span><span>③ ㄱ, ㄴ</span>
<span>④ ㄱ, ㄷ</span><span>⑤ ㄴ, ㄷ</span></div>

## 발상

세 보기가 각각 <b>속도 · 속력 · 가속도</b>를 묻는다.
셋을 헷갈리지 않는 것이 이 문제의 전부다.<br><br>
<b>속도는 위치를 미분한 것</b>이고 부호가 있다.
<b>속력은 속도의 절댓값</b>이라 항상 <span class="m">0</span> 이상이다.
<b>가속도는 속도를 한 번 더 미분한 것</b>이다.
그리고 <b>운동 방향이 바뀌는 순간은 속도가 <span class="m">0</span>이 되면서 부호가 바뀌는 때</b>다.

## 풀이

<p><span class="step">① 속도와 가속도를 먼저 구해 둔다.</span>
위치를 미분하면 속도, 속도를 미분하면 가속도다.</p>
<p class="eqx m">v(t) = (4/6)t<sup>3</sup> − 8t + 6 = (2/3)t<sup>3</sup> − 8t + 6</p>
<p class="eqx m">a(t) = 2t<sup>2</sup> − 8</p>

<p><span class="step">② ㄱ을 확인한다.</span>
<span class="m">t = 1</span>을 속도에 넣는다.</p>
<p class="eqx m">v(1) = 2/3 − 8 + 6 = 2/3 − 2 = −4/3</p>
<p>보기는 <span class="m">−2/3</span>이라 했으므로 <b>ㄱ은 거짓</b>이다.</p>

<p><span class="step">③ ㄴ을 확인한다.</span>
구간 <span class="m">1 ≤ t ≤ 3</span>에서 <b>속력</b>, 곧
<span class="m">|v(t)|</span>의 최댓값을 찾는다.
먼저 <span class="m">v</span>의 증감을 보기 위해 <span class="m">v′(t) = a(t)</span>를 쓴다.</p>
<p class="eqx m">a(t) = 2t<sup>2</sup> − 8 = 2(t+2)(t−2) = 0 → t = 2 (t ≥ 0)</p>
<p><span class="m">1 &lt; t &lt; 2</span>에서 <span class="m">a &lt; 0</span>이므로 <span class="m">v</span>가 감소하고,
<span class="m">2 &lt; t &lt; 3</span>에서 <span class="m">a &gt; 0</span>이므로 <span class="m">v</span>가 증가한다.
따라서 <span class="m">t = 2</span>에서 <span class="m">v</span>가 최소다.</p>
<p class="eqx m">v(1) = −4/3, &nbsp; v(2) = 16/3 − 16 + 6 = −14/3, &nbsp; v(3) = 18 − 24 + 6 = 0</p>
<p>이 구간에서 <span class="m">v</span>는 계속 음수이거나 <span class="m">0</span>이므로
속력은 <span class="m">|v|</span>이고, 가장 큰 것은 <span class="m">v</span>가 가장 작을 때다.</p>
<p class="eqx m">속력의 최댓값 = |−14/3| = 14/3</p>
<p><b>ㄴ은 참</b>이다.</p>

<p><span class="step">④ ㄷ을 확인한다.</span>
운동 방향이 바뀌는 순간은 <span class="m">v(t) = 0</span>인 때다.</p>
<p class="eqx m">(2/3)t<sup>3</sup> − 8t + 6 = 0</p>
<p>양변에 <span class="m">3/2</span>을 곱해 분수를 없앤다.</p>
<p class="eqx m">t<sup>3</sup> − 12t + 9 = 0</p>
<p><span class="m">t = 3</span>을 넣으면 <span class="m">27 − 36 + 9 = 0</span>이므로
<span class="m">(t−3)</span>으로 나누어떨어진다.</p>
<p class="eqx m">(t − 3)(t<sup>2</sup> + 3t − 3) = 0</p>
<p class="eqx m">t<sup>2</sup> + 3t − 3 = 0 → t = (−3 ± √21)/2</p>
<p><span class="m">√21 ≒ 4.58</span>이므로 양수인 근은
<span class="m">t ≒ 0.79</span> 하나뿐이다.
따라서 <span class="m">v = 0</span>인 시각은 <span class="m">t ≒ 0.79</span>와
<span class="m">t = 3</span> 두 개이고, <b>마지막은 <span class="m">t = 3</span></b>이다.</p>
<p class="eqx m">a(3) = 2 × 9 − 8 = 18 − 8 = 10</p>
<p><b>ㄷ은 참</b>이다.</p>

<p><span class="step">⑤ 답을 고른다.</span>
옳은 것은 <b>ㄴ, ㄷ</b>.</p>
<p class="m">답 ⑤</p>

## 함정

<b>속도와 속력을 섞으면 ㄴ에서 틀린다.</b>
이 구간에서 속도는 계속 음수라 &lsquo;최댓값&rsquo;을 그냥 찾으면
<span class="m">t = 3</span>에서 <span class="m">0</span>이 나온다.
속력은 절댓값이므로 <b>속도가 가장 작을 때 속력이 가장 크다.</b><br><br>
그리고 <b>&lsquo;마지막으로&rsquo;라는 말을 흘리면 안 된다.</b>
방향이 바뀌는 시각이 두 개인데, 앞의 것
(<span class="m">t = (−3+√21)/2</span>)을 쓰면 가속도가 <span class="m">10</span>이 아니다.

## 노하우

<b>위치 → (미분) → 속도 → (미분) → 가속도.</b>
그리고 <b>속력 = |속도|</b>다. 세 낱말이 한 문제에 다 나오면
각각 무엇을 묻는지 먼저 표시해 두고 시작한다.<br><br>
<b>운동 방향이 바뀐다 = 속도의 부호가 바뀐다.</b>
그러니 <span class="m">v(t) = 0</span>을 푸는 것이 첫걸음이고,
근이 여러 개면 문제가 &lsquo;처음&rsquo;인지 &lsquo;마지막&rsquo;인지 반드시 밝혀 준다.
삼차방정식이 나오면 <b>정수 근을 먼저 대입해 찾고 인수분해</b>한다.
