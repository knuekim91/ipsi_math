---
id: DIF-J05
unit: 05-미분
topic: 곱의 미분법
level: 3점
difficulty: 하
source: 2027-06모평 5번
exam: 2027-06모평
origin: 기출
core: "곱은 전개하지 말고 곱의 미분법으로"
tags: [곱의미분법,도함수]
status: seed
added: 2026-09-06
answer: ①
---

## 문제

<p class="m">함수 f(x) = (3x − 1)(x<sup>2</sup> − 2x + 2)에 대하여 f′(2)의 값은?</p><div class="choices"><span>① 16</span><span>② 18</span><span>③ 20</span><span>④ 22</span><span>⑤ 24</span></div>

## 발상

전개하면 삼차식이 되어 계산이 길어진다. <b>곱의 미분법을 쓰면 2를 바로 대입</b>할 수 있다.

## 풀이

<p><span class="step">① 전개하지 않기로 정한다.</span>
<span class="m">f(x) = (3x − 1)(x<sup>2</sup> − 2x + 2)</span>를 전개하면 삼차식이 되고
그것을 다시 미분해야 하므로 계산이 길어진다.
<b>구하는 것이 한 점에서의 값 <span class="m">f′(2)</span> 하나뿐</b>이므로
곱의 미분법을 쓰고 곧바로 <span class="m">2</span>를 넣는 편이 짧다.</p>

<p><span class="step">② 곱의 미분법을 적용한다.</span>
두 함수의 곱을 미분하는 규칙은 다음과 같다.</p>
<p class="m">(fg)′ = f′g + fg′</p>
<p>앞의 인수 <span class="m">3x − 1</span>을 미분하면 <span class="m">3</span>,
뒤의 인수 <span class="m">x<sup>2</sup> − 2x + 2</span>를 미분하면 <span class="m">2x − 2</span>이다.</p>
<p class="m">f′(x) = 3(x<sup>2</sup> − 2x + 2) + (3x − 1)(2x − 2)</p>

<p><span class="step">③ x = 2를 대입한다.</span>
<b>전개하지 말고 괄호마다 값을 넣는다.</b></p>
<p class="m">첫째 항 : 3(2<sup>2</sup> − 2 × 2 + 2) = 3(4 − 4 + 2) = 3 × 2 = 6</p>
<p class="m">둘째 항 : (3 × 2 − 1)(2 × 2 − 2) = 5 × 2 = 10</p>
<p class="m">f′(2) = 6 + 10 = 16</p>
<p class="m">답 ①</p>

## 노하우

<b>(fg)′ = f′g + fg′.</b> 한 점에서의 값만 물으면 전개는 손해다. 대입할 수 있는 형태로 두고 값을 넣는다.
