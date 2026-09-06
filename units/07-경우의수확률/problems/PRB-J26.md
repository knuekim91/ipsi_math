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

<p><span class="step">① 조건을 다시 읽는다.</span>
네 수의 <b>곱</b>이 <span class="m">5</span>의 배수가 되려면
곱 안에 <b>인수 <span class="m">5</span>가 적어도 하나</b> 있어야 한다.
<span class="m">1</span>부터 <span class="m">10</span>까지 중에서 <span class="m">5</span>를 인수로 갖는 수는
<span class="m">5</span>와 <span class="m">10</span> 둘뿐이다.
그러므로 조건은 다음과 같이 바뀐다.</p>
<p class="m">5 또는 10 중 적어도 하나를 뽑는다</p>

<p><span class="step">② &lsquo;적어도 하나&rsquo;는 여사건으로 센다.</span>
&lsquo;적어도 하나&rsquo;를 직접 세면 한 개인 경우와 두 개인 경우로 나눠야 해서 번거롭다.
반대로 <b>하나도 안 뽑는 경우</b>는 한 번에 세어진다.</p>

<p><span class="step">③ 전체 경우의 수를 구한다.</span>
<span class="m">10</span>개에서 <span class="m">4</span>개를 <b>동시에</b> 꺼내므로 순서를 따지지 않는다.</p>
<p class="m"><sub>10</sub>C<sub>4</sub> = (10 × 9 × 8 × 7)/(4 × 3 × 2 × 1) = 210</p>

<p><span class="step">④ 여사건의 경우의 수를 구한다.</span>
<span class="m">5</span>와 <span class="m">10</span>을 빼면 남는 것은 <span class="m">8</span>개다.
그중에서 <span class="m">4</span>개를 고른다.</p>
<p class="m"><sub>8</sub>C<sub>4</sub> = (8 × 7 × 6 × 5)/(4 × 3 × 2 × 1) = 70</p>
<p class="m">P(여사건) = 70/210 = 1/3</p>

<p><span class="step">⑤ 여사건에서 되돌린다.</span></p>
<p class="m">P(구하는 사건) = 1 − 1/3 = 2/3</p>
<p class="m">답 ⑤</p>

## 노하우

<b>&lsquo;곱이 어떤 수의 배수&rsquo;는 소인수 하나에 집중한다.</b> 5의 배수라면 인수 5가 하나만 있으면 되고, 그러려면 5나 10이 뽑히기만 하면 된다. 그리고 <b>&lsquo;적어도 하나&rsquo;는 거의 항상 여사건</b>이다.
