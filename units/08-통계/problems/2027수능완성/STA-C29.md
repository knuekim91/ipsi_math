---
id: STA-C29
unit: 08-통계
topic: 두 정규분포 곡선 사이의 넓이 차
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 29번
exam: 2027-수능완성
origin: 기출
core: "S₁−S₂는 두 곡선 아래 넓이의 차이므로 교점을 몰라도 확률의 차로 바뀐다"
tags: [정규분포,표준화,확률밀도함수,이항분포]
status: seed
added: 2026-09-07
answer: 136
---

## 문제

<p>두 집합 <span class="m">A = {1, 2}</span>,
<span class="m">B = {n | 1 ≤ n ≤ 12}</span> (<span class="m">n</span>은 자연수)에 대하여
<span class="m">f : A → B</span>이고
<span class="m">f(1) ≤ f(2)</span>인 모든 함수 <span class="m">f</span> 중에서
임의로 하나를 선택하는 시행을 한다. 이 시행을 <span class="m">100</span>번 반복할 때
선택한 함수 <span class="m">f</span>에 대하여
<span class="m">f(1), f(2)</span>의 값이 모두 소수이고
<span class="m">f(1) + f(2)</span>의 값이 <span class="m">5</span>의 배수인 함수
<span class="m">f</span>의 개수를 확률변수 <span class="m">X</span>라 하고,
확률변수 <span class="m">X</span>의 평균을 <span class="m">m</span>,
표준편차를 <span class="m">σ</span>라 하자.</p>
<p>두 확률변수 <span class="m">Y<sub>1</sub></span>과 <span class="m">Y<sub>2</sub></span>는
각각 정규분포 <span class="m">N(m, σ<sup>2</sup>)</span>,
<span class="m">N(2m, 4σ<sup>2</sup>)</span>을 따르고,
두 확률변수 <span class="m">Y<sub>1</sub>, Y<sub>2</sub></span>의 확률밀도함수는
각각 <span class="m">g(x), h(x)</span>이다.
<span class="m">m ≤ x ≤ 2m</span>에서 그림과 같이 두 함수
<span class="m">y = g(x)</span>, <span class="m">y = h(x)</span>의 그래프와
직선 <span class="m">x = m</span>으로 둘러싸인 부분의 넓이를
<span class="m">S<sub>1</sub></span>, 두 함수
<span class="m">y = g(x)</span>, <span class="m">y = h(x)</span>의 그래프와
직선 <span class="m">x = 2m</span>으로 둘러싸인 부분의 넓이를
<span class="m">S<sub>2</sub></span>라 하자.
아래 표준정규분포표를 이용하여
<span class="m">1000 × (S<sub>1</sub> − S<sub>2</sub>)</span>의 값을 구하시오.</p>

<div class="fig">
<svg viewBox="0 0 380 230" role="img" aria-label="두 정규분포 곡선. 왼쪽의 높고 좁은 곡선 y=g(x)는 x=m에서 최대, 오른쪽의 낮고 넓은 곡선 y=h(x)는 x=2m에서 최대. 두 곡선이 만나는 점을 기준으로 왼쪽이 S1, 오른쪽이 S2이다.">
  <path class="rg" d="M148 190 L148 60 C160 52 172 60 186 96 L186 190 Z"/>
  <path class="ax" d="M30 190 H360 M100 205 V25"/>
  <path class="ax" d="M360 190 l-6 -3.5 v7 z" fill="currentColor"/>
  <path class="cv" d="M40 189 C90 187 120 150 148 60 C176 150 206 187 260 189"/>
  <path class="cv" d="M40 190 C110 189 150 175 186 96 C222 175 300 188 360 189"/>
  <path class="gd" d="M148 60 V190 M186 96 V190"/>
  <text x="148" y="205" text-anchor="middle" class="v">m</text>
  <text x="192" y="205" text-anchor="middle" class="v">2m</text>
  <text x="93"  y="205" text-anchor="end">O</text>
  <text x="158" y="120">S₁</text>
  <text x="192" y="86">S₂</text>
  <text x="152" y="48">y = g(x)</text>
  <text x="262" y="170">y = h(x)</text>
  <text class="v" x="370" y="186">x</text>
  <text class="v" x="108" y="34">y</text>
</svg>
</div>

<span class="cond"><span class="m">z</span> : 1.0 / 1.5 / 2.0 / 2.5 / 3.0<br>
<span class="m">P(0 ≤ Z ≤ z)</span> : 0.341 / 0.433 / 0.477 / 0.494 / 0.499</span>

## 발상

<b>두 넓이를 각각 구하려 하면 두 곡선의 교점을 알아야 한다.</b>
그런데 정규분포 곡선의 교점은 구할 수 없다.<br><br>
그래서 <b><span class="m">S<sub>1</sub> − S<sub>2</sub></span>를 통째로 본다.</b>
교점을 <span class="m">c</span>라 하면
<span class="m">S<sub>1</sub></span>은 <span class="m">m</span>부터 <span class="m">c</span>까지
<span class="m">g</span>가 위에 있는 부분,
<span class="m">S<sub>2</sub></span>는 <span class="m">c</span>부터 <span class="m">2m</span>까지
<span class="m">h</span>가 위에 있는 부분이므로</p>
<p class="m">S<sub>1</sub> − S<sub>2</sub> = ∫<sub>m</sub><sup>c</sup>(g−h)dx + ∫<sub>c</sub><sup>2m</sup>(g−h)dx = ∫<sub>m</sub><sup>2m</sup>(g−h)dx</p>
<p><b>교점이 사라지고 <span class="m">m</span>부터 <span class="m">2m</span>까지의 확률의 차</b>가 된다.

## 풀이

