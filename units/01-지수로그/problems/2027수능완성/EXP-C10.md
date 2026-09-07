---
id: EXP-C10
unit: 01-지수로그
topic: 로그 곡선으로 둘러싸인 넓이와 격자점
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 10번
exam: 2027-수능완성
origin: 기출
core: "평행이동한 두 로그 곡선의 적분은 서로 상쇄되어 넓이가 직선 부분만 남는다"
tags: [로그함수,넓이,정적분,격자점]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>함수 <span class="m">y = log<sub>3</sub>(x−1)</span>의 그래프 위의 점
<span class="m">A(4, 1)</span>을 지나고 기울기가 <span class="m">−2</span>인 직선을
<span class="m">l</span>이라 하자. 그림과 같이 <span class="m">x ≥ 0</span>에서
두 함수 <span class="m">y = log<sub>3</sub>(x−1)</span>,
<span class="m">y = log<sub>3</sub>(x+1) + 4</span>의 그래프와
<span class="m">x</span>축, <span class="m">y</span>축 및 직선 <span class="m">l</span>로
둘러싸인 도형을 <span class="m">P</span>라 하자.
<span class="m">P</span>의 넓이를 <span class="m">S</span>,
<span class="m">P</span>의 내부 또는 둘레에 포함된 점 중
<span class="m">x</span>좌표와 <span class="m">y</span>좌표가 모두 정수인 점의 개수를
<span class="m">m</span>이라 하자. <span class="m">S + m</span>의 값은?</p>

<div class="fig">
<svg viewBox="0 0 360 300" role="img" aria-label="두 로그 곡선과 직선 l, x축, y축으로 둘러싸인 도형 P. 위쪽 곡선은 y=log3(x+1)+4, 아래쪽 곡선은 y=log3(x−1), 직선 l은 점 A(4,1)을 지나고 기울기가 −2이다.">
  <path class="rg" d="M60 260 L60 148 C82 137 104 129 126 123 L126 123 L214 260 Z"/>
  <path class="ax" d="M30 260 H345 M60 285 V30"/>
  <path class="ax" d="M345 260 l-6 -3.5 v7 z" fill="currentColor"/>
  <path class="ax" d="M60 30 l-3.5 6 h7 z" fill="currentColor"/>
  <path class="cv" d="M62 40 C68 92 86 128 126 123 C170 118 230 100 335 82"/>
  <path class="cv" d="M99 285 C104 216 116 190 137 186 C180 178 250 158 335 140"/>
  <path class="cv" d="M126 78 L245 293" stroke-dasharray="0"/>
  <path class="gd" d="M60 214 H214 M214 214 V260 M126 123 V260 M126 123 H60"/>
  <circle class="pt" cx="214" cy="214" r="4"/>
  <circle class="pt" cx="126" cy="123" r="4"/>
  <text x="60"  y="278" text-anchor="middle">O</text>
  <text x="214" y="278" text-anchor="middle">4</text>
  <text x="126" y="278" text-anchor="middle">2</text>
  <text x="52"  y="218" text-anchor="end">1</text>
  <text x="52"  y="127" text-anchor="end">5</text>
  <text x="222" y="208">A</text>
  <text x="105" y="205" class="v">P</text>
  <text x="248" y="300" class="v">l</text>
  <text x="252" y="70">y = log₃(x+1)+4</text>
  <text x="252" y="132">y = log₃(x−1)</text>
  <text class="v" x="353" y="256">x</text>
  <text class="v" x="68" y="40">y</text>
</svg>
</div>

<div class="choices"><span>① 28</span><span>② 30</span><span>③ 32</span>
<span>④ 34</span><span>⑤ 36</span></div>

## 발상

<b>두 곡선은 평행이동한 사이</b>다.
<span class="m">log<sub>3</sub>(x+1)+4</span>는 <span class="m">log<sub>3</sub>(x−1)</span>을
왼쪽으로 <span class="m">2</span>, 위로 <span class="m">4</span>만큼 옮긴 것이다.<br><br>
그래서 넓이를 계산할 때 <b>위쪽 곡선 아래의 적분과 아래쪽 곡선 아래의 적분이 정확히 같아져 상쇄된다.</b>
로그의 정적분은 고등학교 과정에서 계산할 수 없는데, 이 문제는 <b>계산하지 말라고 만든 문제</b>다.
남는 것은 직선 부분의 넓이뿐이다.

## 풀이

<p><span class="step">① 직선 l의 식을 구한다.</span>
점 <span class="m">A(4, 1)</span>을 지나고 기울기가 <span class="m">−2</span>이므로</p>
<p class="eqx m">y = −2(x − 4) + 1 = −2x + 9</p>
<p>(<span class="m">A</span>가 정말 곡선 위의 점인지 확인하면
<span class="m">log<sub>3</sub>(4−1) = log<sub>3</sub>3 = 1</span> ✓)</p>

<p><span class="step">② 도형 P의 경계를 하나씩 정한다.</span>
먼저 위쪽 곡선과 직선 <span class="m">l</span>이 만나는 점을 찾는다.</p>
<p class="m">log<sub>3</sub>(x+1) + 4 = −2x + 9 → log<sub>3</sub>(x+1) = 5 − 2x</p>
<p><span class="m">x = 2</span>를 넣으면 왼쪽은 <span class="m">log<sub>3</sub>3 = 1</span>,
오른쪽은 <span class="m">5 − 4 = 1</span>로 같다. 따라서 교점은 <span class="m">(2, 5)</span>이다.</p>
<p>이제 <span class="m">P</span>의 경계가 정해진다.</p>
<p class="m">0 ≤ x ≤ 2 : 위는 y = log<sub>3</sub>(x+1) + 4, 아래는 x축</p>
<p class="m">2 ≤ x ≤ 4 : 위는 직선 y = −2x + 9, 아래는 y = log<sub>3</sub>(x−1)</p>

