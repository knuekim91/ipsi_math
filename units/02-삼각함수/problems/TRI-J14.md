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

<p><span class="step">① 구간을 주기로 읽는다.</span> <span class="m">u = bπx</span>라 하면 <span class="m">x : 0 → 2</span>일 때 <span class="m">u : 0 → 2bπ</span>, 곧 <b>b주기</b>.</p><p><span class="step">② 근의 개수 규칙.</span> <span class="m">cos u = c</span>의 근의 개수는</p><p class="m">−1 &lt; c &lt; 1 → 2b개 &nbsp;/&nbsp; c = −1 → b개 &nbsp;/&nbsp; |c| &gt; 1 → 0개</p><p><span class="step">③ 첫 번째 인수.</span> <span class="m">cos(bπx) = 1/2</span> → 항상 <b>2b개</b>.</p><p><span class="step">④ 두 번째 인수.</span> <span class="m">cos(bπx) = −(a+2)/(2a) = c<sub>2</sub></span>. <span class="m">a &gt; 0</span>이므로 <span class="m">c<sub>2</sub> &lt; 0</span>이고 <span class="m">c<sub>2</sub> ≠ 1/2</span>이라 겹치는 근은 없다.</p><p class="m">c<sub>2</sub> ≥ −1 ⟺ (a+2)/(2a) ≤ 1 ⟺ a ≥ 2</p><p><span class="step">⑤ 경우를 나눈다.</span></p><p class="m">a &lt; 2 : c<sub>2</sub> &lt; −1 → 총 2b = 15 (불가, 짝수)</p><p class="m">a &gt; 2 : −1 &lt; c<sub>2</sub> &lt; 0 → 총 4b = 15 (불가)</p><p class="m">a = 2 : c<sub>2</sub> = −1 → 총 2b + b = 3b = 15 → b = 5</p><p class="m">a + b = 2 + 5 = 7</p>

## 함정

<b>15가 홀수라는 것 자체가 결정적인 단서</b>다. 일반적인 경우는 모두 짝수가 나오므로, 홀수를 만들 수 있는 예외(<span class='m'>cos = ±1</span>, 즉 접하는 경우)를 찾아야 한다는 신호다.

## 노하우

<b>삼각방정식의 실근 개수는 &lsquo;구간이 몇 주기인가 × 한 주기당 몇 개인가&rsquo;로 센다.</b> <span class='m'>cos u = c</span>는 한 주기에 <b>보통 2개</b>지만 <span class='m'>c = ±1</span>이면 <b>1개(접점)</b>가 된다. 개수가 홀수로 주어지면 거의 항상 이 접점 경우를 묻는 것이다.
