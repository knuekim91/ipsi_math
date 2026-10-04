---
id: PRB-W02-V3
parent: PRB-W02
unit: 07-경우의수확률
topic: 순서가 정해진 나열과 같은 수가 적힌 공
level: 4점
difficulty: 중
source: 자체 개발 (PRB-W02 변형 · 부등호에서 등호를 뺀 경우)
origin: 유사문항
core: "a<b<c<d는 네 수가 모두 달라야 한다는 뜻이므로, 같은 수가 적힌 두 공이 함께 뽑히면 아예 불가능하다"
tags: [확률,순열,같은것이있는순열,순서가정해진나열]
status: variant
added: 2026-10-04
answer: ②
---

## 문제

<p>주머니에 <span class="m">1, 1, 2, 3, 4</span>의 숫자가 하나씩 적혀 있는
<span class="m">5</span>개의 공이 들어 있다.
이 주머니에서 임의로 <span class="m">4</span>개의 공을 동시에 꺼내어
임의로 일렬로 나열하고, 나열된 순서대로 공에 적혀 있는 수를
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>라 할 때,
<span class="m">a &lt; b &lt; c &lt; d</span>일 확률은?</p>

<div class="choices"><span>① 1/120</span><span>② 1/60</span><span>③ 1/30</span>
<span>④ 1/20</span><span>⑤ 1/15</span></div>

## 발상

<b>원문항과 공은 똑같고 부등호에서 등호만 빠졌다.
그런데 이 한 글자가 경우를 거의 다 지운다.</b><br><br>

<span class="m">a &lt; b &lt; c &lt; d</span>는 <b>네 수가 모두 달라야</b> 한다는 뜻이다.
그런데 <span class="m">1</span>이 적힌 공이 두 개 있으므로,
<b>그 둘이 함께 뽑히면 어떻게 나열해도
<span class="m">1</span>과 <span class="m">1</span>이 이웃하여
등호가 생긴다.</b> 조건을 만족시킬 수 없다.<br><br>

따라서 <span class="m">1</span>이 적힌 공 중 <b>하나만</b> 뽑혀야 한다.
다섯 개 중 넷을 꺼내므로, 이는
<b>남기는 공이 반드시 <span class="m">1</span>이 적힌 공이어야 한다</b>는 뜻이다.
가능한 경우가 단 둘로 줄어든다.

## 풀이

<p><span class="step">① 공을 구별해 적고 전체를 센다.</span></p>
<p class="m">1<sub>①</sub>, 1<sub>②</sub>, 2, 3, 4</p>
<p class="m">(전체) = <sub>5</sub>P<sub>4</sub> = 120</p>

<p><span class="step">② 불가능한 경우를 먼저 잘라 낸다.</span>
<span class="m">1</span>이 적힌 두 공이 모두 뽑히면
<span class="m">a, b, c, d</span> 중 두 수가 <span class="m">1</span>로 같아진다.
<span class="m">a &lt; b &lt; c &lt; d</span>에는 등호가 없으므로
이 경우는 <b>어떤 나열로도 조건을 만족시킬 수 없다.</b><br>
그러므로 남기는 공은 <span class="m">1</span>이 적힌 두 공 중 하나여야 한다.</p>
<p class="m">(남기는 방법) = 2</p>

<p><span class="step">③ 각 경우의 나열을 센다.</span>
이때 꺼낸 수는 <span class="m">1, 2, 3, 4</span>로 모두 다르다.
작은 것부터 놓는 방법은 <b>하나뿐</b>이고,
같은 수가 없으니 자리를 바꿀 여지도 없다.</p>
<p class="m">2 × 1 = 2</p>

<p><span class="step">④ 확률을 구한다.</span></p>
<p class="m">2/120 = 1/60</p>
<p class="m">답 ②</p>

## 함정

<b>등호가 빠진 것을 놓치면 원문항의 답 <span class="m">1/15</span>를 그대로 쓴다.</b>
<span class="m">≤</span>와 <span class="m">&lt;</span>는 전혀 다른 조건이다.
<span class="m">≤</span>는 같아도 되지만 <span class="m">&lt;</span>는 <b>같으면 안 된다.</b>
답이 <span class="m">8</span>배 차이 난다.<br><br>

<b>&lsquo;네 수가 모두 다르다&rsquo;로 바꿔 읽어야 한다.</b>
<span class="m">a &lt; b &lt; c &lt; d</span>를 그대로 들여다보면 막막하지만,
<b>&lsquo;같은 수가 있으면 안 된다&rsquo;</b>로 번역하면
어떤 공을 뽑아야 하는지가 바로 보인다.<br><br>

<b><span class="m">1</span>이 적힌 공을 남기는 방법이
<span class="m">2</span>가지임을 잊지 않는다.</b>
두 공은 서로 다른 공이므로 어느 쪽을 남기느냐가 구별된다.
<span class="m">1</span>가지로 세면 <span class="m">1/120</span>이 되어 ①을 고르게 된다.

## 노하우

<b>부등호에 등호가 있는지부터 확인한다.</b>
<span class="m">≤</span>이면 같은 수가 있어도 되고,
<span class="m">&lt;</span>이면 같은 수가 있으면 안 된다.
같은 것이 섞인 문제에서는 <b>이 한 글자가 답을 몇 배씩 바꾼다.</b>
문제를 읽을 때 부등호에 동그라미를 쳐 두는 습관이 좋다.<br><br>

<b>조건을 &lsquo;무엇이 불가능한가&rsquo;로 뒤집어 읽는다.</b>
가능한 경우를 세려 하기 전에 <b>아예 안 되는 경우</b>를 먼저 잘라 내면
남는 것이 몇 개 안 될 때가 많다.
이 문제는 그렇게 해서 경우가 둘로 줄었다.<br><br>

<b>모두 다른 <span class="m">4</span>개를 오름차순으로 놓을 확률은
<span class="m">1/4! = 1/24</span>이다.</b>
이 문제의 답 <span class="m">1/60</span>은 그보다 작은데,
<b>애초에 모두 다른 공이 뽑힐 확률</b>
<span class="m">(2/5)</span>이 곱해졌기 때문이다.</p>
<p class="m">(2/5) × (1/24) = 1/60</p>
<p>이렇게 두 단계로 쪼개어 검산할 수도 있다.