<p><span class="step">① 한 번의 시행에서의 확률을 구한다.</span>
먼저 <span class="m">f(1) ≤ f(2)</span>인 함수의 개수를 센다.
<span class="m">1</span>부터 <span class="m">12</span>까지에서 중복을 허용해
두 값을 고르면 순서가 저절로 정해지므로 중복조합이다.</p>
<p class="m"><sub>12</sub>H<sub>2</sub> = <sub>13</sub>C<sub>2</sub> = 78</p>
<p>이 중 조건을 만족시키는 것을 찾는다.
<span class="m">12</span> 이하의 소수는 <span class="m">2, 3, 5, 7, 11</span>이고,
<span class="m">f(1) ≤ f(2)</span>이면서 합이 <span class="m">5</span>의 배수인 쌍을 모두 적으면</p>
<p class="m">(2, 3) → 합 5 &nbsp;/&nbsp; (3, 7) → 합 10 &nbsp;/&nbsp; (5, 5) → 합 10</p>
<p>세 가지뿐이다. 따라서 한 번의 시행에서의 확률은</p>
<p class="m">p = 3/78 = 1/26</p>

<p><span class="step">② X의 평균과 표준편차를 구한다.</span>
<span class="m">100</span>번 반복하므로
<span class="m">X</span>는 이항분포 <span class="m">B(100, 1/26)</span>을 따른다.</p>
<p class="m">m = 100 × 1/26 = 50/13</p>
<p class="m">σ<sup>2</sup> = 100 × (1/26) × (25/26) = 2500/676 = 625/169</p>
<p class="m">σ = 25/13</p>
<p><b>여기서 중요한 관계가 나온다.</b></p>
<p class="m">m = 50/13 = 2 × (25/13) = 2σ</p>

<p><span class="step">③ 넓이의 차를 확률의 차로 바꾼다.</span>
두 곡선의 교점을 <span class="m">c</span>라 하면
<span class="m">S<sub>1</sub> = ∫<sub>m</sub><sup>c</sup>(g−h)dx</span>,
<span class="m">S<sub>2</sub> = ∫<sub>c</sub><sup>2m</sup>(h−g)dx</span>이므로</p>
<p class="m">S<sub>1</sub> − S<sub>2</sub> = ∫<sub>m</sub><sup>c</sup>(g−h)dx + ∫<sub>c</sub><sup>2m</sup>(g−h)dx = ∫<sub>m</sub><sup>2m</sup>(g−h)dx</p>
<p>확률밀도함수의 적분은 확률이므로</p>
<p class="m">S<sub>1</sub> − S<sub>2</sub> = P(m ≤ Y<sub>1</sub> ≤ 2m) − P(m ≤ Y<sub>2</sub> ≤ 2m)</p>

<p><span class="step">④ 각각을 표준화한다.</span>
<span class="m">Y<sub>1</sub> ~ N(m, σ<sup>2</sup>)</span>이므로
<span class="m">(Y<sub>1</sub> − m)/σ</span>로 바꾼다.
②에서 <span class="m">m = 2σ</span>임을 쓴다.</p>
<p class="m">x = m → z = 0, &nbsp; x = 2m → z = (2m−m)/σ = m/σ = 2</p>
<p class="m">P(m ≤ Y<sub>1</sub> ≤ 2m) = P(0 ≤ Z ≤ 2) = 0.477</p>
<p><span class="m">Y<sub>2</sub> ~ N(2m, (2σ)<sup>2</sup>)</span>이므로
평균이 <span class="m">2m</span>, 표준편차가 <span class="m">2σ</span>다.</p>
<p class="m">x = m → z = (m−2m)/(2σ) = −m/(2σ) = −1, &nbsp; x = 2m → z = 0</p>
<p class="m">P(m ≤ Y<sub>2</sub> ≤ 2m) = P(−1 ≤ Z ≤ 0) = P(0 ≤ Z ≤ 1) = 0.341</p>

<p><span class="step">⑤ 답을 만든다.</span></p>
<p class="m">S<sub>1</sub> − S<sub>2</sub> = 0.477 − 0.341 = 0.136</p>
<p class="m">1000 × 0.136 = 136</p>
<p class="m">답 136</p>

## 함정

<b>두 곡선의 교점을 구하려 하면 안 된다.</b>
정규분포 곡선의 교점은 고등학교 과정에서 구할 수 없다.
<span class="m">S<sub>1</sub> − S<sub>2</sub></span>를 <b>차로 묶는 순간</b> 교점이 사라진다는 것이 이 문제의 설계다.<br><br>
그리고 <b><span class="m">N(2m, 4σ<sup>2</sup>)</span>의 표준편차는
<span class="m">4σ</span>가 아니라 <span class="m">2σ</span></b>다.
분산이 <span class="m">4σ<sup>2</sup></span>이므로 제곱근을 취해야 한다.

## 노하우

<b>두 영역의 넓이의 &lsquo;차&rsquo;를 물으면 교점을 구하지 말고 하나의 적분으로 합친다.</b>
경계에서 위아래가 뒤바뀌므로 부호까지 포함해 더하면
<span class="m">∫(위쪽함수 − 아래쪽함수)</span>가 구간 전체에 대한 하나의 적분이 된다.
9월 확통 문항의 <span class="m">Σ</span> 상쇄, 1회 10번의 로그 적분 상쇄와 같은 구조다.<br><br>
<b>확률밀도함수의 정적분은 곧 확률이다.</b>
그래서 넓이 문제가 표준정규분포표 문제로 바뀐다.
<b><span class="m">m</span>과 <span class="m">σ</span> 사이의 관계(<span class="m">m = 2σ</span>)를
먼저 찾아 두면</b> 표준화한 값이 표에 있는 수로 딱 떨어진다.
