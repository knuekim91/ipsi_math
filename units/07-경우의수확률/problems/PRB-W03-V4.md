---
id: PRB-W03-V4
parent: PRB-W03
unit: 07-경우의수확률
topic: 동전 뒤집기와 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W03 변형 · 조건을 짝수로)
origin: 유사문항
core: "짝수 조건에서는 0, 2, 4 세 가지가 남으므로 여사건 한 줄로 끝나지 않고 목표 상태를 직접 세야 한다"
tags: [조건부확률,시행,홀짝,패리티,상태추적]
status: variant
added: 2026-10-11
answer: 85
---

## 문제

<p>탁자 위에 <span class="m">4</span>개의 동전이 모두 앞면이 보이도록
일렬로 놓여 있다. 이 <span class="m">4</span>개의 동전과 각 면에 숫자
<span class="m">1, 2, 2, 2</span>가 하나씩 적혀 있는 정사면체 모양의 상자를
사용하여 다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">상자를 던져서 바닥에 닿은 면에 적혀 있는 수만큼의 동전을 임의로 선택한 뒤</span>
<span class="cond m">선택한 모든 동전을 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>위의 시행을 <span class="m">3</span>번 반복한 후 앞면이 보이도록 놓여 있는
동전의 개수가 짝수일 때, 그 개수가 <span class="m">2</span>일 확률은
<span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>두 군데가 바뀌었다. 정사면체가
<span class="m">1, 2, 2, 2</span>이고, 조건이 <b>짝수</b>다.</b></p>
<p class="m">P(1이 나온다) = 1/4, &nbsp; P(2가 나온다) = 3/4</p>

<p><b>조건이 짝수라는 것이 계산을 늘린다.</b>
홀수일 때는 가능한 개수가 <span class="m">1</span>과
<span class="m">3</span> 둘뿐이라 여사건 한 줄로 끝났지만,
<b>짝수는 <span class="m">0, 2, 4</span> 세 가지</b>라 그 수가 안 통한다.
<span class="m">2</span>개인 경우를 <b>직접 세야</b> 한다.<br><br>

<b>분모는 여전히 홀짝으로 바로 나온다.</b>
처음 앞면이 <span class="m">4</span>개로 짝수이므로
짝수로 남으려면 <span class="m">1</span>이 <b>짝수 번</b> 나와야 한다.
이번에는 <span class="m">P(1) = 1/4</span>이라 원문항과 수가 뒤바뀐다.

## 풀이

<p><span class="step">① 분모를 구한다.</span>
<span class="m">1</span>이 <span class="m">0</span>번 또는
<span class="m">2</span>번 나와야 한다.</p>
<p class="m">P(짝수) = <sub>3</sub>C<sub>0</sub>(3/4)<sup>3</sup> + <sub>3</sub>C<sub>2</sub>(1/4)<sup>2</sup>(3/4)</p>
<p class="m">= 27/64 + 3 × (1/16) × (3/4) = 27/64 + 9/64 = 36/64 = 9/16</p>

<p><span class="step">② 1번 시행 뒤의 상태를 구한다.</span>
네 개가 모두 앞면이므로 앞면만 뒤집힌다.</p>
<p class="m">1이 나오면 → 3개 : 1/4</p>
<p class="m">2가 나오면 → 2개 : 3/4</p>

<p><span class="step">③ 2번 시행 뒤의 상태를 구한다.</span>
<b>앞면이 3개인 상태(1/4)에서</b> 앞면 <span class="m">3</span>, 뒷면
<span class="m">1</span>이다.</p>
<p class="m">1이 나오고 앞면 : (1/4)(1/4)(3/4) = 3/64 → 2개</p>
<p class="m">1이 나오고 뒷면 : (1/4)(1/4)(1/4) = 1/64 → 4개</p>
<p class="m">2가 나오고 앞면 2개 : (1/4)(3/4)(3/6) = 3/32 → 1개</p>
<p class="m">2가 나오고 앞면 1개 : (1/4)(3/4)(3/6) = 3/32 → 3개</p>
<p><b>앞면이 2개인 상태(3/4)에서</b> 앞면 <span class="m">2</span>, 뒷면
<span class="m">2</span>이다.</p>
<p class="m">1이 나오고 앞면 : (3/4)(1/4)(1/2) = 3/32 → 1개</p>
<p class="m">1이 나오고 뒷면 : (3/4)(1/4)(1/2) = 3/32 → 3개</p>
<p class="m">2가 나오고 앞면 2개 : (3/4)(3/4)(1/6) = 3/32 → 0개</p>
<p class="m">2가 나오고 앞면 1개 : (3/4)(3/4)(4/6) = 3/8 → 2개</p>
<p class="m">2가 나오고 앞면 0개 : (3/4)(3/4)(1/6) = 3/32 → 4개</p>
<p>같은 상태끼리 모은다. 분모를 <span class="m">64</span>로 통일한다.</p>
<p class="m">0개 : 6/64 &nbsp; 1개 : 12/64 &nbsp; 2개 : 27/64 &nbsp; 3개 : 12/64 &nbsp; 4개 : 7/64</p>
<p>합이 <span class="m">64/64 = 1</span>임을 확인한다.</p>

