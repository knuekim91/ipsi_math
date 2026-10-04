---
id: PRB-W02-V1
parent: PRB-W02
unit: 07-경우의수확률
topic: 순서가 정해진 나열과 같은 수가 적힌 공
level: 4점
difficulty: 중상
source: 자체 개발 (PRB-W02 변형 · 같은 수가 두 쌍)
origin: 유사문항
core: "같은 수가 적힌 공이 두 쌍이면 쌍마다 2가지씩 생기고, 두 쌍이 모두 뽑히면 더하지 않고 곱해 4가지가 된다"
tags: [확률,순열,같은것이있는순열,순서가정해진나열]
status: variant
added: 2026-10-04
answer: ③
---

## 문제

<p>주머니에 <span class="m">1, 1, 2, 2, 3</span>의 숫자가 하나씩 적혀 있는
<span class="m">5</span>개의 공이 들어 있다.
이 주머니에서 임의로 <span class="m">4</span>개의 공을 동시에 꺼내어
임의로 일렬로 나열하고, 나열된 순서대로 공에 적혀 있는 수를
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>라 할 때,
<span class="m">a ≤ b ≤ c ≤ d</span>일 확률은?</p>

<div class="choices"><span>① 1/15</span><span>② 1/12</span><span>③ 1/10</span>
<span>④ 2/15</span><span>⑤ 1/6</span></div>

## 발상

<b>구조는 원문항과 같다. 달라진 것은 같은 수가 <b>두 쌍</b>이라는 점이다.</b>
<span class="m">1</span>이 둘, <span class="m">2</span>가 둘이다.<br><br>

여전히 <span class="m">a ≤ b ≤ c ≤ d</span>는 수의 나열을 하나로 묶고,
남는 자유는 <b>같은 수가 적힌 공끼리 자리를 바꾸는 것</b>뿐이다.
이번에는 그런 쌍이 두 개일 수 있으므로,
<b>두 쌍이 모두 뽑히면 <span class="m">2 × 2 = 4</span>가지</b>가 된다.
<b>더하는 것이 아니라 곱한다</b>는 것을 놓치면 안 된다.<br><br>

<b>남기는 공 하나로 경우를 나눈다.</b>
<span class="m">3</span>을 남기면 두 쌍이 모두 뽑히고,
<span class="m">1</span>이나 <span class="m">2</span>를 남기면 한 쌍만 온전히 남는다.

## 풀이

<p><span class="step">① 공을 구별해 적는다.</span>
수가 같아도 공은 서로 다른 공이다.</p>
<p class="m">1<sub>①</sub>, 1<sub>②</sub>, 2<sub>①</sub>, 2<sub>②</sub>, 3</p>

<p><span class="step">② 전체 경우의 수를 센다.</span>
<span class="m">5</span>개 중 <span class="m">4</span>개를 꺼내어 나열한다.</p>
<p class="m">(전체) = <sub>5</sub>P<sub>4</sub> = 120</p>

<p><span class="step">③ 1이 적힌 공 하나를 남기는 경우.</span>
남기는 방법이 <span class="m">2</span>가지다.
꺼낸 수는 <span class="m">1, 2, 2, 3</span>이므로 작은 것부터 놓으면
<span class="m">1, 2, 2, 3</span>이고,
<span class="m">2</span>가 적힌 두 공이 가운데 두 자리에서 자리를 바꾸는
<span class="m">2</span>가지가 있다.</p>
<p class="m">2 × 2 = 4</p>

<p><span class="step">④ 2가 적힌 공 하나를 남기는 경우.</span>
남기는 방법이 <span class="m">2</span>가지다.
꺼낸 수는 <span class="m">1, 1, 2, 3</span>이므로
<span class="m">1</span>이 적힌 두 공이 앞의 두 자리에서 자리를 바꾸는
<span class="m">2</span>가지가 있다.</p>
<p class="m">2 × 2 = 4</p>

<p><span class="step">⑤ 3을 남기는 경우.</span>
남기는 방법이 <span class="m">1</span>가지다.
꺼낸 수는 <span class="m">1, 1, 2, 2</span>이고,
<b>두 쌍이 각각 자리를 바꾸므로 그 가짓수를 곱한다.</b></p>
<p class="m">1 × (2 × 2) = 4</p>

<p><span class="step">⑥ 더해서 확률을 구한다.</span></p>
<p class="m">(조건을 만족) = 4 + 4 + 4 = 12</p>
<p class="m">12/120 = 1/10</p>
<p class="m">답 ③</p>

## 함정

<b>두 쌍이 모두 뽑힌 경우를 <span class="m">2 + 2 = 4</span>로 세면 안 된다.</b>
값은 우연히 같지만 이유가 틀렸다.
<span class="m">1</span>끼리 바꾸는 것과 <span class="m">2</span>끼리 바꾸는 것은
서로 영향을 주지 않으므로 <b>곱해야</b> 한다.
쌍이 셋이었다면 <span class="m">2<sup>3</sup> = 8</span>이지
<span class="m">6</span>이 아니다.<br><br>

<b>세 경우의 값이 모두 <span class="m">4</span>라고 대충 넘어가면 안 된다.</b>
앞의 둘은 <span class="m">(남기는 방법 2가지) × (쌍 하나 2가지)</span>이고,
마지막은 <span class="m">(남기는 방법 1가지) × (쌍 둘 4가지)</span>이다.
구조가 다르다.<br><br>

<b><span class="m">3</span>을 남기는 방법이 <span class="m">1</span>가지임을 확인한다.</b>
<span class="m">3</span>이 적힌 공은 하나뿐이다.
<span class="m">1</span>이나 <span class="m">2</span>처럼 둘이 아니다.

## 노하우

<b>같은 것이 여러 묶음이면 묶음마다의 가짓수를 곱한다.</b>
같은 수가 <span class="m">k</span>개 적힌 공이 모두 뽑히면
그 묶음에서 <span class="m">k!</span>가지가 생기고,
서로 다른 묶음끼리는 곱한다.
이 문제에서는 <span class="m">2! × 2! = 4</span>였다.<br><br>

<b>원문항과 답을 비교하면 구조가 보인다.</b>
원문항은 <span class="m">1/15</span>, 이 문항은 <span class="m">1/10</span>으로
<b>더 크다.</b>
같은 수가 많을수록 오름차순으로 놓이는 경우가 늘어나기 때문이다.
<b>답이 커지는 방향이 맞는지</b>로 검산할 수 있다.<br><br>

<b>&lsquo;남기는 공 하나&rsquo;로 나누면 경우가 다섯 개뿐이다.</b>
<span class="m">5</span>개 중 <span class="m">4</span>개를 꺼내는 문제는
언제나 버리는 하나를 기준으로 삼는 것이 가장 짧다.
