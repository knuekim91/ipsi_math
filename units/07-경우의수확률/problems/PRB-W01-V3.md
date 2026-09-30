---
id: PRB-W01-V3
parent: PRB-W01
unit: 07-경우의수확률
topic: 동전 뒤집기 시행과 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W01 변형 · 조건부확률)
origin: 유사문항
core: "분모는 원래 문항의 답 그대로이고, 분자는 '짝수 눈 3번'인 경우 하나만 세면 된다"
tags: [조건부확률,시행,홀짝,패리티]
status: variant
added: 2026-09-30
answer: ②
---

## 문제

<p>탁자 위에 <span class="m">6</span>개의 동전이 일렬로 놓여 있다.
<span class="m">1</span>번째, <span class="m">2</span>번째,
<span class="m">3</span>번째 자리의 동전은 뒷면이 보이도록 놓여 있고,
나머지 <span class="m">3</span>개의 동전은 앞면이 보이도록 놓여 있다.
이 <span class="m">6</span>개의 동전과 한 개의 주사위를 사용하여
다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">주사위를 한 번 던져 나온 눈의 수가 k일 때,</span>
<span class="cond m">k가 홀수이면 k번째 자리의 동전과 k+1번째 자리의 동전을 한 번씩 뒤집어 제자리에 놓고,</span>
<span class="cond m">k가 짝수이면 임의로 하나의 동전을 선택하여 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>이 시행을 <span class="m">3</span>번 반복한 후 이
<span class="m">6</span>개의 동전이 모두 같은 면이 보이도록 놓여 있었을 때,
<span class="m">3</span>번의 시행에서 나온 주사위의 눈의 수가
모두 짝수였을 확률은?</p>

<div class="choices"><span>① 1/6</span><span>② 1/5</span><span>③ 7/30</span>
<span>④ 4/15</span><span>⑤ 3/10</span></div>

## 발상

<b>조건부확률은 분모와 분자를 각각 구하는 문제다.
그런데 이 문제는 <b>분모가 이미 알려진 값</b>이다.</b></p>
<p class="m">P(B | A) = P(A ∩ B) / P(A)</p>
<p>여기서 <span class="m">A</span>는 &lsquo;모두 같은 면&rsquo;,
<span class="m">B</span>는 &lsquo;세 눈이 모두 짝수&rsquo;이다.
<span class="m">P(A)</span>는 원래 문항에서 구한
<span class="m">5/144</span>를 그대로 쓴다.<br><br>

<b>분자는 원래 풀이의 &lsquo;경우 1&rsquo; 그 자체다.</b>
뒷면의 개수가 <span class="m">3</span>(홀수)에서 짝수로 가려면
짝수 눈이 홀수 번 나와야 하므로
<span class="m">1</span>번 또는 <span class="m">3</span>번이었다.
<b>&lsquo;모두 짝수&rsquo;는 그중 <span class="m">3</span>번인 경우</b>이므로,
이미 세어 둔 <span class="m">1/144</span>를 그대로 가져오면 된다.<br><br>

<b>그러므로 이 문제는 새로 셀 것이 거의 없다.</b>
조건부확률 문제가 늘 무거운 것은 아니고,
<b>앞에서 나눈 경우가 그대로 분자가 되는</b> 구조를 알아보는 것이 핵심이다.

## 풀이

<p><span class="step">① 두 사건을 정한다.</span></p>
<p class="m">A : 3번의 시행 후 6개의 동전이 모두 같은 면이다</p>
<p class="m">B : 3번의 시행에서 나온 눈의 수가 모두 짝수이다</p>
<p>구하는 것은 <span class="m">P(B | A)</span>이다.</p>

<p><span class="step">② 분모 P(A)를 구한다.</span>
<span class="m">n</span>번째 자리의 동전을 <span class="m">c<sub>n</sub></span>이라 하자.
홀수 눈은 동전 두 개를 뒤집어 뒷면 개수의 홀짝을 그대로 두고,
짝수 눈은 한 개를 뒤집어 홀짝을 바꾼다.
처음 뒷면이 <span class="m">3</span>개(홀수)이고 목표는 짝수이므로
<b>짝수 눈이 홀수 번</b>, 곧 <span class="m">1</span>번 또는
<span class="m">3</span>번 나와야 한다.</p>
<p class="m">(짝수 눈 3번) = 1/144, &nbsp; (짝수 눈 1번) = 1/36</p>
<p class="m">P(A) = 1/144 + 4/144 = 5/144</p>

