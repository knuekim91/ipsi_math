---
id: PRB-W02-V2
parent: PRB-W02
unit: 07-경우의수확률
topic: 순서가 정해진 나열과 같은 수가 적힌 공
level: 4점
difficulty: 중상
source: 자체 개발 (PRB-W02 변형 · 같은 수가 셋)
origin: 유사문항
core: "같은 수가 적힌 공 셋이 모두 뽑히면 그 세 공이 자리를 바꾸는 3! = 6가지가 생긴다. 개수가 아니라 계승이다"
tags: [확률,순열,같은것이있는순열,순서가정해진나열]
status: variant
added: 2026-10-04
answer: ③
---

## 문제

<p>주머니에 <span class="m">1, 1, 1, 2, 3</span>의 숫자가 하나씩 적혀 있는
<span class="m">5</span>개의 공이 들어 있다.
이 주머니에서 임의로 <span class="m">4</span>개의 공을 동시에 꺼내어
임의로 일렬로 나열하고, 나열된 순서대로 공에 적혀 있는 수를
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>라 할 때,
<span class="m">a ≤ b ≤ c ≤ d</span>일 확률은?</p>

<div class="choices"><span>① 1/10</span><span>② 1/8</span><span>③ 3/20</span>
<span>④ 1/5</span><span>⑤ 1/4</span></div>

## 발상

<b>이번에는 같은 수가 <b>세 개</b>다.</b>
<span class="m">1</span>이 적힌 공이 셋이므로, 이 셋이 모두 뽑히면
<b>세 공이 앞의 세 자리에서 자리를 바꾸는
<span class="m">3! = 6</span>가지</b>가 생긴다.
<span class="m">3</span>이 아니라 <span class="m">6</span>이라는 것이 핵심이다.<br><br>

<b>남기는 공 하나로 경우를 나눈다.</b>
<span class="m">1</span>이 적힌 공 하나를 남기면
<span class="m">1</span>이 둘만 뽑히고,
<span class="m">2</span>나 <span class="m">3</span>을 남기면
<span class="m">1</span>이 셋 모두 뽑힌다.
이 두 경우에서 생기는 가짓수가 <span class="m">2</span>와
<span class="m">6</span>으로 크게 다르다.

## 풀이

<p><span class="step">① 공을 구별해 적는다.</span></p>
<p class="m">1<sub>①</sub>, 1<sub>②</sub>, 1<sub>③</sub>, 2, 3</p>

<p><span class="step">② 전체 경우의 수를 센다.</span></p>
<p class="m">(전체) = <sub>5</sub>P<sub>4</sub> = 120</p>

<p><span class="step">③ 1이 적힌 공 하나를 남기는 경우.</span>
<span class="m">1</span>이 적힌 공이 셋이므로 남기는 방법이
<span class="m">3</span>가지다.
꺼낸 수는 <span class="m">1, 1, 2, 3</span>이고,
<span class="m">1</span>이 적힌 두 공이 앞의 두 자리에서 자리를 바꾸는
<span class="m">2! = 2</span>가지가 있다.</p>
<p class="m">3 × 2 = 6</p>

<p><span class="step">④ 2 또는 3을 남기는 경우.</span>
남기는 방법이 <span class="m">2</span>가지다.
꺼낸 수는 <span class="m">1, 1, 1, x</span>이고,
<span class="m">1</span>이 적힌 세 공이 앞의 세 자리에서 자리를 바꾸는
<span class="m">3! = 6</span>가지가 있다.</p>
<p class="m">2 × 6 = 12</p>

<p><span class="step">⑤ 더해서 확률을 구한다.</span></p>
<p class="m">(조건을 만족) = 6 + 12 = 18</p>
<p class="m">18/120 = 3/20</p>
<p class="m">답 ③</p>

## 함정

<b><span class="m">1</span>이 셋일 때를 <span class="m">3</span>가지로 세면 안 된다.</b>
세 공을 세 자리에 배열하는 것이므로
<span class="m">3! = 6</span>가지다.
<b>개수가 아니라 계승</b>이다.
같은 수가 <span class="m">k</span>개면 <span class="m">k!</span>가지다.<br><br>

<b>남기는 방법의 가짓수를 빠뜨리지 않는다.</b>
<span class="m">1</span>이 적힌 공 중 하나를 남기는 방법은
<span class="m">1</span>가지가 아니라 <span class="m">3</span>가지다.
세 공이 서로 다른 공이기 때문이다.<br><br>

<b><span class="m">2</span>와 <span class="m">3</span>을 남기는 경우를 묶어 센 것에 주의한다.</b>
둘 다 꺼낸 수가 <span class="m">1, 1, 1, x</span> 꼴이라 가짓수가 같아서
<span class="m">2</span>가지로 묶었다. 구조가 같을 때만 묶을 수 있다.

## 노하우

<b>같은 수가 <span class="m">k</span>개 모두 뽑히면 <span class="m">k!</span>가 곱해진다.</b>
<span class="m">k = 2</span>면 <span class="m">2</span>,
<span class="m">k = 3</span>이면 <span class="m">6</span>,
<span class="m">k = 4</span>면 <span class="m">24</span>로 빠르게 커진다.
같은 수가 많을수록 오름차순이 될 확률이 급격히 올라간다.<br><br>

<b>세 문항의 답을 늘어놓으면 흐름이 보인다.</b></p>
<p class="m">원문항 1/15 &lt; V1 1/10 &lt; V2 3/20</p>
<p>같은 수가 늘어날수록 커진다.
<b>답이 커지는 방향이 맞는지</b>가 가장 빠른 검산이다.<br><br>

<b>구조가 같은 경우끼리 묶어 센다.</b>
<span class="m">2</span>를 남기든 <span class="m">3</span>을 남기든
꺼낸 수의 모양이 <span class="m">1, 1, 1, x</span>로 같으므로 한꺼번에 센다.
<b>경우를 나눌 때는 &lsquo;가짓수가 달라지는 지점&rsquo;에서만</b> 가른다.
