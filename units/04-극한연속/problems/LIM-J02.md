---
id: LIM-J02
unit: 04-극한연속
topic: 미분계수의 정의
level: 2점
difficulty: 하
source: 2027-06모평 2번
exam: 2027-06모평
origin: 기출
core: "(f(x)−f(a))/(x−a) 는 계산하지 말고 f′(a)로 읽는다"
tags: [미분계수,극한]
status: seed
added: 2026-09-06
answer: ⑤
---

## 문제

<p class="m">함수 f(x) = 3x<sup>2</sup> − x + 1에 대하여 lim<sub>x→1</sub> (f(x) − f(1))/(x − 1)의 값은?</p><div class="choices"><span>① 1</span><span>② 2</span><span>③ 3</span><span>④ 4</span><span>⑤ 5</span></div>

## 발상

이 꼴은 계산하는 극한이 아니라 <b>기호를 바꿔 읽는 극한</b>이다. 곧바로 <span class='m'>f′(1)</span>.

## 풀이

<p><span class="step">① 주어진 식이 무엇인지 알아본다.</span>
구하라고 한 것은 <span class="m">lim<sub>x→1</sub> (f(x) − f(1))/(x − 1)</span>이다.
이것은 미분계수의 정의</p>
<p class="m">f′(a) = lim<sub>x→a</sub> (f(x) − f(a))/(x − a)</p>
<p>에서 <span class="m">a = 1</span>인 경우와 똑같다.
그러므로 <b>이 극한의 값은 <span class="m">f′(1)</span>이다.</b>
분자를 전개해서 약분하려 하면 시간만 잃는다.</p>

<p><span class="step">② 도함수를 구한다.</span>
<span class="m">f(x) = 3x<sup>2</sup> − x + 1</span>을 항별로 미분한다.</p>
<p class="m">f′(x) = 3 × 2x − 1 + 0 = 6x − 1</p>

<p><span class="step">③ x = 1을 대입한다.</span></p>
<p class="m">f′(1) = 6 × 1 − 1 = 5</p>
<p class="m">답 ⑤</p>

## 노하우

<b>(f(x)−f(a))/(x−a) 를 보면 즉시 f′(a).</b> 분모를 없애려고 전개하기 시작하면 시간을 잃는다.