<p><span class="step">③ 분자 P(A ∩ B)를 구한다.</span>
<span class="m">B</span>는 세 번 모두 짝수 눈이라는 뜻이므로,
<span class="m">A ∩ B</span>는 위에서 이미 센 <b>짝수 눈 3번인 경우</b>다.
세 번 모두 임의의 동전 한 개씩을 뒤집으므로 모두 세 개가 뒤집힌다.
모두 앞면이 되려면
<span class="m">c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub></span>을
각각 한 번씩 뒤집어야 하고 그 순서가 <span class="m">3! = 6</span>가지,
모두 뒷면이 되려면
<span class="m">c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub></span>을
각각 한 번씩 뒤집어야 하므로 역시 <span class="m">6</span>가지다.
한 번의 시행에서 짝수 눈이 나오고 특정한 동전을 고를 확률은
<span class="m">(3/6) × (1/6) = 1/12</span>이다.</p>
<p class="m">P(A ∩ B) = 12 × (1/12)<sup>3</sup> = 12/1728 = 1/144</p>

<p><span class="step">④ 조건부확률을 계산한다.</span></p>
<p class="m">P(B | A) = P(A ∩ B) / P(A) = (1/144) / (5/144)</p>
<p>분모가 같으므로 <span class="m">144</span>가 그대로 지워진다.</p>
<p class="m">= 1/5</p>
<p class="m">답 ②</p>

## 함정

<b>조건부확률의 분모를 <span class="m">P(B)</span>로 두면 안 된다.</b>
&lsquo;모두 같은 면이었을 때&rsquo;가 조건이므로
<b>주어진 사건이 <span class="m">A</span></b>이고 분모는
<span class="m">P(A)</span>다.
<span class="m">P(A | B)</span>를 구하면
<span class="m">(1/144) / (1/8) = 1/18</span>이 되어 전혀 다른 값이 된다.<br><br>

<b>분자를 처음부터 다시 세느라 시간을 쓰지 않는다.</b>
<span class="m">P(A)</span>를 구할 때 이미 짝수 눈의 횟수로 경우를 갈랐으므로,
<b>그중 한 경우가 그대로 분자</b>다.
경우를 나눌 때 <b>나중에 조건이 될 만한 기준으로 나누어 두면</b>
이런 문제가 계산 없이 풀린다.<br><br>

<b>분모의 <span class="m">144</span>가 지워지는 것을 보고 계산을 줄인다.</b>
두 확률의 분모가 같으면 <b>분자끼리의 비</b>가 곧 답이다.
<span class="m">1 : 5</span>이므로 <span class="m">1/5</span>이다.

## 노하우

<b>경우를 나눌 때는 &lsquo;무엇으로 나눌지&rsquo;를 고른다.</b>
이 계열의 문제에서는 <b>짝수 눈이 몇 번 나왔는가</b>가
가장 좋은 기준이다.
홀짝 조건이 경우를 줄여 주고, 조건부확률을 물어도 그대로 재활용된다.<br><br>

<b>조건부확률은 분모를 먼저 확인한다.</b>
&lsquo;<span class="m">~</span>이었을 때&rsquo;, &lsquo;<span class="m">~</span>인 조건에서&rsquo;
뒤에 오는 것이 분모다.
이 문제에서는 &lsquo;모두 같은 면이 보이도록 놓여 있었을 때&rsquo;가 조건이므로
<b>분모가 <span class="m">P(모두 같은 면)</span></b>이다.<br><br>

<b>확률의 비로 생각하면 계산이 가벼워진다.</b>
같은 표본공간에서 <b>경우의 가짓수의 비</b>를 그대로 쓰면
분모를 통분할 필요가 없다.
여기서는 <span class="m">1/144</span>와 <span class="m">5/144</span>이므로
<span class="m">1 : 5</span>가 바로 보인다.
