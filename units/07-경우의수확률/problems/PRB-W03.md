---
id: PRB-W03
unit: 07-경우의수확률
topic: 동전 뒤집기와 조건부확률
level: 4점
difficulty: 상
source: 나은이가 가져온 문제 (확률과 통계 30번, 홀수형)
exam: 오답노트
origin: 기출
core: "분모는 홀짝만 보면 정사면체의 이항분포로 바로 나오고, 분자만 앞면 개수를 상태로 삼아 전이표를 만든다"
tags: [조건부확률,시행,홀짝,패리티,상태추적]
status: wrong
added: 2026-10-11
answer: 45
---

## 문제

<p>탁자 위에 <span class="m">4</span>개의 동전이 모두 앞면이 보이도록
일렬로 놓여 있다. 이 <span class="m">4</span>개의 동전과 각 면에 숫자
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

<b>조건부확률이므로 분모와 분자를 따로 구한다.
그런데 두 쪽의 난이도가 전혀 다르다.</b></p>
<p class="m">P(앞면이 1개 | 앞면의 개수가 홀수) = P(앞면이 1개) / P(홀수)</p>

<p><b>분모는 홀짝만 보면 끝난다.</b>
한 번의 시행에서 뒤집는 동전이 <span class="m">1</span>개면
앞면의 개수가 <span class="m">1</span>만큼 바뀌므로 <b>홀짝이 바뀌고</b>,
<span class="m">2</span>개면 <span class="m">2</span>만큼 바뀌거나 그대로이므로
<b>홀짝이 바뀌지 않는다.</b>
처음에 앞면이 <span class="m">4</span>개로 짝수이므로,
<b>홀수가 되려면 &lsquo;<span class="m">1</span>이 나온 횟수&rsquo;가 홀수여야 한다.</b>
정사면체는 <span class="m">1</span>이 세 면, <span class="m">2</span>가 한 면이므로
이것은 <b>성공확률 <span class="m">3/4</span>인 독립시행</b> 문제가 된다.<br><br>

<b>분자는 그렇게 안 된다. 앞면의 개수를 끝까지 따라가야 한다.</b>
<span class="m">2</span>개를 고를 때 앞면이 몇 개 섞이느냐가
<b>지금 앞면이 몇 개인지에 따라 달라지기 때문</b>이다.
그러므로 <b>앞면의 개수를 상태로 삼아 한 시행씩 옮겨 가는 표</b>를 만든다.
상태는 <span class="m">0</span>부터 <span class="m">4</span>까지 다섯 개뿐이다.

## 풀이

<p><span class="step">① 정사면체의 확률을 적는다.</span>
네 면 중 <span class="m">1</span>이 세 면, <span class="m">2</span>가 한 면이다.</p>
<p class="m">P(1이 나온다) = 3/4, &nbsp; P(2가 나온다) = 1/4</p>

<p><span class="step">② 분모를 홀짝으로 구한다.</span>
<span class="m">1</span>이 나오면 동전 한 개를 뒤집으므로 앞면의 개수의 홀짝이 바뀌고,
<span class="m">2</span>가 나오면 두 개를 뒤집으므로 홀짝이 그대로다.
처음 앞면은 <span class="m">4</span>개로 짝수이므로,
<span class="m">3</span>번 중 <span class="m">1</span>이
<b>홀수 번</b> 나와야 앞면의 개수가 홀수가 된다.</p>
<p class="m">P(홀수) = <sub>3</sub>C<sub>1</sub>(3/4)(1/4)<sup>2</sup> + <sub>3</sub>C<sub>3</sub>(3/4)<sup>3</sup></p>
<p class="m">= 3 × 3/64 + 27/64 = 9/64 + 27/64 = 36/64 = 9/16</p>

