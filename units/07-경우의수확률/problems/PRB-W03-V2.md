---
id: PRB-W03-V2
parent: PRB-W03
unit: 07-경우의수확률
topic: 동전 뒤집기와 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W03 변형 · 정사면체를 1,1,2,2로)
origin: 유사문항
core: "1과 2가 반반이면 홀짝이 바뀔 확률도 반이라 P(홀수)가 정확히 1/2이 된다"
tags: [조건부확률,시행,홀짝,패리티,상태추적]
status: variant
added: 2026-10-11
answer: 47
---

## 문제

<p>탁자 위에 <span class="m">4</span>개의 동전이 모두 앞면이 보이도록
일렬로 놓여 있다. 이 <span class="m">4</span>개의 동전과 각 면에 숫자
<span class="m">1, 1, 2, 2</span>가 하나씩 적혀 있는 정사면체 모양의 상자를
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

<b>정사면체의 면이 <span class="m">1, 1, 2, 2</span>로 반반이 되었다.</b></p>
<p class="m">P(1이 나온다) = P(2가 나온다) = 2/4 = 1/2</p>

<p><b>그러면 분모가 아주 깔끔해진다.</b>
홀짝을 바꾸는 것은 <span class="m">1</span>이 나올 때뿐인데
그 확률이 <span class="m">1/2</span>이므로,
<span class="m">3</span>번 중 홀수 번 나올 확률은
<b>동전을 세 번 던져 앞면이 홀수 번 나올 확률</b>과 같아
<span class="m">1/2</span>이 된다.<br><br>

<b>분자는 여전히 상태를 따라가야 한다.</b>
<span class="m">2</span>개를 고를 때 앞면이 몇 개 섞이느냐가
지금 앞면의 개수에 달려 있기 때문이다.
<b>틀은 원문항과 똑같고 두 갈래의 확률만 <span class="m">1/2</span>씩으로 바뀐다.</b>

## 풀이

<p><span class="step">① 분모를 구한다.</span>
<span class="m">1</span>이 나올 확률이 <span class="m">1/2</span>이므로
<span class="m">3</span>번 중 홀수 번 나올 확률은</p>
<p class="m">P(홀수) = <sub>3</sub>C<sub>1</sub>(1/2)<sup>3</sup> + <sub>3</sub>C<sub>3</sub>(1/2)<sup>3</sup></p>
<p class="m">= 3/8 + 1/8 = 4/8 = 1/2</p>

<p><span class="step">② 1번 시행 뒤의 상태를 구한다.</span>
네 개가 모두 앞면이므로 무엇을 고르든 앞면만 뒤집힌다.</p>
<p class="m">1이 나오면 → 앞면 3개 : 1/2</p>
<p class="m">2가 나오면 → 앞면 2개 : 1/2</p>

<p><span class="step">③ 2번 시행 뒤의 상태를 구한다.</span>
<b>앞면이 3개인 상태(1/2)에서</b> 앞면 <span class="m">3</span>, 뒷면
<span class="m">1</span>이다.</p>
<p class="m">1이 나오고 앞면 : (1/2)(1/2)(3/4) = 3/16 → 2개</p>
<p class="m">1이 나오고 뒷면 : (1/2)(1/2)(1/4) = 1/16 → 4개</p>
<p class="m">2가 나오고 앞면 2개 : (1/2)(1/2)(3/6) = 1/8 → 1개</p>
<p class="m">2가 나오고 앞면 1개 : (1/2)(1/2)(3/6) = 1/8 → 3개</p>
<p><b>앞면이 2개인 상태(1/2)에서</b> 앞면 <span class="m">2</span>, 뒷면
<span class="m">2</span>이다.</p>
<p class="m">1이 나오고 앞면 : (1/2)(1/2)(1/2) = 1/8 → 1개</p>
<p class="m">1이 나오고 뒷면 : (1/2)(1/2)(1/2) = 1/8 → 3개</p>
<p class="m">2가 나오고 앞면 2개 : (1/2)(1/2)(1/6) = 1/24 → 0개</p>
<p class="m">2가 나오고 앞면 1개 : (1/2)(1/2)(4/6) = 1/6 → 2개</p>
<p class="m">2가 나오고 앞면 0개 : (1/2)(1/2)(1/6) = 1/24 → 4개</p>
<p>같은 상태끼리 모은다. 분모를 <span class="m">48</span>로 통일한다.</p>
<p class="m">0개 : 2/48 &nbsp; 1개 : 12/48 &nbsp; 2개 : 17/48 &nbsp; 3개 : 12/48 &nbsp; 4개 : 5/48</p>

