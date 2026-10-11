---
id: PRB-W03-V3
parent: PRB-W03
unit: 07-경우의수확률
topic: 동전 뒤집기와 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W03 변형 · 동전을 3개로)
origin: 유사문항
core: "동전이 3개면 처음부터 앞면이 홀수이므로 홀짝 조건이 뒤집혀 1이 짝수 번 나와야 한다"
tags: [조건부확률,시행,홀짝,패리티,상태추적]
status: variant
added: 2026-10-11
answer: 16
---

## 문제

<p>탁자 위에 <span class="m">3</span>개의 동전이 모두 앞면이 보이도록
일렬로 놓여 있다. 이 <span class="m">3</span>개의 동전과 각 면에 숫자
<span class="m">1, 1, 1, 2</span>가 하나씩 적혀 있는 정사면체 모양의 상자를
사용하여 다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">상자를 던져서 바닥에 닿은 면에 적혀 있는 수만큼의 동전을 임의로 선택한 뒤</span>
<span class="cond m">선택한 모든 동전을 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>위의 시행을 <span class="m">3</span>번 반복한 후 앞면이 보이도록 놓여 있는
동전의 개수가 홀수일 때, 그 개수가 <span class="m">1</span>일 확률은
<span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>동전이 하나 줄었을 뿐인데 홀짝 조건이 정반대가 된다.</b>
처음에 앞면이 <span class="m">3</span>개로 <b>홀수</b>이기 때문이다.
원문항은 <span class="m">4</span>개로 짝수에서 시작했다.<br><br>

홀짝을 바꾸는 것은 <span class="m">1</span>이 나올 때뿐이므로,
홀수에서 다시 홀수로 가려면
<b><span class="m">1</span>이 짝수 번</b> 나와야 한다.
원문항에서는 홀수 번이었다. <b>조건이 뒤집혔다.</b><br><br>

<b>상태도 하나 줄어 <span class="m">0, 1, 2, 3</span> 네 개뿐이다.</b>
<span class="m">2</span>개를 고르는 방법도
<span class="m"><sub>3</sub>C<sub>2</sub> = 3</span>가지로 줄어
손으로 끝까지 따라가기 좋다.

## 풀이

<p><span class="step">① 분모를 구한다.</span>
처음 앞면이 <span class="m">3</span>개로 홀수이므로,
<span class="m">3</span>번 중 <span class="m">1</span>이
<b>짝수 번</b>(<span class="m">0</span>번 또는 <span class="m">2</span>번)
나와야 홀수로 남는다.</p>
<p class="m">P(홀수) = <sub>3</sub>C<sub>0</sub>(1/4)<sup>3</sup> + <sub>3</sub>C<sub>2</sub>(3/4)<sup>2</sup>(1/4)</p>
<p class="m">= (1/4)<sup>3</sup> + 3 × (9/16) × (1/4)</p>
<p class="m">= 1/64 + 27/64 = 28/64 = 7/16</p>

<p><span class="step">② 전이 규칙을 적는다.</span>
앞면이 <span class="m">a</span>개, 뒷면이 <span class="m">3 − a</span>개다.
<span class="m">2</span>개를 고르는 방법은
<span class="m"><sub>3</sub>C<sub>2</sub> = 3</span>가지뿐이다.</p>
<p class="m">1이 나오면 : 앞면을 고를 확률 a/3, 뒷면을 고를 확률 (3 − a)/3</p>
<p class="m">2가 나오면 : 앞면이 j개 섞일 확률 = <sub>a</sub>C<sub>j</sub> × <sub>3−a</sub>C<sub>2−j</sub> / 3</p>

<p><span class="step">③ 1번 시행 뒤의 상태를 구한다.</span>
세 개가 모두 앞면이므로 앞면만 뒤집힌다.</p>
<p class="m">1이 나오면 → 2개 : 3/4</p>
<p class="m">2가 나오면 → 1개 : 1/4</p>

