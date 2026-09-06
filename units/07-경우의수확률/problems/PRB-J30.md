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

<p><span class="step">① 칸을 만든다.</span> 검은 공 4개를 놓으면</p><p class="slot">▢ ● ▢ ● ▢ ● ▢ ● ▢ &nbsp;&nbsp;<span>(● = 검은 공, ▢ = 칸 5개)</span></p><p><span class="step">② 각 칸은 한 색만.</span> 노란색을 넣을 칸을 <span class="m">i</span>개, 보라색을 넣을 칸을 <span class="m">j</span>개 고른다 (서로 겹치지 않게).</p><p><span class="step">③ 공을 칸에 나눈다.</span> 노란 공 4개를 <span class="m">i</span>개의 칸에 <b>하나도 빠짐없이</b> 나누는 방법은 <span class="m"><sub>3</sub>C<sub>i−1</sub></span>가지 (4를 <span class="m">i</span>개의 양의 정수로 쪼개기). 보라색도 같다.</p><p><span class="step">④ 센다.</span></p><p class="m">Σ<sub>i</sub> Σ<sub>j</sub> <sub>5</sub>C<sub>i</sub> · <sub>5−i</sub>C<sub>j</sub> · <sub>3</sub>C<sub>i−1</sub> · <sub>3</sub>C<sub>j−1</sub></p><p>먼저 남은 칸 수 <span class="m">R = 5 − i</span>에 대해 보라색 쪽 합을 구해 두면</p><p class="m">R = 4 : 4·1 + 6·3 + 4·3 + 1·1 = 35</p><p class="m">R = 3 : 3·1 + 3·3 + 1·3 = 15</p><p class="m">R = 2 : 2·1 + 1·3 = 5</p><p class="m">R = 1 : 1·1 = 1</p><p>노란색 쪽 <span class="m"><sub>5</sub>C<sub>i</sub> · <sub>3</sub>C<sub>i−1</sub></span>은</p><p class="m">i=1 : 5·1 = 5 &nbsp;/&nbsp; i=2 : 10·3 = 30 &nbsp;/&nbsp; i=3 : 10·3 = 30 &nbsp;/&nbsp; i=4 : 5·1 = 5</p><p><span class="step">⑤ 곱해서 더한다.</span></p><p class="m">5×35 + 30×15 + 30×5 + 5×1 = 175 + 450 + 150 + 5 = 780</p>

## 함정

<b>&lsquo;각 칸에 한 색만&rsquo;이라는 것을 놓치면 안 된다.</b> 한 칸에 노랑과 보라를 섞어 넣으면 그 칸 안에서 둘이 반드시 붙는다. 또 <b>칸을 고른 뒤 공을 나눌 때 빈 칸이 생기면 안 된다</b> — 고른 칸은 이미 &lsquo;쓰는 칸&rsquo;이므로 각 칸에 최소 1개씩 들어가야 하고, 그래서 <span class='m'><sub>3</sub>C<sub>i−1</sub></span>(중복 없는 양의 정수 분할)이 된다.

## 노하우

<b>&lsquo;A와 B가 이웃하지 않게&rsquo;는 제3의 것으로 칸을 만들어 갈라놓는다.</b> 여기서는 검은 공이 그 역할이다. 그리고 <b>칸 하나에는 한 종류만</b>이라는 제약을 알아내면 &lsquo;칸을 색깔별로 배정 → 각 색을 칸에 양수로 분배&rsquo;라는 2단 구조가 나온다. <b>4를 i개의 양의 정수로 쪼개는 방법은 <span class='m'><sub>3</sub>C<sub>i−1</sub></span></b> (칸막이를 3개의 틈에 놓는다)는 공식을 외워 두면 이런 문제가 계산 문제로 바뀐다.