<p><span class="step">④ 3번째 시행에서 앞면이 2개가 되는 길을 센다.</span>
<span class="m">2</span>개에 닿는 길은 다섯 상태에서 모두 나온다.</p>
<p class="m">0개 → 2가 나와 뒷면 2개 : (6/64)(3/4)(1) = 18/256</p>
<p class="m">1개 → 1이 나와 뒷면 : (12/64)(1/4)(3/4) = 9/256</p>
<p class="m">2개 → 2가 나와 앞면 1개 : (27/64)(3/4)(4/6) = 54/256</p>
<p class="m">3개 → 1이 나와 앞면 : (12/64)(1/4)(3/4) = 9/256</p>
<p class="m">4개 → 2가 나와 앞면 2개 : (7/64)(3/4)(1) = 21/256</p>
<p>모두 더한다.</p>
<p class="m">P(2개) = (18 + 9 + 54 + 9 + 21)/256 = 111/256</p>

<p><span class="step">⑤ 조건부확률을 구한다.</span>
<span class="m">P(짝수) = 9/16 = 144/256</span>이다.</p>
<p class="m">P(2개 | 짝수) = (111/256) / (144/256) = 111/144</p>
<p><span class="m">111 = 3 × 37</span>, <span class="m">144 = 3 × 48</span>이므로
<span class="m">3</span>으로 약분한다.</p>
<p class="m">= 37/48</p>

<p><span class="step">⑥ 답을 만든다.</span>
<span class="m">37</span>과 <span class="m">48</span>은 서로소이므로
<span class="m">q = 37</span>, <span class="m">p = 48</span>이다.</p>
<p class="m">p + q = 48 + 37 = 85</p>
<p class="m">답 85</p>

## 함정

<b>짝수 조건에서는 여사건이 한 줄로 안 끝난다.</b>
짝수인 개수가 <span class="m">0, 2, 4</span>로 <b>셋</b>이기 때문이다.
<span class="m">1 − P(0개 | 짝수)</span>로 쓰면
<span class="m">4</span>개인 경우가 빠져 틀린다.
<b>조건 아래의 경우가 몇 가지인지 먼저 세는 습관</b>이 필요하다.<br><br>

<b>④에서 다섯 줄을 모두 써야 한다.</b>
<span class="m">2</span>개는 가운데 상태라 <b>어느 쪽에서든 닿을 수 있다.</b>
원문항에서 <span class="m">1</span>개를 구할 때는
<span class="m">4</span>개에서 오는 길이 없어 네 줄이었지만, 여기서는 다섯 줄이다.<br><br>

<b><span class="m">P(1) = 1/4</span>로 바뀐 것을 끝까지 유지한다.</b>
원문항과 수가 뒤바뀌었다.
<span class="m">1</span>이 적힌 면이 <b>하나뿐</b>이므로
동전 한 개만 뒤집히는 일이 드물고,
그래서 가운데 상태인 <span class="m">2</span>개에 확률이 많이 몰린다.
답이 <span class="m">37/48 ≒ 0.77</span>로 큰 것이 그 때문이다.

## 노하우

<b>조건을 보면 가능한 경우가 몇 가지인지부터 센다.</b>
동전 <span class="m">n</span>개에서
<b>홀수는 <span class="m">n/2</span>가지 안팎, 짝수는 그보다 하나 많다.</b>
경우가 둘이면 여사건이 통하고, 셋 이상이면 직접 세야 한다.
<b>이 판단을 먼저 해야 풀이 전략이 정해진다.</b><br><br>

<b>가운데 상태는 들어오는 길이 가장 많다.</b>
양 끝(<span class="m">0</span>개, <span class="m">4</span>개)은 갈래가 적고
가운데(<span class="m">2</span>개)는 많다.
<b>목표가 가운데면 줄이 늘어난다</b>고 미리 각오하고 표를 넓게 그린다.<br><br>

<b>세 변형의 답을 견주어 보면 구조가 보인다.</b></p>
<p class="m">1이 세 면 : 13/32 &nbsp;/&nbsp; 1이 두 면 : 15/32 &nbsp;/&nbsp; 1이 한 면 : 가운데로 쏠림</p>
<p><b><span class="m">2</span>가 자주 나올수록 두 개씩 뒤집혀
가운데 상태에 머무르기 쉽다.</b>
계산을 끝낸 뒤 이 방향이 맞는지 보면 실수를 잡을 수 있다.
