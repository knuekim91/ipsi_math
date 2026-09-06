---
id: DIF-J19
unit: 05-미분
topic: 접선의 방정식
level: 3점
difficulty: 하
source: 2027-06모평 19번
exam: 2027-06모평
origin: 기출
core: "접점에서의 미분계수가 기울기다"
tags: [접선,미분계수,절편]
status: seed
added: 2026-09-06
answer: 9
---

## 문제

<p>곡선 <span class="m">y = x<sup>3</sup> − 5x<sup>2</sup> + 3x + 6</span> 위의 점 <span class="m">(1, 5)</span>에서의 접선의 <span class="m">y</span>절편을 구하시오.</p>

## 발상

접선은 <b>기울기 <span class='m'>f′(1)</span>, 지나는 점 <span class='m'>(1,5)</span></b>로 끝난다. <span class='m'>y</span>절편은 <span class='m'>x = 0</span>을 대입한 값.

## 풀이

<p><span class="step">① 접선을 만드는 데 필요한 두 조각을 확인한다.</span>
접선은 <b>지나는 점</b>과 <b>기울기</b>만 있으면 정해진다.
지나는 점은 문제가 준 <span class="m">(1, 5)</span>이고,
기울기는 <b>그 점에서의 미분계수</b>다.</p>

<p><span class="step">② 도함수를 구해 기울기를 계산한다.</span></p>
<p class="m">y = x<sup>3</sup> − 5x<sup>2</sup> + 3x + 6 → y′ = 3x<sup>2</sup> − 10x + 3</p>
<p><span class="m">x = 1</span>을 대입한다.</p>
<p class="m">y′(1) = 3 × 1 − 10 × 1 + 3 = 3 − 10 + 3 = −4</p>

<p><span class="step">③ 접선의 방정식을 세운다.</span>
기울기가 <span class="m">−4</span>이고 점 <span class="m">(1, 5)</span>를 지나므로</p>
<p class="m">y − 5 = −4(x − 1)</p>
<p>오른쪽을 전개하고 <span class="m">5</span>를 넘긴다.</p>
<p class="m">y = −4x + 4 + 5 = −4x + 9</p>

<p><span class="step">④ y절편을 읽는다.</span>
<span class="m">y</span>절편은 <span class="m">x = 0</span>일 때의 <span class="m">y</span>값이다.</p>
<p class="m">y = −4 × 0 + 9 = 9</p>
<p class="m">답 9</p>

## 노하우

<b>접선 = 기울기 f′(a) + 점 (a, f(a)).</b> 두 조각만 있으면 끝난다. <span class='m'>y = f′(a)(x−a) + f(a)</span> 형태로 두면 <span class='m'>y</span>절편은 <span class='m'>f(a) − a·f′(a)</span> = <span class='m'>5 − 1·(−4) = 9</span>로 바로 나온다.