<p><span class="step">③ 전이 규칙을 적어 둔다.</span>
앞면이 <span class="m">a</span>개일 때 뒷면은
<span class="m">4 − a</span>개다.<br>
<b><span class="m">1</span>이 나온 경우</b>: 고른 한 개가 앞면이면
<span class="m">a</span>가 <span class="m">1</span> 줄고, 뒷면이면
<span class="m">1</span> 는다.</p>
<p class="m">앞면을 고를 확률 a/4, &nbsp; 뒷면을 고를 확률 (4 − a)/4</p>
<p><b><span class="m">2</span>가 나온 경우</b>: <span class="m">4</span>개에서
<span class="m">2</span>개를 고르는 방법이
<span class="m"><sub>4</sub>C<sub>2</sub> = 6</span>가지이고,
그중 앞면이 <span class="m">j</span>개 섞일 확률은
<span class="m"><sub>a</sub>C<sub>j</sub> × <sub>4−a</sub>C<sub>2−j</sub> / 6</span>이다.
이때 앞면은 <span class="m">j</span>개 줄고
<span class="m">2 − j</span>개 늘어난다.</p>

<p><span class="step">④ 1번 시행 뒤의 상태를 구한다.</span>
처음에는 네 개가 모두 앞면이므로 무엇을 고르든 앞면만 뒤집힌다.</p>
<p class="m">1이 나오면 → 앞면 3개 : 3/4</p>
<p class="m">2가 나오면 → 앞면 2개 : 1/4</p>

<p><span class="step">⑤ 2번 시행 뒤의 상태를 구한다.</span>
<b>앞면이 3개인 상태(3/4)에서</b> 앞면 <span class="m">3</span>, 뒷면
<span class="m">1</span>이므로</p>
<p class="m">1이 나오고 앞면을 고름 : (3/4)(3/4)(3/4) = 27/64 → 앞면 2개</p>
<p class="m">1이 나오고 뒷면을 고름 : (3/4)(3/4)(1/4) = 9/64 → 앞면 4개</p>
<p class="m">2가 나오고 앞면 2개 : (3/4)(1/4)(3/6) = 3/32 → 앞면 1개</p>
<p class="m">2가 나오고 앞면 1개 : (3/4)(1/4)(3/6) = 3/32 → 앞면 3개</p>
<p><b>앞면이 2개인 상태(1/4)에서</b> 앞면 <span class="m">2</span>, 뒷면
<span class="m">2</span>이므로</p>
<p class="m">1이 나오고 앞면을 고름 : (1/4)(3/4)(1/2) = 3/32 → 앞면 1개</p>
<p class="m">1이 나오고 뒷면을 고름 : (1/4)(3/4)(1/2) = 3/32 → 앞면 3개</p>
<p class="m">2가 나오고 앞면 2개 : (1/4)(1/4)(1/6) = 1/96 → 앞면 0개</p>
<p class="m">2가 나오고 앞면 1개 : (1/4)(1/4)(4/6) = 1/24 → 앞면 2개</p>
<p class="m">2가 나오고 앞면 0개 : (1/4)(1/4)(1/6) = 1/96 → 앞면 4개</p>
<p>같은 상태끼리 모은다. 분모를 <span class="m">192</span>로 통일한다.</p>
<p class="m">0개 : 2/192 &nbsp; 1개 : 36/192 &nbsp; 2개 : 89/192 &nbsp; 3개 : 36/192 &nbsp; 4개 : 29/192</p>
<p>합이 <span class="m">192/192 = 1</span>인지 확인하고 넘어간다.</p>

<p><span class="step">⑥ 3번째 시행에서 앞면이 1개가 되는 길만 고른다.</span>
<b>분자는 <span class="m">P(앞면 1개)</span> 하나뿐이므로
거기에 닿는 길만 세면 된다.</b></p>
<p class="m">0개 → 1이 나와 뒷면을 고름 : (1/96)(3/4)(1) = 1/128</p>
<p class="m">1개 → 2가 나와 앞면 1개를 고름 : (3/16)(1/4)(3/6) = 3/128</p>
<p class="m">2개 → 1이 나와 앞면을 고름 : (89/192)(3/4)(1/2) = 89/512</p>
<p class="m">3개 → 2가 나와 앞면 2개를 고름 : (3/16)(1/4)(3/6) = 3/128</p>
<p><span class="m">4</span>개인 상태에서는 한 번에 <span class="m">1</span>개가 될 수 없다.
분모를 <span class="m">512</span>로 통일하여 더한다.</p>
<p class="m">P(앞면 1개) = 4/512 + 12/512 + 89/512 + 12/512 = 117/512</p>