<p><span class="step">④ 3번째 시행에서 앞면이 1개가 되는 길을 센다.</span></p>
<p class="m">0개 → 1이 나와 뒷면 : (1/24)(1/2)(1) = 1/48</p>
<p class="m">1개 → 2가 나와 앞면 1개 : (1/4)(1/2)(3/6) = 1/16</p>
<p class="m">2개 → 1이 나와 앞면 : (17/48)(1/2)(1/2) = 17/192</p>
<p class="m">3개 → 2가 나와 앞면 2개 : (1/4)(1/2)(3/6) = 1/16</p>
<p>분모를 <span class="m">192</span>로 통일하여 더한다.</p>
<p class="m">P(1개) = 4/192 + 12/192 + 17/192 + 12/192 = 45/192 = 15/64</p>

<p><span class="step">⑤ 조건부확률을 구하고 답을 만든다.</span></p>
<p class="m">P(1개 | 홀수) = (15/64) / (1/2) = 15/64 × 2 = 15/32</p>
<p><span class="m">15</span>와 <span class="m">32</span>는 서로소이므로
<span class="m">q = 15</span>, <span class="m">p = 32</span>이다.</p>
<p class="m">p + q = 32 + 15 = 47</p>
<p class="m">답 47</p>

## 함정

<b><span class="m">1, 1, 2, 2</span>를 보고
<span class="m">P(1) = 1/2</span>임을 확인하고 넘어간다.</b>
네 면 중 두 면이므로 <span class="m">2/4</span>다.
원문항의 <span class="m">3/4</span>를 그대로 쓰면 처음부터 다 틀린다.<br><br>

<b><span class="m">2</span>개를 고를 때의 분모는 여전히
<span class="m"><sub>4</sub>C<sub>2</sub> = 6</span>이다.</b>
정사면체가 바뀌어도 <b>동전은 네 개 그대로</b>이므로
고르는 방법의 수는 달라지지 않는다.
<b>무엇이 바뀌고 무엇이 그대로인지 구분</b>하는 것이 변형 문항의 핵심이다.<br><br>

<b>원문항보다 답이 커진 것이 맞는지 본다.</b>
원문항은 <span class="m">13/32</span>, 여기서는 <span class="m">15/32</span>다.
<span class="m">2</span>가 더 자주 나와 <b>두 개씩 뒤집히는 일이 늘면</b>
앞면이 적은 쪽으로 더 많이 내려간다.

## 노하우

<b>확률이 반반이면 홀짝 계산이 <span class="m">1/2</span>로 떨어진다.</b>
성공확률이 <span class="m">1/2</span>인 독립시행에서
<b>성공 횟수가 홀수일 확률은 횟수와 상관없이 언제나
<span class="m">1/2</span></b>이다.
<span class="m">(1/2 + 1/2)<sup>n</sup></span>과
<span class="m">(1/2 − 1/2)<sup>n</sup></span>을 비교하면 나오는 성질인데,
외워 두면 분모를 세지 않고 바로 쓸 수 있다.<br><br>

<b>변형 문항은 &lsquo;바뀐 수&rsquo;에만 동그라미를 친다.</b>
이 문제에서 바뀐 것은 <span class="m">P(1)</span>과
<span class="m">P(2)</span> 둘뿐이고,
<span class="m"><sub>4</sub>C<sub>2</sub></span>나 상태의 개수는 그대로다.
<b>틀을 그대로 두고 숫자만 갈아 끼우면</b> 두 번째 문제부터는 훨씬 빠르다.