<p><span class="step">④ 2번 시행 뒤의 상태를 구한다.</span>
<b>앞면이 2개인 상태(3/4)에서</b> 앞면 <span class="m">2</span>, 뒷면
<span class="m">1</span>이다.</p>
<p class="m">1이 나오고 앞면 : (3/4)(3/4)(2/3) = 3/8 → 1개</p>
<p class="m">1이 나오고 뒷면 : (3/4)(3/4)(1/3) = 3/16 → 3개</p>
<p class="m">2가 나오고 앞면 2개 : (3/4)(1/4)(1/3) = 1/16 → 0개</p>
<p class="m">2가 나오고 앞면 1개 : (3/4)(1/4)(2/3) = 1/8 → 2개</p>
<p><b>앞면이 1개인 상태(1/4)에서</b> 앞면 <span class="m">1</span>, 뒷면
<span class="m">2</span>이다.</p>
<p class="m">1이 나오고 앞면 : (1/4)(3/4)(1/3) = 1/16 → 0개</p>
<p class="m">1이 나오고 뒷면 : (1/4)(3/4)(2/3) = 1/8 → 2개</p>
<p class="m">2가 나오고 앞면 1개 : (1/4)(1/4)(2/3) = 1/24 → 1개</p>
<p class="m">2가 나오고 앞면 0개 : (1/4)(1/4)(1/3) = 1/48 → 3개</p>
<p>같은 상태끼리 모은다. 분모를 <span class="m">48</span>로 통일한다.</p>
<p class="m">0개 : 6/48 &nbsp; 1개 : 20/48 &nbsp; 2개 : 12/48 &nbsp; 3개 : 10/48</p>
<p>합이 <span class="m">48/48 = 1</span>임을 확인한다.</p>

<p><span class="step">⑤ 3번째 시행에서 앞면이 1개가 되는 길을 센다.</span></p>
<p class="m">0개 → 1이 나와 뒷면 : (1/8)(3/4)(1) = 3/32</p>
<p class="m">1개 → 2가 나와 앞면 1개 : (5/12)(1/4)(2/3) = 5/72</p>
<p class="m">2개 → 1이 나와 앞면 : (1/4)(3/4)(2/3) = 1/8</p>
<p class="m">3개 → 2가 나와 앞면 2개 : (5/24)(1/4)(1) = 5/96</p>
<p>분모를 <span class="m">288</span>로 통일하여 더한다.</p>
<p class="m">P(1개) = 27/288 + 20/288 + 36/288 + 15/288 = 98/288 = 49/144</p>

<p><span class="step">⑥ 조건부확률을 구하고 답을 만든다.</span>
<span class="m">P(홀수) = 7/16 = 63/144</span>이다.</p>
<p class="m">P(1개 | 홀수) = (49/144) / (63/144) = 49/63</p>
<p><span class="m">49 = 7 × 7</span>, <span class="m">63 = 7 × 9</span>이므로
<span class="m">7</span>로 약분한다.</p>
<p class="m">= 7/9</p>
<p><span class="m">7</span>과 <span class="m">9</span>는 서로소이므로
<span class="m">q = 7</span>, <span class="m">p = 9</span>이다.</p>
<p class="m">p + q = 9 + 7 = 16</p>
<p class="m">답 16</p>

## 함정

<b>처음 상태가 홀수라는 것을 놓치면 분모부터 틀린다.</b>
동전이 <span class="m">3</span>개이므로 앞면이
<span class="m">3</span>개, 곧 <b>홀수</b>에서 시작한다.
홀수로 남으려면 <span class="m">1</span>이
<b>짝수 번</b> 나와야 한다.
원문항의 감각으로 홀수 번을 쓰면 <span class="m">9/16</span>이 나와 틀린다.<br><br>

<b><span class="m">2</span>개를 고르는 방법의 수가
<span class="m">6</span>이 아니라 <span class="m">3</span>이다.</b>
동전이 세 개이므로
<span class="m"><sub>3</sub>C<sub>2</sub> = 3</span>이다.
<b>동전 개수가 바뀌면 이 분모도 함께 바뀐다.</b><br><br>

<b>앞면이 <span class="m">3</span>개일 때
<span class="m">2</span>가 나오면 반드시 앞면 두 개를 고른다.</b>
뒷면이 하나도 없기 때문이다. 확률이 <span class="m">1</span>이다.
표의 양 끝 상태에서는 이렇게 갈래가 줄어든다.

## 노하우

<b>처음 상태의 홀짝을 먼저 적고 시작한다.</b>
<b>&lsquo;처음 홀짝 → 목표 홀짝&rsquo;</b>을 적어 두면
<span class="m">1</span>이 홀수 번 나와야 하는지 짝수 번 나와야 하는지가
한눈에 정해진다.
이 문제에서는 <b>홀수 → 홀수</b>라 짝수 번이다.<br><br>

<b>동전 개수가 줄면 손으로 끝까지 갈 수 있다.</b>
상태가 네 개, 고르는 방법이 세 가지뿐이라
<b>표를 다 채워 놓고 검산</b>할 수 있다.
같은 유형이 어려울 때는 <b>개수를 줄여 한 번 손으로 끝까지 해 보는 것</b>이
구조를 익히는 가장 빠른 길이다.<br><br>

<b>단계마다 확률의 합이 <span class="m">1</span>인지 본다.</b>
④에서 <span class="m">6 + 20 + 12 + 10 = 48</span>로 맞는지 확인하고 넘어가면,
⑤에서 틀려도 어디서 틀렸는지 금방 찾는다.
