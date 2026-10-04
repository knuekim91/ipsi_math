---
id: PRB-W02-V4
parent: PRB-W02
unit: 07-경우의수확률
topic: 순서가 정해진 나열과 조건부확률
level: 4점
difficulty: 중상
source: 자체 개발 (PRB-W02 변형 · 조건부확률)
origin: 유사문항
core: "조건이 붙으면 표본공간이 원문항의 분자 8로 줄어든다. 그 8가지를 이미 두 묶음으로 나눠 두었으므로 다시 셀 것이 없다"
tags: [조건부확률,순열,같은것이있는순열,순서가정해진나열]
status: variant
added: 2026-10-04
answer: ③
---

## 문제

<p>주머니에 <span class="m">1, 1, 2, 3, 4</span>의 숫자가 하나씩 적혀 있는
<span class="m">5</span>개의 공이 들어 있다.
이 주머니에서 임의로 <span class="m">4</span>개의 공을 동시에 꺼내어
임의로 일렬로 나열하고, 나열된 순서대로 공에 적혀 있는 수를
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>라 하자.
<span class="m">a ≤ b ≤ c ≤ d</span>일 때,
네 수 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>가 모두 다를 확률은?</p>

<div class="choices"><span>① 1/8</span><span>② 1/6</span><span>③ 1/4</span>
<span>④ 3/8</span><span>⑤ 1/2</span></div>

## 발상

<b>조건부확률이지만 새로 셀 것이 거의 없다.</b>
사건을 이렇게 둔다.</p>
<p class="m">A : a ≤ b ≤ c ≤ d</p>
<p class="m">B : 네 수가 모두 다르다</p>
<p>구하는 것은 <span class="m">P(B | A)</span>이고,</p>
<p class="m">P(B | A) = P(A ∩ B) / P(A)</p>
<p>이다. <b>분모 <span class="m">P(A)</span>는 원문항에서 이미 구한 값</b>이다.<br><br>

<b>더 중요한 것은, 원문항에서 경우를 나눈 방식이 그대로 분자가 된다는 점이다.</b>
원문항에서는 남기는 공이 <span class="m">1</span>이 적힌 공인지 아닌지로 갈랐는데,
<b><span class="m">1</span>이 적힌 공을 남긴 쪽이 바로 &lsquo;네 수가 모두 다른&rsquo; 경우</b>다.
표를 다시 읽기만 하면 된다.<br><br>

<b>조건이 붙으면 표본공간이 바뀐다.</b>
전체 <span class="m">120</span>이 아니라,
조건을 만족하는 <span class="m">8</span>가지가 새로운 전체가 된다.

## 풀이

<p><span class="step">① 공을 구별해 적는다.</span></p>
<p class="m">1<sub>①</sub>, 1<sub>②</sub>, 2, 3, 4</p>

<p><span class="step">② 조건 A의 경우의 수를 센다.</span>
남기는 공 하나로 경우를 나눈다.<br>
<span class="m">1</span>이 적힌 공 하나를 남기면 꺼낸 수가
<span class="m">1, 2, 3, 4</span>로 모두 다르고, 나열은 한 가지다.</p>
<p class="m">2 × 1 = 2</p>
<p><span class="m">2, 3, 4</span> 중 하나를 남기면 꺼낸 수가
<span class="m">1, 1, x, y</span>이고,
<span class="m">1</span>이 적힌 두 공이 자리를 바꾸는 두 가지가 있다.</p>
<p class="m">3 × 2 = 6</p>
<p class="m">(A의 경우의 수) = 2 + 6 = 8</p>

<p><span class="step">③ A와 B가 함께 일어나는 경우를 센다.</span>
위의 두 묶음 중 네 수가 모두 다른 것은 <b>앞쪽</b>뿐이다.
뒤쪽은 <span class="m">1</span>이 두 개라 같은 수가 있다.</p>
<p class="m">(A ∩ B의 경우의 수) = 2</p>

<p><span class="step">④ 조건부확률을 구한다.</span>
두 확률의 분모가 모두 <span class="m">120</span>으로 같으므로
<b>가짓수의 비가 곧 답</b>이다.</p>
<p class="m">P(B | A) = (2/120) / (8/120) = 2/8 = 1/4</p>
<p class="m">답 ③</p>

## 함정

<b>분모를 <span class="m">120</span>으로 두면 안 된다.</b>
조건이 &lsquo;<span class="m">a ≤ b ≤ c ≤ d</span>일 때&rsquo;이므로
<b>표본공간이 그 <span class="m">8</span>가지로 줄어든 것</b>이다.
<span class="m">2/120 = 1/60</span>은 조건부확률이 아니라
<span class="m">P(A ∩ B)</span>다.<br><br>

<b>분자에서도 공을 구별해 세야 한다.</b>
네 수가 모두 다른 경우는 &lsquo;<span class="m">1</span>이 적힌 공 중
어느 것을 남기느냐&rsquo;로 <span class="m">2</span>가지다.
<span class="m">1</span>가지로 세면 <span class="m">1/8</span>이 되어 ①을 고르게 된다.
<b>원문항과 똑같은 함정이 조건부확률의 분자에서 한 번 더 나온다.</b><br><br>

<b>조건과 사건의 자리를 바꾸면 안 된다.</b>
<span class="m">P(A | B)</span>를 구하면 <span class="m">2/2 = 1</span>이 된다.
네 수가 모두 다르면서 오름차순일 조건부확률이 아니라,
<b>오름차순일 때 모두 다를 확률</b>을 묻고 있다.

## 노하우

<b>조건부확률은 표본공간을 갈아 끼우는 것이다.</b>
&lsquo;<span class="m">~</span>일 때&rsquo; 뒤에 오는 것이 새로운 전체집합이 된다.
이 문제에서는 <span class="m">120</span>이 아니라
<span class="m">8</span>이 전체가 된다.
<b>조건을 먼저 찾아 동그라미를 치고 시작한다.</b><br><br>

<b>앞에서 나눈 경우가 그대로 분자가 되게 나눠 둔다.</b>
원문항에서 &lsquo;<span class="m">1</span>이 몇 개 뽑혔는가&rsquo;로 경우를 갈라 두었기 때문에
이 문제는 <b>그 표를 다시 읽는 것만으로</b> 끝난다.
경우를 나눌 때 <b>나중에 조건이 될 만한 기준</b>을 고르는 습관이
이런 곳에서 시간을 벌어 준다.<br><br>

<b>분모가 같으면 가짓수의 비로 바로 계산한다.</b>
<span class="m">P(A ∩ B)</span>와 <span class="m">P(A)</span>가
같은 표본공간에서 나왔으므로 통분할 필요 없이
<span class="m">2 : 8</span>을 그대로 쓰면 된다.
