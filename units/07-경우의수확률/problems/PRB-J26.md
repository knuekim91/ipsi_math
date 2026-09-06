---
id: PRB-J26
unit: 07-경우의수확률
topic: 여사건의 확률
level: 3점
difficulty: 중
source: 2027-06모평 26번
exam: 2027-06모평
origin: 기출
core: "5의 배수가 되려면 5나 10 중 하나는 뽑혀야 하므로 여사건이 훨씬 쉽다"
tags: [여사건,조합,배수]
status: seed
added: 2026-09-06
answer: ⑤
---

## 문제

<p>1부터 10까지의 자연수가 하나씩 적힌 10개의 공이 들어 있는 주머니에서 임의로 4개의 공을 동시에 꺼낼 때, 꺼낸 공에 적힌 네 수의 곱이 5의 배수일 확률은?</p><div class="choices"><span>① 1/2</span><span>② 5/9</span><span>③ 7/12</span><span>④ 5/8</span><span>⑤ 2/3</span></div>

## 발상

<b>곱이 5의 배수 ⟺ 뽑은 수 중에 5의 배수가 적어도 하나 있다.</b> &lsquo;적어도 하나&rsquo;는 여사건이 훨씬 짧다 — 5의 배수(5, 10)를 <b>하나도 안 뽑는</b> 경우.

## 풀이

<p><span class="step">① 전체.</span> <span class="m"><sub>10</sub>C<sub>4</sub> = 210</span></p><p><span class="step">② 여사건.</span> 5의 배수는 <span class="m">5, 10</span> 두 개. 이 둘을 빼고 나머지 8개에서 4개를 고른다.</p><p class="m"><sub>8</sub>C<sub>4</sub> = 70</p><p class="m">P(여사건) = 70/210 = 1/3</p><p><span class="step">③</span></p><p class="m">1 − 1/3 = 2/3</p>

## 노하우

<b>&lsquo;곱이 어떤 수의 배수&rsquo;는 소인수 하나에 집중한다.</b> 5의 배수라면 인수 5가 하나만 있으면 되고, 그러려면 5나 10이 뽑히기만 하면 된다. 그리고 <b>&lsquo;적어도 하나&rsquo;는 거의 항상 여사건</b>이다.
