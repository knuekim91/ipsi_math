---
id: PRB-W03-V1
parent: PRB-W03
unit: 07-경우의수확률
topic: 동전 뒤집기와 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W03 변형 · 묻는 대상을 3개로)
origin: 유사문항
core: "앞면의 개수가 홀수이면 1 아니면 3이므로, 둘 중 계산이 쉬운 쪽을 구하고 1에서 빼면 된다"
tags: [조건부확률,시행,홀짝,패리티,여사건]
status: variant
added: 2026-10-11
answer: 51
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
동전의 개수가 홀수일 때, 그 개수가 <span class="m">3</span>일 확률은
<span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>원문항과 설정이 완전히 같고 묻는 개수만 <span class="m">1</span>에서
<span class="m">3</span>으로 바뀌었다.</b><br><br>

<b>여기서 가장 중요한 관찰은 이것이다.</b>
동전이 네 개이므로 앞면의 개수는
<span class="m">0, 1, 2, 3, 4</span> 중 하나이고,
그중 <b>홀수는 <span class="m">1</span>과 <span class="m">3</span> 둘뿐</b>이다.
곧 &lsquo;홀수&rsquo;라는 조건 아래에서는 두 가지 경우밖에 없으므로</p>
<p class="m">P(1개 | 홀수) + P(3개 | 홀수) = 1</p>
<p><b>둘 중 하나만 구하면 나머지는 빼기 한 번으로 나온다.</b><br><br>

<b>그러므로 계산이 쉬운 쪽을 고른다.</b>
<span class="m">3</span>개에 닿는 길을 직접 세도 되지만,
<span class="m">1</span>개에 닿는 길이 더 적으므로
<b><span class="m">1</span>개를 구하고 빼는 편</b>이 빠르다.
아래에서는 두 방법을 모두 보인다.

## 풀이

<p><span class="step">① 정사면체의 확률과 홀짝을 정리한다.</span></p>
<p class="m">P(1이 나온다) = 3/4, &nbsp; P(2가 나온다) = 1/4</p>
<p><span class="m">1</span>이 나오면 한 개를 뒤집어 홀짝이 바뀌고,
<span class="m">2</span>가 나오면 두 개를 뒤집어 홀짝이 그대로다.
처음 앞면이 <span class="m">4</span>개로 짝수이므로
<span class="m">1</span>이 홀수 번 나와야 홀수가 된다.</p>
<p class="m">P(홀수) = 3(3/4)(1/4)<sup>2</sup> + (3/4)<sup>3</sup> = 9/64 + 27/64 = 9/16</p>

<p><span class="step">② 2번 시행 뒤의 상태를 구한다.</span>
처음에 네 개가 모두 앞면이므로 <span class="m">1</span>번 시행 뒤에는
앞면이 <span class="m">3</span>개(확률 <span class="m">3/4</span>) 또는
<span class="m">2</span>개(확률 <span class="m">1/4</span>)이다.
여기서 한 번 더 나아가 같은 상태끼리 모으면 다음과 같다.
분모를 <span class="m">192</span>로 통일한다.</p>
<p class="m">0개 : 2/192 &nbsp; 1개 : 36/192 &nbsp; 2개 : 89/192 &nbsp; 3개 : 36/192 &nbsp; 4개 : 29/192</p>

<p><span class="step">③ 앞면이 1개가 되는 길을 센다.</span>
<span class="m">3</span>번째 시행에서 <span class="m">1</span>개에 닿는 길만 고른다.</p>
<p class="m">0개 → 1이 나와 뒷면을 고름 : (1/96)(3/4)(1) = 1/128</p>
<p class="m">1개 → 2가 나와 앞면 1개를 고름 : (3/16)(1/4)(3/6) = 3/128</p>
<p class="m">2개 → 1이 나와 앞면을 고름 : (89/192)(3/4)(1/2) = 89/512</p>
<p class="m">3개 → 2가 나와 앞면 2개를 고름 : (3/16)(1/4)(3/6) = 3/128</p>
<p class="m">P(1개) = 4/512 + 12/512 + 89/512 + 12/512 = 117/512</p>

<p><span class="step">④ 여사건으로 답을 만든다.</span>
<span class="m">P(홀수) = 9/16 = 288/512</span>이므로</p>
<p class="m">P(3개) = P(홀수) − P(1개) = 288/512 − 117/512 = 171/512</p>
<p class="m">P(3개 | 홀수) = (171/512) / (288/512) = 171/288</p>
<p><span class="m">171 = 9 × 19</span>, <span class="m">288 = 9 × 32</span>이므로
<span class="m">9</span>로 약분한다.</p>
<p class="m">= 19/32</p>

<p><span class="step">⑤ 더 빠른 길도 확인해 둔다.</span>
원문항에서 <span class="m">P(1개 | 홀수) = 13/32</span>를 이미 구했다면
그 한 줄로 끝난다.</p>
<p class="m">P(3개 | 홀수) = 1 − 13/32 = 19/32</p>

<p><span class="step">⑥ 답을 쓴다.</span>
<span class="m">19</span>와 <span class="m">32</span>는 서로소이므로
<span class="m">q = 19</span>, <span class="m">p = 32</span>이다.</p>
<p class="m">p + q = 32 + 19 = 51</p>
<p class="m">답 51</p>

## 함정

<b><span class="m">1 − 13/32</span>를 쓸 수 있는 이유를 확인하고 써야 한다.</b>
동전이 <b>네 개</b>라서 홀수인 개수가
<span class="m">1</span>과 <span class="m">3</span> 둘뿐이기 때문이다.
동전이 여섯 개였다면 홀수가
<span class="m">1, 3, 5</span> 세 가지라 이 방법을 쓸 수 없다.
<b>&lsquo;조건 아래의 경우가 정확히 둘인가&rsquo;를 먼저 센다.</b><br><br>

<b><span class="m">P(3개) = 1 − P(1개)</span>로 쓰면 안 된다.</b>
빼야 할 것은 <span class="m">1</span>이 아니라
<span class="m">P(홀수)</span>다.
조건을 붙이기 <b>전</b>의 확률끼리 뺄 때는
<span class="m">288/512 − 117/512</span>이고,
조건을 붙인 <b>뒤</b>라야 <span class="m">1</span>에서 뺄 수 있다.<br><br>

<b>약분을 빠뜨리면 서로소가 아니다.</b>
<span class="m">171/288</span>을 그대로 쓰면
<span class="m">p + q = 459</span>가 되어 틀린다.
<b>문제가 &lsquo;서로소&rsquo;라고 못 박았으면 반드시 끝까지 약분</b>한다.

## 노하우

<b>조건 아래의 경우가 둘뿐이면 쉬운 쪽을 구하고 뺀다.</b>
<span class="m">P(A | C) + P(B | C) = 1</span>이 되는 구조를 알아보면
계산량이 절반이 된다.
<b>어느 쪽이 쉬운지는 &lsquo;닿는 길의 개수&rsquo;로 판단</b>한다.
이 문제에서는 <span class="m">1</span>개 쪽이 네 갈래,
<span class="m">3</span>개 쪽이 다섯 갈래여서 <span class="m">1</span>개가 쉽다.<br><br>

<b>같은 설정의 문제를 여러 개 풀 때는 중간 결과를 적어 둔다.</b>
<span class="m">2</span>번 시행 뒤의 다섯 상태
<span class="m">2 : 36 : 89 : 36 : 29</span>(분모 <span class="m">192</span>)는
이 설정에서 계속 쓰인다.
<b>한 번 구해 두면 묻는 것이 바뀌어도 마지막 한 단계만</b> 다시 하면 된다.
