---
id: TRI-J06
unit: 02-삼각함수
topic: 삼각함수의 값과 사분면
level: 3점
difficulty: 중
source: 2027-06모평 6번
exam: 2027-06모평
origin: 기출
core: "사분면이 부호를 정하고, 부호가 정해져야 값이 하나로 결정된다"
tags: [삼각함수,사분면,부호]
status: seed
added: 2026-09-06
answer: ①
---

## 문제

<p class="m">3π/2 &lt; θ &lt; 2π 인 θ에 대하여 cos<sup>2</sup>θ = 1/10 일 때, tan θ의 값은?</p><div class="choices"><span>① −3</span><span>② −2</span><span>③ −1</span><span>④ 2</span><span>⑤ 3</span></div>

## 발상

<span class='m'>cos<sup>2</sup>θ</span>만 주어졌으니 <span class='m'>cos θ</span>는 부호가 둘이다. <b>제4사분면이라는 조건이 부호를 하나로 못 박는다.</b>

## 풀이

<p><span class="step">① 부호부터 정한다.</span>
주어진 것은 <span class="m">cos<sup>2</sup>θ</span>이므로
<span class="m">cos θ</span>는 <b>양수와 음수 두 가지 가능성</b>이 있다.
어느 쪽인지는 <span class="m">θ</span>가 어느 사분면에 있는지가 정한다.</p>
<p class="m">3π/2 &lt; θ &lt; 2π &nbsp; → &nbsp; 제4사분면</p>
<p>제4사분면에서는 <b><span class="m">cos</span>이 양수, <span class="m">sin</span>이 음수</b>다.
(따라서 <span class="m">tan</span>은 음수가 될 것을 미리 알 수 있다.)</p>

<p><span class="step">② cos θ를 구한다.</span></p>
<p class="m">cos<sup>2</sup>θ = 1/10 → cos θ = ±1/√10</p>
<p>제4사분면이므로 양수를 택한다.</p>
<p class="m">cos θ = 1/√10</p>

<p><span class="step">③ sin θ를 구한다.</span>
삼각함수의 기본 관계 <span class="m">sin<sup>2</sup>θ + cos<sup>2</sup>θ = 1</span>을 쓴다.</p>
<p class="m">sin<sup>2</sup>θ = 1 − 1/10 = 9/10</p>
<p class="m">sin θ = ±3/√10</p>
<p>제4사분면이므로 음수를 택한다.</p>
<p class="m">sin θ = −3/√10</p>

<p><span class="step">④ tan θ를 계산한다.</span>
<span class="m">tan θ = sin θ / cos θ</span>이다.
분모와 분자에 똑같이 <span class="m">√10</span>이 있으므로 약분된다.</p>
<p class="m">tan θ = (−3/√10) ÷ (1/√10) = (−3/√10) × (√10/1) = −3</p>
<p class="m">답 ①</p>

## 노하우

<b>제곱만 주어지면 부호는 사분면이 정한다.</b> 4사분면은 cos만 양수. 부호를 먼저 적어 놓고 계산을 시작하면 마지막에 헷갈리지 않는다.
