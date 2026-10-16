---
id: PRB-W04-V1
parent: PRB-W04
unit: 07-경우의수확률
topic: 맞바꾸기 대칭으로 대소 조건 세기
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W04 변형 · 경우를 나누지 않고 세기)
origin: 유사문항
core: "a와 b를 맞바꾸어도 조건이 그대로이므로 a<b 와 a>b 의 개수가 같다. 전체에서 a=b 만 빼고 반으로 나눈다"
tags: [중복조합,절댓값,대칭,일대일대응,순서쌍]
status: variant
added: 2026-10-17
answer: 162
---

## 문제

<p>다음 조건을 만족시키는 <span class="m">0</span>이 아닌 네 정수
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>의 모든 순서쌍
<span class="m">(a, b, c, d)</span>의 개수를 구하시오.</p>

<div class="cond">
<span class="cond m">(가) a + b + c + d = 0</span>
<span class="cond m">(나) |a| + |b| + |c| + |d| = 14</span>
<span class="cond m">(다) a &lt; b</span>
</div>

## 발상

<b>모문항의 (다)에서 절댓값만 걷어냈다.</b>
그런데 세는 방법은 완전히 달라진다.<br><br>

<b>절댓값이 있을 때는 부호로 갈래를 나눌 수밖에 없었다.</b>
<span class="m">|a| + a</span>가
<span class="m">a</span>의 부호에 따라 다른 식이 되기 때문이다.
<b>하지만 그냥 <span class="m">a &lt; b</span>라면
부호를 따질 필요가 없다.</b><br><br>

<b>대신 짝짓기를 쓴다.</b>
어떤 순서쌍 <span class="m">(a, b, c, d)</span>에서
<span class="m">a</span>와 <span class="m">b</span>만 맞바꾸어
<span class="m">(b, a, c, d)</span>를 만들어도
<b>(가)와 (나)는 그대로</b>다.
그리고 <span class="m">a &lt; b</span>이던 것은
<span class="m">a &gt; b</span>가 된다.
<b>곧 두 무리가 하나씩 짝을 이룬다.</b><br><br>

<b>그러면 개수가 같다.</b>
전체에서 <span class="m">a = b</span>인 것만 떼어 내고
<b>나머지를 반으로 나누면</b> 끝난다.

## 풀이

<p><span class="step">① (다) 없이 전체를 센다.</span>
양수들의 합을 <span class="m">A</span>,
음수들의 합을 <span class="m">B</span>라 하면
(가), (나)에서</p>
<p class="m">A + B = 0, &nbsp; A − B = 14 → A = 7, B = −7</p>
<p>음수가 <span class="m">k</span>개라 하면 양수는
<span class="m">4 − k</span>개이고,
<span class="m">k</span>개의 양의 정수의 합이
<span class="m">7</span>인 순서쌍의 개수는
<span class="m"><sub>k</sub>H<sub>7−k</sub> = <sub>6</sub>C<sub>k−1</sub></span>이다.</p>
<p class="m">k = 1 → 1, &nbsp; k = 2 → 6, &nbsp; k = 3 → 15</p>
<p>음수가 들어갈 자리를 고르는 것까지 세면</p>
<p class="m">k = 1 : <sub>4</sub>C<sub>1</sub> × 1 × 15 = 60</p>
<p class="m">k = 2 : <sub>4</sub>C<sub>2</sub> × 6 × 6 = 216</p>
<p class="m">k = 3 : <sub>4</sub>C<sub>3</sub> × 15 × 1 = 60</p>
<p class="m">60 + 216 + 60 = 336</p>

<p><span class="step">② 맞바꾸기가 짝짓기임을 확인한다.</span>
<span class="m">(a, b, c, d)</span>를
<span class="m">(b, a, c, d)</span>로 보내는 대응을 생각하면,
<b>네 수의 합도 절댓값의 합도 그대로</b>이므로
조건 (가), (나)를 만족시키는 순서쌍끼리 서로 옮겨간다.
또 두 번 하면 제자리로 돌아오므로 <b>일대일대응</b>이다.
이 대응은 <span class="m">a &lt; b</span>인 것과
<span class="m">a &gt; b</span>인 것을 맞바꾸므로</p>
<p class="m">(a &lt; b 인 개수) = (a &gt; b 인 개수)</p>

<p><span class="step">③ a = b 인 것을 센다.</span>
<span class="m">a = b</span>이면 두 수의 부호가 같다.<br>