<p><span class="step">③ 넓이를 식으로 쓴다.</span>
위쪽 경계에서 아래쪽 경계를 뺀 것을 적분한다.</p>
<p class="eqx m">S = ∫<sub>0</sub><sup>2</sup>{log<sub>3</sub>(x+1) + 4}dx + ∫<sub>2</sub><sup>4</sup>(−2x+9)dx − ∫<sub>2</sub><sup>4</sup>log<sub>3</sub>(x−1)dx</p>

<p><span class="step">④ 두 로그 적분이 상쇄됨을 보인다.</span>
첫 번째 적분에서 <span class="m">u = x + 1</span>로 바꾸면 적분 구간이
<span class="m">1</span>부터 <span class="m">3</span>까지가 된다.</p>
<p class="eqx m">∫<sub>0</sub><sup>2</sup>log<sub>3</sub>(x+1)dx = ∫<sub>1</sub><sup>3</sup>log<sub>3</sub>u du</p>
<p>세 번째 적분에서 <span class="m">u = x − 1</span>로 바꾸면 역시 구간이
<span class="m">1</span>부터 <span class="m">3</span>까지다.</p>
<p class="eqx m">∫<sub>2</sub><sup>4</sup>log<sub>3</sub>(x−1)dx = ∫<sub>1</sub><sup>3</sup>log<sub>3</sub>u du</p>
<p><b>두 값이 완전히 같으므로 빼면 <span class="m">0</span>이 된다.</b>
로그를 실제로 적분할 필요가 없다.</p>

<p><span class="step">⑤ 남은 것만 계산한다.</span>
첫 번째 적분에 남은 상수 <span class="m">4</span> 부분은
가로 <span class="m">2</span>, 세로 <span class="m">4</span>인 직사각형이다.</p>
<p class="eqx m">∫<sub>0</sub><sup>2</sup>4 dx = 8</p>
<p>직선 부분을 계산한다.</p>
<p class="eqx m">∫<sub>2</sub><sup>4</sup>(−2x+9)dx = [−x<sup>2</sup> + 9x]<sub>2</sub><sup>4</sup> = (−16+36) − (−4+18) = 20 − 14 = 6</p>
<p class="eqx m">S = 8 + 6 = 14</p>

<p><span class="step">⑥ 격자점을 x좌표별로 센다.</span>
<span class="m">P</span>는 <span class="m">0 ≤ x ≤ 4</span>에 걸쳐 있으므로
정수 <span class="m">x</span>를 하나씩 놓고 <span class="m">y</span>의 범위를 본다.</p>
<p class="m">x = 0 : 0 ≤ y ≤ log<sub>3</sub>1 + 4 = 4 → y = 0,1,2,3,4 (5개)</p>
<p class="m">x = 1 : 0 ≤ y ≤ log<sub>3</sub>2 + 4 ≒ 4.63 → y = 0,1,2,3,4 (5개)</p>
<p class="m">x = 2 : 0 ≤ y ≤ 5 → y = 0,1,2,3,4,5 (6개)</p>
<p class="m">x = 3 : log<sub>3</sub>2 ≒ 0.63 ≤ y ≤ 3 → y = 1,2,3 (3개)</p>
<p class="m">x = 4 : log<sub>3</sub>3 = 1 ≤ y ≤ 1 → y = 1 (1개)</p>
<p><span class="m">x = 2</span>에서 위쪽 경계가 <span class="m">5</span>인 것은
곡선과 직선이 만나는 점이기 때문이고, <span class="m">x = 4</span>에서 위아래가 모두
<span class="m">1</span>인 것은 점 <span class="m">A</span>에서 두 경계가 만나기 때문이다.</p>
<p class="eqx m">m = 5 + 5 + 6 + 3 + 1 = 20</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="eqx m">S + m = 14 + 20 = 34</p>
<p class="m">답 ④</p>

## 함정

<b>로그를 적분하려고 달려들면 안 된다.</b>
<span class="m">∫log<sub>3</sub>x dx</span>는 고등학교 과정에서 구할 수 없다.
구할 수 없는 것이 나왔다면 <b>그것은 상쇄되라고 넣어 둔 것</b>이다.<br><br>
격자점을 셀 때는 <b>경계 위의 점도 포함</b>한다는 것을 놓치기 쉽다.
문제가 &lsquo;내부 또는 둘레&rsquo;라고 못 박아 두었다.
특히 <span class="m">x = 4</span>일 때 점 <span class="m">(4, 1)</span> 하나가 살아남는다.

## 노하우

<b>두 곡선이 평행이동 관계이면 적분값이 같다.</b>
<span class="m">y = f(x)</span>와 <span class="m">y = f(x−p)+q</span>는
같은 길이의 구간에서 넓이가 같다(<span class="m">q</span>는 직사각형만큼 더해진다).
넓이를 구하는 문제에서 <b>구할 수 없는 적분이 두 번 나오면 부호를 확인해 보라</b> —
대개 빼면서 사라진다.<br><br>
그리고 <b>격자점 세기는 반드시 <span class="m">x</span>를 정수로 고정한 뒤
<span class="m">y</span>의 범위를 부등식으로 적는다.</b>
눈으로 세면 경계에 걸친 점을 빠뜨린다.
