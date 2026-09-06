---
id: SEQ-J03
unit: 03-수열
topic: 시그마의 성질
level: 3점
difficulty: 하
source: 2027-06모평 3번
exam: 2027-06모평
origin: 기출
core: "두 식을 빼면 구하는 것만 남는다"
tags: [시그마,연립]
status: seed
added: 2026-09-06
answer: ④
---

## 문제

<p>두 수열 <span class="m">{a<sub>n</sub>}</span>, <span class="m">{b<sub>n</sub>}</span>에 대하여</p><span class="cond m">Σ<sub>k=1</sub><sup>5</sup>(2a<sub>k</sub> + b<sub>k</sub>) = 19, &nbsp; Σ<sub>k=1</sub><sup>5</sup>(a<sub>k</sub> + b<sub>k</sub>) = 10</span><p>일 때, <span class="m">Σ<sub>k=1</sub><sup>5</sup> a<sub>k</sub></span>의 값은?</p><div class="choices"><span>① 6</span><span>② 7</span><span>③ 8</span><span>④ 9</span><span>⑤ 10</span></div>

## 발상

<b>두 식을 빼면 <span class='m'>Σb</span>가 통째로 지워진다.</b> 각각을 구할 필요가 없다.

## 풀이

<p><span class="step">① 두 수열을 각각 구하려 하지 않는다.</span>
구하는 것은 <span class="m">Σa<sub>k</sub></span> 하나뿐이고,
주어진 두 식에는 <span class="m">Σa<sub>k</sub></span>와 <span class="m">Σb<sub>k</sub></span>가 섞여 있다.
<b>두 식을 빼면 <span class="m">Σb<sub>k</sub></span>가 통째로 지워진다.</b></p>

<p><span class="step">② 시그마를 항별로 나눈다.</span>
시그마는 덧셈에 대해 나눠 쓸 수 있고, 상수배는 밖으로 나온다.</p>
<p class="m">Σ(2a<sub>k</sub> + b<sub>k</sub>) = 2Σa<sub>k</sub> + Σb<sub>k</sub> = 19</p>
<p class="m">Σ(a<sub>k</sub> + b<sub>k</sub>) = Σa<sub>k</sub> + Σb<sub>k</sub> = 10</p>

<p><span class="step">③ 위 식에서 아래 식을 뺀다.</span>
<span class="m">Σb<sub>k</sub></span>가 양쪽에 똑같이 있으므로 빼면 사라진다.</p>
<p class="m">(2Σa<sub>k</sub> + Σb<sub>k</sub>) − (Σa<sub>k</sub> + Σb<sub>k</sub>) = 19 − 10</p>
<p class="m">Σa<sub>k</sub> = 9</p>
<p class="m">답 ④</p>

## 노하우

<b>시그마는 항끼리 더하고 뺄 수 있다.</b> 두 식이 주어지면 먼저 <b>빼서 무엇이 지워지는지</b> 본다.
