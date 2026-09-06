---
id: EXP-J20
unit: 01-지수로그
topic: 지수·로그함수의 교점
level: 4점
difficulty: 상
source: 2027-06모평 20번
exam: 2027-06모평
origin: 기출
core: "교점 조건 두 개를 로그로 합치면 αβ³=1이 β=3α로 풀린다"
tags: [지수함수,로그함수,교점,빈칸추론]
status: seed
added: 2026-09-06
answer: 48
---

## 문제

<p><span class="m">b &gt; 1</span>인 실수 <span class="m">b</span>에 대하여 두 함수 <span class="m">f(x) = b<sup>x</sup></span>, <span class="m">g(x) = −log<sub>b</sub>x</span>의 그래프가 제1사분면에서 만나는 점을 <span class="m">P(α, β)</span>라 하자. <span class="m">αβ<sup>3</sup> = 1</span>일 때, 직선 <span class="m">OP</span>의 기울기를 <span class="m">m</span>이라 하고 <span class="m">g(m)</span>을 구하는 과정이다. (단, <span class="m">O</span>는 원점)</p><span class="cond">점 <span class="m">P</span>가 두 그래프 위에 있으므로 <span class="m">β = b<sup>α</sup></span>, <span class="m">β = −log<sub>b</sub>α</span>, 즉 <span class="m">α = log<sub>b</sub>β</span>, <span class="m">log<sub>b</sub>α = −β</span>이다.<br><br>따라서 <span class="m">3α − β = 3log<sub>b</sub>β + log<sub>b</sub>α = log<sub>b</sub>(αβ<sup>3</sup>) = 0</span>이므로<br><span class="m">m = β/α = <b>(가)</b></span> 이다.<br><br>또 <span class="m">β<sup>4</sup> = m·αβ<sup>3</sup> = m</span> 이므로 <span class="m">β = <b>(나)</b></span> 이다.<br><br>한편 <span class="m">b = α<sup>−1/β</sup></span>이고 <span class="m">α = β/m</span>이므로<br><span class="m">g(m) = −log<sub>b</sub>m = β/log<sub>m</sub>α = β/(−1 + log<sub>m</sub>β) = <b>(다)</b></span> 이다.</span><p>위에서 <span class="m">(가), (나), (다)</span>에 알맞은 수를 각각 <span class="m">p, q, r</span>라 할 때, <span class="m">(p × q × r)<sup>2</sup></span>의 값을 구하시오.</p>

## 발상

<b><span class='m'>αβ<sup>3</sup> = 1</span>에 로그를 씌우면 <span class='m'>log α + 3log β = 0</span></b>이 되고, 교점 조건이 <span class='m'>log<sub>b</sub>β = α</span>, <span class='m'>log<sub>b</sub>α = −β</span>이므로 그대로 <span class='m'>−β + 3α = 0</span>. 곧 <b><span class='m'>β = 3α</span></b>, 기울기는 3이다.

## 풀이

<p><span class="step">① 점 P가 두 그래프 위에 있다는 것을 식으로 쓴다.</span>
<span class="m">P(α, β)</span>가 <span class="m">y = f(x) = b<sup>x</sup></span> 위에 있으므로</p>
<p class="m">β = b<sup>α</sup> &nbsp; 즉 &nbsp; α = log<sub>b</sub>β</p>
<p>또 <span class="m">y = g(x) = −log<sub>b</sub>x</span> 위에도 있으므로</p>
<p class="m">β = −log<sub>b</sub>α &nbsp; 즉 &nbsp; log<sub>b</sub>α = −β</p>