<p><span class="step">⑦ 조건부확률을 구한다.</span>
②에서 <span class="m">P(홀수) = 9/16 = 288/512</span>이다.</p>
<p class="m">P(1개 | 홀수) = (117/512) / (288/512) = 117/288</p>
<p><span class="m">117 = 9 × 13</span>, <span class="m">288 = 9 × 32</span>이므로
<span class="m">9</span>로 약분한다.</p>
<p class="m">= 13/32</p>

<p><span class="step">⑧ 답을 만든다.</span>
<span class="m">q/p = 13/32</span>이고
<span class="m">13</span>과 <span class="m">32</span>는 서로소이므로
<span class="m">q = 13</span>, <span class="m">p = 32</span>이다.</p>
<p class="m">p + q = 32 + 13 = 45</p>
<p class="m">답 45</p>

## 함정

<b>분모를 <span class="m">1</span>로 두면 안 된다.</b>
&lsquo;개수가 홀수일 때&rsquo;가 조건이므로 <b>표본공간이 홀수인 경우로 줄어든다.</b>
<span class="m">117/512</span>를 그대로 답으로 쓰면 조건부확률이 아니다.<br><br>

<b><span class="m">2</span>개를 고를 때의 확률을
<span class="m">(1/2)<sup>2</sup></span>처럼 쓰면 안 된다.</b>
<span class="m">4</span>개에서 <span class="m">2</span>개를 <b>동시에</b> 고르는 것이므로
분모가 <span class="m"><sub>4</sub>C<sub>2</sub> = 6</span>이다.
한 개씩 두 번 고르는 것이 아니다.<br><br>

<b>앞면이 <span class="m">4</span>개인 상태를 빠뜨리지 않도록 끝까지 적는다.</b>
⑥에서 <span class="m">4</span>개인 상태는 한 번에
<span class="m">1</span>개가 될 수 없어 기여가 <span class="m">0</span>이다.
<b>&lsquo;안 되는 줄&rsquo;도 확인하고 넘어가야</b> 빠뜨린 것이 없다고 말할 수 있다.<br><br>

<b>각 단계에서 확률의 합이 <span class="m">1</span>인지 확인한다.</b>
⑤에서 다섯 상태의 합이 <span class="m">1</span>이 되어야 한다.
여기서 어긋나면 ⑥의 계산은 전부 무의미하다.

## 노하우

<b>조건부확률은 분모와 분자의 난이도가 다를 때가 많다.</b>
이 문제처럼 <b>분모가 홀짝으로 한 줄에 나오면 거기서 시간을 아껴</b>
분자에 집중한다. 분모까지 상태표로 구하려 들면 시간이 모자란다.<br><br>

<b>뒤집기 문제에서 홀짝은 늘 먼저 본다.</b>
<b>짝수 개를 뒤집으면 홀짝이 보존되고, 홀수 개를 뒤집으면 바뀐다.</b>
그래서 &lsquo;몇 개를 뒤집었는가&rsquo;가 아니라
<b>&lsquo;홀수 개를 뒤집은 횟수&rsquo;</b>만 세면 최종 홀짝이 정해진다.
같은 발상을 쓰는 문항으로 <span class="m">PRB-W01</span>,
<span class="m">PRB-J28</span>이 있다.<br><br>

<b>개수가 상태일 때는 표를 세로로 쌓는다.</b>
상태가 다섯 개뿐이므로 한 시행마다 다섯 칸을 채우면 된다.
<b>마지막 단계에서는 목표 상태에 닿는 길만</b> 세면 되므로
표를 끝까지 다 채울 필요도 없다.<br><br>

<b>같은 조건에서 나머지 하나는 여사건으로 나온다.</b>
앞면의 개수가 홀수이면 <span class="m">1</span> 아니면
<span class="m">3</span>이므로</p>
<p class="m">P(3개 | 홀수) = 1 − 13/32 = 19/32</p>
<p>이다. <b>둘 중 계산이 쉬운 쪽을 구하고 빼면 된다.</b>
