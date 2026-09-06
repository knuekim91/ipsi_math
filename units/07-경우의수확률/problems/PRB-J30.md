---
id: PRB-J30
unit: 07-경우의수확률
topic: 이웃하지 않는 배열
level: 4점
difficulty: 상
source: 2027-06모평 30번
exam: 2027-06모평
origin: 기출
core: "검은 공으로 칸을 만들면 각 칸에는 한 색만 들어갈 수 있다"
tags: [이웃하지않게,같은것이있는순열,조합]
status: seed
added: 2026-09-06
answer: 780
---

## 문제

<p>노란색 공 4개, 보라색 공 4개, 검은색 공 4개가 있다. 이 12개의 공을 모두 일렬로 나열할 때, 노란색 공이 보라색 공과 이웃하지 않게 나열하는 경우의 수를 구하시오. (단, 같은 색 공끼리는 서로 구별하지 않는다.)</p>

## 발상

<b>검은 공 4개를 먼저 세워 놓으면 5개의 칸이 생긴다.</b> 한 칸 안에 노란 공과 보라색 공이 함께 들어가면 그 안에서 반드시 이웃하게 되므로, <b>각 칸은 노란색 전용이거나 보라색 전용이거나 비어 있어야 한다.</b> 이 한 문장이 문제를 통째로 바꾼다.

## 풀이

<p><span class="step">① 제3의 색으로 칸을 만든다.</span>
&lsquo;노란 공과 보라 공이 이웃하지 않게&rsquo;라는 조건이므로
<b>둘을 갈라놓을 것</b>이 필요하다. 그 역할을 검은 공이 한다.
검은 공 <span class="m">4</span>개를 먼저 늘어놓으면 그 사이와 양 끝에 자리가 생긴다.</p>
<p class="slot">▢ ● ▢ ● ▢ ● ▢ ● ▢ &nbsp;&nbsp;<span>(● = 검은 공, ▢ = 칸 5개)</span></p>
<p>칸은 모두 <span class="m">5</span>개다.</p>

<p><span class="step">② 한 칸에 두 색을 섞을 수 없음을 확인한다.</span>
어떤 칸에 노란 공과 보라 공을 함께 넣으면,
그 칸 안에서 <b>둘이 반드시 맞닿게</b> 된다. 사이에 검은 공이 없기 때문이다.
그러므로 <b>각 칸은 노란색 전용이거나 보라색 전용이거나 비어 있어야</b> 한다.
이 한 문장이 문제를 통째로 바꾼다.</p>

<p><span class="step">③ 문제를 두 단계로 나눈다.</span>
<b>(1단계)</b> <span class="m">5</span>개의 칸 중 노란색이 들어갈 칸 <span class="m">i</span>개와
보라색이 들어갈 칸 <span class="m">j</span>개를 서로 겹치지 않게 고른다.
<b>(2단계)</b> 고른 칸에 공을 하나도 빠짐없이 나눠 넣는다.</p>
<p>고른 칸은 &lsquo;쓰는 칸&rsquo;이므로 <b>각 칸에 최소 1개는 들어가야</b> 한다.
<span class="m">4</span>개의 공을 <span class="m">i</span>개의 칸에 양의 개수로 나누는 방법은
칸막이를 <span class="m">3</span>개의 틈에 <span class="m">i−1</span>개 놓는 것이므로</p>
<p class="m"><sub>3</sub>C<sub>i−1</sub></p>

<p><span class="step">④ 식을 세운다.</span></p>
<p class="m">Σ<sub>i</sub> Σ<sub>j</sub> <sub>5</sub>C<sub>i</sub> × <sub>5−i</sub>C<sub>j</sub> × <sub>3</sub>C<sub>i−1</sub> × <sub>3</sub>C<sub>j−1</sub></p>

<p><span class="step">⑤ 보라색 쪽을 먼저 정리한다.</span>
노란색이 <span class="m">i</span>개의 칸을 쓰면 남은 칸은 <span class="m">R = 5 − i</span>개다.
그 <span class="m">R</span>개 중에서 보라색이 쓸 칸을 고르고 나누는 경우의 수를
<span class="m">R</span>별로 미리 계산해 둔다.
(<span class="m"><sub>3</sub>C<sub>0</sub>, <sub>3</sub>C<sub>1</sub>, <sub>3</sub>C<sub>2</sub>, <sub>3</sub>C<sub>3</sub></span>은 차례로
<span class="m">1, 3, 3, 1</span>이다.)</p>
<p class="m">R = 4 : 4×1 + 6×3 + 4×3 + 1×1 = 4 + 18 + 12 + 1 = 35</p>
<p class="m">R = 3 : 3×1 + 3×3 + 1×3 = 3 + 9 + 3 = 15</p>
<p class="m">R = 2 : 2×1 + 1×3 = 2 + 3 = 5</p>
<p class="m">R = 1 : 1×1 = 1</p>

<p><span class="step">⑥ 노란색 쪽도 계산한다.</span></p>
<p class="m">i = 1 : <sub>5</sub>C<sub>1</sub> × <sub>3</sub>C<sub>0</sub> = 5 × 1 = 5 &nbsp; (R = 4)</p>
<p class="m">i = 2 : <sub>5</sub>C<sub>2</sub> × <sub>3</sub>C<sub>1</sub> = 10 × 3 = 30 &nbsp; (R = 3)</p>
<p class="m">i = 3 : <sub>5</sub>C<sub>3</sub> × <sub>3</sub>C<sub>2</sub> = 10 × 3 = 30 &nbsp; (R = 2)</p>
<p class="m">i = 4 : <sub>5</sub>C<sub>4</sub> × <sub>3</sub>C<sub>3</sub> = 5 × 1 = 5 &nbsp; (R = 1)</p>

<p><span class="step">⑦ 짝지어 곱하고 더한다.</span></p>
<p class="m">5 × 35 + 30 × 15 + 30 × 5 + 5 × 1</p>
<p class="m">= 175 + 450 + 150 + 5 = 780</p>
<p class="m">답 780</p>

## 함정

<b>&lsquo;각 칸에 한 색만&rsquo;이라는 것을 놓치면 안 된다.</b> 한 칸에 노랑과 보라를 섞어 넣으면 그 칸 안에서 둘이 반드시 붙는다. 또 <b>칸을 고른 뒤 공을 나눌 때 빈 칸이 생기면 안 된다</b> — 고른 칸은 이미 &lsquo;쓰는 칸&rsquo;이므로 각 칸에 최소 1개씩 들어가야 하고, 그래서 <span class='m'><sub>3</sub>C<sub>i−1</sub></span>(중복 없는 양의 정수 분할)이 된다.

## 노하우

<b>&lsquo;A와 B가 이웃하지 않게&rsquo;는 제3의 것으로 칸을 만들어 갈라놓는다.</b> 여기서는 검은 공이 그 역할이다. 그리고 <b>칸 하나에는 한 종류만</b>이라는 제약을 알아내면 &lsquo;칸을 색깔별로 배정 → 각 색을 칸에 양수로 분배&rsquo;라는 2단 구조가 나온다. <b>4를 i개의 양의 정수로 쪼개는 방법은 <span class='m'><sub>3</sub>C<sub>i−1</sub></span></b> (칸막이를 3개의 틈에 놓는다)는 공식을 외워 두면 이런 문제가 계산 문제로 바뀐다.