<p><span class="step">② (가) — 조건 αβ<sup>3</sup> = 1을 로그로 바꾼다.</span>
<b>곱이 1인 조건은 로그를 씌우면 합이 0인 조건</b>이 된다.
밑이 <span class="m">b</span>인 로그를 취한다.</p>
<p class="m">log<sub>b</sub>(αβ<sup>3</sup>) = log<sub>b</sub>1 = 0</p>
<p>왼쪽을 로그의 성질로 풀어 쓰면</p>
<p class="m">log<sub>b</sub>α + 3log<sub>b</sub>β = 0</p>
<p>①에서 얻은 <span class="m">log<sub>b</sub>α = −β</span>와
<span class="m">log<sub>b</sub>β = α</span>를 넣는다.</p>
<p class="m">−β + 3α = 0 → β = 3α</p>
<p>직선 OP의 기울기는 <span class="m">(β − 0)/(α − 0) = β/α</span>이므로</p>
<p class="m">m = β/α = 3 &nbsp; 따라서 &nbsp; p = 3</p>

<p><span class="step">③ (나) — β를 구한다.</span>
<span class="m">β = mα</span>이므로 <span class="m">β<sup>4</sup></span>을 다음과 같이 바꿔 쓸 수 있다.</p>
<p class="m">β<sup>4</sup> = β × β<sup>3</sup> = (mα) × β<sup>3</sup> = m × (αβ<sup>3</sup>)</p>
<p>괄호 안이 조건에 의해 <span class="m">1</span>이므로</p>
<p class="m">β<sup>4</sup> = m = 3</p>
<p>양변을 <span class="m">4</span>제곱근 하면 (<span class="m">β</span>는 제1사분면 점의 좌표라 양수)</p>
<p class="m">β = ⁴√3 = 3<sup>1/4</sup> &nbsp; 따라서 &nbsp; q = 3<sup>1/4</sup></p>

<p><span class="step">④ (다) — g(m)을 구한다.</span>
먼저 <span class="m">α</span>를 구한다.</p>
<p class="m">α = β/m = 3<sup>1/4</sup>/3 = 3<sup>1/4 − 1</sup> = 3<sup>−3/4</sup></p>
<p>문제의 과정이 <span class="m">g(m) = β / log<sub>m</sub>α</span>까지 왔으므로
<span class="m">log<sub>m</sub>α</span>를 계산한다. <span class="m">m = 3</span>이다.</p>
<p class="m">log<sub>m</sub>α = log<sub>3</sub>3<sup>−3/4</sup> = −3/4</p>
<p>나눗셈을 곱셈으로 바꿔 계산한다.</p>
<p class="m">g(m) = 3<sup>1/4</sup> ÷ (−3/4) = 3<sup>1/4</sup> × (−4/3) = −(4/3) × 3<sup>1/4</sup></p>
<p class="m">따라서 r = −(4/3) × 3<sup>1/4</sup></p>

<p><span class="step">⑤ 세 값을 곱한다.</span>
<span class="m">3<sup>1/4</sup></span>이 두 번 나오므로 지수를 더해 <span class="m">3<sup>1/2</sup></span>이 된다.</p>
<p class="m">p × q × r = 3 × 3<sup>1/4</sup> × (−4/3) × 3<sup>1/4</sup></p>
<p class="m">= (3 × (−4/3)) × 3<sup>1/4 + 1/4</sup> = −4 × 3<sup>1/2</sup> = −4√3</p>

<p><span class="step">⑥ 제곱한다.</span>
<b>음수이지만 제곱하므로 부호는 사라진다.</b></p>
<p class="m">(−4√3)<sup>2</sup> = 16 × 3 = 48</p>
<p class="m">답 48</p>

## 함정

<span class='m'>r</span>가 <b>음수</b>다. 제곱하면 사라지지만, 중간에 부호를 빠뜨리고 <span class='m'>log<sub>m</sub>α</span>를 양수로 두면 값 자체가 달라진다.

## 노하우

<b>곱이 1인 조건은 로그를 씌워 합이 0인 조건으로 바꾼다.</b> <span class='m'>αβ<sup>3</sup>=1 → log α + 3log β = 0</span>. 그리고 <span class='m'>y=b<sup>x</sup></span>와 <span class='m'>y=log<sub>b</sub>x</span>가 얽힌 문제는 <b>두 교점 조건을 로그로 통일해 놓으면 문자 관계가 저절로 정리된다.</b> 빈칸 추론은 <b>빈칸 다음 줄이 답을 어떻게 쓰는지 먼저 읽는 것</b>이 요령이다.
