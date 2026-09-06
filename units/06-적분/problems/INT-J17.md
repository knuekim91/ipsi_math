---
id: INT-J17
unit: 06-적분
topic: 부정적분과 초기조건
level: 3점
difficulty: 하
source: 2027-06모평 17번
exam: 2027-06모평
origin: 기출
core: "f′을 적분한 뒤 f(0)으로 적분상수를 정한다"
tags: [부정적분,적분상수]
status: seed
added: 2026-09-06
answer: 10
---

## 문제

<p class="m">다항함수 f(x)가 f′(x) = 6x<sup>2</sup> + 5, f(0) = 3을 만족시킬 때, f(1)의 값을 구하시오.</p>

## 발상

<b>적분하면 상수가 하나 남고, <span class='m'>f(0) = 3</span>이 그것을 정해 준다.</b>

## 풀이

<p><span class="step">① 도함수를 적분한다.</span>
<span class="m">f′(x)</span>가 주어졌으므로 적분하면 <span class="m">f(x)</span>가 나온다.
<b>적분하면 상수 하나가 반드시 따라붙는다.</b>
도함수가 같은 함수는 세로로 평행이동한 것들이 모두 해당되기 때문이다.
그 상수를 <span class="m">C</span>라 하자.</p>
<p class="m">f(x) = ∫(6x<sup>2</sup> + 5)dx = 6 × x<sup>3</sup>/3 + 5x + C = 2x<sup>3</sup> + 5x + C</p>

<p><span class="step">② 초기조건으로 상수를 잡는다.</span>
문제가 <span class="m">f(0) = 3</span>을 준 이유가 이 <span class="m">C</span>를 정하기 위해서다.
<span class="m">x = 0</span>을 넣으면 <span class="m">x</span>가 든 항이 모두 사라진다.</p>
<p class="m">f(0) = 0 + 0 + C = C = 3</p>
<p class="m">f(x) = 2x<sup>3</sup> + 5x + 3</p>

<p><span class="step">③ 구하는 값을 대입한다.</span></p>
<p class="m">f(1) = 2 × 1 + 5 × 1 + 3 = 2 + 5 + 3 = 10</p>
<p class="m">답 10</p>

## 노하우

<b>도함수만으로는 함수가 하나로 정해지지 않는다.</b> 세로로 평행이동한 함수들이 전부 같은 도함수를 갖기 때문. 그래서 <b>초기조건이 반드시 하나 딸려 온다</b> — 그것을 먼저 찾아 놓고 적분한다.
