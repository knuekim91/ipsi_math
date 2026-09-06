---
id: TRI-J14
unit: 02-삼각함수
topic: 삼각방정식의 실근 개수
level: 4점
difficulty: 상
source: 2027-06모평 14번
exam: 2027-06모평
origin: 기출
core: "cos의 값이 ±1이면 근이 절반으로 줄고, 그 덕에 홀수 개가 나온다"
tags: [삼각방정식,실근개수,주기]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>양수 <span class="m">a</span>와 자연수 <span class="m">b</span>에 대하여 <span class="m">0 ≤ x ≤ 2</span>에서 방정식</p><span class="cond m">(cos(bπx) − 1/2)(a cos(bπx) + (a+2)/2) = 0</span><p>의 서로 다른 실근의 개수가 15일 때, <span class="m">a + b</span>의 값은?</p><div class="choices"><span>① 5</span><span>② 6</span><span>③ 7</span><span>④ 8</span><span>⑤ 9</span></div>

## 발상

곱이 0이니 <span class='m'>cos(bπx) = 1/2</span> 또는 <span class='m'>cos(bπx) = −(a+2)/(2a)</span>. <span class='m'>0 ≤ x ≤ 2</span>는 <b>정확히 b주기</b>다. <b>한 주기에 근이 2개씩 나오므로 합은 짝수여야 하는데 15는 홀수</b> — 어딘가에서 근이 절반으로 줄어야 하고, 그건 <span class='m'>cos = ±1</span>일 때뿐이다.

## 풀이

<p><span class="step">① 곱이 0이므로 두 방정식으로 나눈다.</span>
두 수의 곱이 <span class="m">0</span>이면 둘 중 하나가 <span class="m">0</span>이다.</p>
<p class="m">cos(bπx) = 1/2 &nbsp;&nbsp; 또는 &nbsp;&nbsp; a cos(bπx) + (a+2)/2 = 0</p>
<p>두 번째 식을 <span class="m">cos</span>에 대해 정리한다.
(<span class="m">a</span>는 양수라 <span class="m">0</span>으로 나눌 걱정이 없다.)</p>
<p class="m">cos(bπx) = −(a + 2)/(2a) &nbsp; 이 값을 c<sub>2</sub>라 하자</p>

<p><span class="step">② 구간이 몇 주기인지 센다.</span>
<span class="m">u = bπx</span>로 두면
<span class="m">x</span>가 <span class="m">0</span>에서 <span class="m">2</span>까지 갈 때 <span class="m">u</span>는 <span class="m">0</span>에서 <span class="m">2bπ</span>까지 간다.
<span class="m">cos</span>의 주기가 <span class="m">2π</span>이므로 이것은 <b>정확히 <span class="m">b</span>주기</b>다.</p>

<p><span class="step">③ 한 주기당 근이 몇 개인지 정리한다.</span>
<span class="m">cos u = c</span>의 근의 개수는 <span class="m">c</span>의 값에 따라 다르다.</p>
<p class="m">−1 &lt; c &lt; 1 : 한 주기에 2개 → 모두 2b개</p>
<p class="m">c = −1 : 한 주기에 1개(접점) → 모두 b개</p>
<p class="m">|c| &gt; 1 : 0개</p>

<p><span class="step">④ 개수가 홀수라는 것이 무엇을 뜻하는지 본다.</span>
<b>실근이 15개, 즉 홀수다.</b>
그런데 위 표에서 <span class="m">2b</span>는 항상 짝수이므로,
<b>어딘가에서 근이 절반으로 줄어야 하고 그것은 <span class="m">c = −1</span>일 때뿐</b>이다.
이것이 이 문제의 핵심 단서다.</p>

<p><span class="step">⑤ 첫 번째 방정식의 근을 센다.</span>
<span class="m">1/2</span>은 <span class="m">−1</span>과 <span class="m">1</span> 사이이므로 언제나 <span class="m">2b</span>개다.</p>

<p><span class="step">⑥ 두 번째 방정식을 a에 따라 나눈다.</span>
<span class="m">a &gt; 0</span>이므로 <span class="m">c<sub>2</sub> = −(a+2)/(2a)</span>는 <b>항상 음수</b>다.
따라서 <span class="m">1/2</span>과 같아질 일이 없어 <b>두 방정식의 근이 겹치지 않는다.</b>
<span class="m">c<sub>2</sub></span>가 <span class="m">−1</span>보다 큰지 작은지를 따진다.</p>
<p class="m">c<sub>2</sub> ≥ −1 ⟺ (a+2)/(2a) ≤ 1 ⟺ a + 2 ≤ 2a ⟺ a ≥ 2</p>

<p><b>[경우 1] <span class="m">a &lt; 2</span></b> — <span class="m">c<sub>2</sub> &lt; −1</span>이라 근이 없다.
총 <span class="m">2b = 15</span>인데 왼쪽은 짝수라 <b>불가능</b>하다.</p>

<p><b>[경우 2] <span class="m">a &gt; 2</span></b> — <span class="m">−1 &lt; c<sub>2</sub> &lt; 0</span>이라 <span class="m">2b</span>개다.
총 <span class="m">2b + 2b = 4b = 15</span>인데 <span class="m">15</span>는 <span class="m">4</span>의 배수가 아니라 <b>불가능</b>하다.</p>

<p><b>[경우 3] <span class="m">a = 2</span></b> — <span class="m">c<sub>2</sub> = −4/4 = −1</span>이라 <span class="m">b</span>개다.</p>
<p class="m">2b + b = 3b = 15 → b = 5</p>
<p><span class="m">b = 5</span>는 자연수이므로 조건에 맞는다.</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">a + b = 2 + 5 = 7</p>
<p class="m">답 ③</p>

## 함정

<b>15가 홀수라는 것 자체가 결정적인 단서</b>다. 일반적인 경우는 모두 짝수가 나오므로, 홀수를 만들 수 있는 예외(<span class='m'>cos = ±1</span>, 즉 접하는 경우)를 찾아야 한다는 신호다.

## 노하우

<b>삼각방정식의 실근 개수는 &lsquo;구간이 몇 주기인가 × 한 주기당 몇 개인가&rsquo;로 센다.</b> <span class='m'>cos u = c</span>는 한 주기에 <b>보통 2개</b>지만 <span class='m'>c = ±1</span>이면 <b>1개(접점)</b>가 된다. 개수가 홀수로 주어지면 거의 항상 이 접점 경우를 묻는 것이다.