<b><span class="m">a = b &gt; 0</span>인 경우</b><br>
양수들의 합이 <span class="m">7</span>이므로
<span class="m">c</span>, <span class="m">d</span> 쪽의 양수들의 합은
<span class="m">7 − 2a</span>이고, 음수들의 절댓값의 합은
<span class="m">7</span>이다.
<span class="m">c</span>, <span class="m">d</span>가 둘 다 양수이면 음수가 없고,
둘 다 음수이면 <span class="m">2a = 7</span>이 되어 정수가 아니다.
따라서 <b>하나는 양수, 하나는 음수</b>이고</p>
<p class="m">양수 = 7 − 2a ≥ 1 → a ≤ 3</p>
<p><span class="m">a = 1, 2, 3</span>이고 음수는
<span class="m">−7</span>로 정해진다.
<span class="m">c</span>, <span class="m">d</span> 중 어느 쪽이 양수인지
<span class="m">2</span>가지이므로</p>
<p class="m">3 × 2 = 6</p>

<p><b><span class="m">a = b &lt; 0</span>인 경우</b><br>
부호를 모두 뒤집으면 위와 똑같은 셈이 되므로
<span class="m">6</span>가지다.</p>
<p class="m">6 + 6 = 12</p>

<p><span class="step">④ 답을 만든다.</span></p>
<p class="m">(336 − 12) ÷ 2 = 324 ÷ 2 = 162</p>
<p class="m">답 162</p>

## 함정

<b><span class="m">336 ÷ 2 = 168</span>이라고 답하면 안 된다.</b>
<span class="m">a = b</span>인 <span class="m">12</span>가지는
<b>어느 쪽에도 속하지 않는다.</b>
맞바꾸기로 자기 자신에게 가는 것들이기 때문이다.
<b>짝짓기를 쓸 때는 &lsquo;자기 자신과 짝이 되는 것&rsquo;을 먼저 떼어 낸다.</b><br><br>

<b><span class="m">a = b</span>에서 부호가 같다는 것을 놓치지 않는다.</b>
<span class="m">a = b</span>이면 당연히 둘의 부호가 같고,
<span class="m">0</span>이 아니므로 둘 다 양수이거나 둘 다 음수다.
<b>두 경우를 모두 세야 <span class="m">12</span>가 된다.</b>
한쪽만 세면 <span class="m">6</span>이 되어 답이
<span class="m">165</span>가 되는데, <b>홀수가 나오는 순간 틀린 것</b>이다.<br><br>

<b>모문항의 답과 비교해 본다.</b>
모문항의 (다)는
<span class="m">b &gt; 0</span>이고 <span class="m">a &lt; b</span>라는 뜻이었다.
<b>이 문항은 <span class="m">b &gt; 0</span>이라는 제한이 빠진 것</b>이므로
답이 더 커야 한다.</p>
<p class="m">132 &lt; 162 ✓</p>
<p>차이 <span class="m">30</span>은
<span class="m">a &lt; b &lt; 0</span>인 경우의 수다.

## 노하우

<b>&lsquo;<span class="m">a &lt; b</span>&rsquo; 꼴이 보이면 맞바꾸기를 먼저 떠올린다.</b></p>
<p class="m">(a &lt; b 인 개수) = (전체 − a = b 인 개수) ÷ 2</p>
<p>조건이 <span class="m">a</span>와 <span class="m">b</span>를
<b>대등하게</b> 다루고 있을 때만 쓸 수 있다.
이 문제에서 (가)와 (나)는 네 수를 모두 대등하게 다루므로 쓸 수 있고,
모문항의 (다)는 <span class="m">a</span>와 <span class="m">b</span>를
<b>다르게</b> 다루므로 쓸 수 없었다.
<b>쓸 수 있는지부터 확인한다.</b><br><br>

<b>짝짓기를 쓸 때 확인할 것은 세 가지다.</b></p>
<p class="m">① 조건을 보존하는가 (옮긴 것도 여전히 조건을 만족시키는가)</p>
<p class="m">② 두 번 하면 제자리인가 (일대일대응인가)</p>
<p class="m">③ 자기 자신과 짝이 되는 것은 무엇인가</p>
<p><b>③을 빠뜨리는 것이 이 방법의 거의 유일한 실수</b>다.<br><br>

<b>부호를 뒤집는 대칭도 자주 쓴다.</b>
<span class="m">(a, b, c, d) → (−a, −b, −c, −d)</span>도
(가), (나)를 보존하는 일대일대응이다.
<b>&lsquo;모두 양수인 경우&rsquo;와 &lsquo;모두 음수인 경우&rsquo;의 개수가 같다</b>는 것을
이것으로 한 줄에 쓸 수 있다.
이 문항의 ③에서 <span class="m">a = b &lt; 0</span>을
다시 세지 않고 넘어간 근거가 바로 이것이다.
