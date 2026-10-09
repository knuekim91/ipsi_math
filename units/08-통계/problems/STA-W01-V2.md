---
id: STA-W01-V2
parent: STA-W01
unit: 08-통계
topic: 멈추는 시행의 횟수와 기댓값
level: 4점
difficulty: 상
source: 자체 개발 (STA-W01 변형 · 작은 수가 많은 경우)
origin: 유사문항
core: "작은 수가 많아지면 천천히 올라가 X가 커지는 쪽으로 쏠린다. 상태 추적의 틀은 그대로이고 쏠리는 방향만 반대다"
tags: [이산확률변수,기댓값,시행,상태추적,누적합]
status: variant
added: 2026-10-09
answer: 80
---

## 문제

<p>숫자 <span class="m">1, 1, 1, 1, 2, 3</span>이 하나씩 적혀 있는
<span class="m">6</span>장의 카드가 들어 있는 주머니가 있다.
이 주머니에서 임의로 <span class="m">1</span>장의 카드를 꺼내어
카드에 적힌 수를 확인한 후 다시 넣는 시행을 한다.
이 시행을 반복하여 확인한 모든 수의 합이
<b>처음으로 <span class="m">4</span> 이상이 되면</b> 이 시행을 멈춘다.
시행을 멈출 때까지 시행을 반복한 횟수를 확률변수
<span class="m">X</span>라 할 때,
<span class="m">E(27X)</span>의 값을 구하시오.</p>

## 발상

<b>이번에는 <span class="m">1</span>이 네 장으로 가장 많다.</b>
작은 수가 자주 나오면 합이 천천히 올라가므로,
<b><span class="m">X</span>가 큰 쪽으로 쏠린다.</b>
원본이나 앞 문항과 반대 방향이다.<br><br>

<b>틀은 똑같다.</b> 살아남는 상태는 합이
<span class="m">1, 2, 3</span>인 세 가지이고
<span class="m">X</span>는 <span class="m">2, 3, 4</span> 중 하나다.
<b>달라지는 것은 각 상태에 머무를 확률의 크기뿐</b>이다.<br><br>

<b>특히 합이 <span class="m">1</span>인 상태가 두꺼워진다.</b>
합 <span class="m">1</span>에서 멈추려면 <span class="m">3</span>이 나와야 하는데
그 확률이 <span class="m">1/6</span>로 작다.
<b>그래서 합 <span class="m">1</span>에 머물던 확률이 계속 흘러 내려가
<span class="m">X = 4</span>가 꽤 커진다.</b>

## 풀이

<p><span class="step">① 한 번의 시행에서의 확률을 적는다.</span>
<span class="m">1</span>이 네 장, <span class="m">2</span>와
<span class="m">3</span>이 각각 한 장이다.</p>
<p class="m">P(1) = 4/6 = 2/3, &nbsp; P(2) = 1/6, &nbsp; P(3) = 1/6</p>

<p><span class="step">② X의 범위를 정한다.</span></p>
<p class="m">X = 2, 3, 4</p>

<p><span class="step">③ 1번 시행 뒤의 상태와 멈출 확률을 적는다.</span></p>
<p class="m">합 1 : 2/3 &nbsp;/&nbsp; 합 2 : 1/6 &nbsp;/&nbsp; 합 3 : 1/6</p>
<p>각 상태에서 다음 한 번에 멈출 확률은 다음과 같다.</p>
<p class="m">합 1 → 3이 필요 : 1/6</p>
<p class="m">합 2 → 2 또는 3 : 1/6 + 1/6 = 1/3</p>
<p class="m">합 3 → 무엇이든 : 1</p>

<p><span class="step">④ P(X = 2)를 구한다.</span></p>
<p class="m">P(X = 2) = (2/3)(1/6) + (1/6)(1/3) + (1/6)(1)</p>
<p class="m">= 1/9 + 1/18 + 1/6</p>
<p>분모를 <span class="m">18</span>로 통일한다.</p>
<p class="m">= 2/18 + 1/18 + 3/18 = 6/18 = 1/3</p>

<p><span class="step">⑤ 2번 시행 뒤의 상태를 구한다.</span>
합 <span class="m">2</span>는 <span class="m">1</span>에서
<span class="m">1</span>을 더한 것뿐이고, 합 <span class="m">3</span>은
<span class="m">1</span>에서 <span class="m">2</span>를 더하거나
<span class="m">2</span>에서 <span class="m">1</span>을 더한 것이다.</p>
<p class="m">합 2 : (2/3)(2/3) = 4/9</p>
<p class="m">합 3 : (2/3)(1/6) + (1/6)(2/3) = 1/9 + 1/9 = 2/9</p>

<p><span class="step">⑥ P(X = 3)을 구한다.</span></p>
<p class="m">P(X = 3) = (4/9)(1/3) + (2/9)(1) = 4/27 + 6/27 = 10/27</p>

<p><span class="step">⑦ P(X = 4)를 구한다.</span>
<span class="m">3</span>번 뽑아 합이 <span class="m">3</span> 이하인 것은
<span class="m">1</span>을 세 번 뽑은 경우뿐이다.</p>
<p class="m">P(X = 4) = (2/3)<sup>3</sup> = 8/27</p>
<p>확률의 합을 확인한다.</p>
<p class="m">1/3 + 10/27 + 8/27 = 9/27 + 10/27 + 8/27 = 27/27 = 1</p>

<p><span class="step">⑧ 기댓값을 구하고 답을 만든다.</span></p>
<p class="m">E(X) = 2 × 1/3 + 3 × 10/27 + 4 × 8/27</p>
<p class="m">= 18/27 + 30/27 + 32/27 = 80/27</p>
<p class="m">E(27X) = 80</p>
<p class="m">답 80</p>

## 함정

<b>합 <span class="m">1</span>에서 멈출 확률을 <span class="m">1/3</span>로 보면 안 된다.</b>
합이 <span class="m">1</span>일 때 <span class="m">4</span>에 닿으려면
<span class="m">3</span>이 나와야 하는데, 여기서
<span class="m">3</span>은 한 장뿐이라 <span class="m">1/6</span>이다.
<b>&lsquo;얼마가 더 필요한가&rsquo;를 보고 그 수가 나올 확률을 그 문제의 카드로 세야</b> 한다.<br><br>

<b><span class="m">P(X = 4)</span>를 빠뜨리기 쉽다.</b>
원본에서는 <span class="m">1/8</span>로 작았지만 여기서는
<span class="m">8/27 ≒ 0.30</span>으로 꽤 크다.
<b><span class="m">1</span>이 네 장이라 세 번 연속 뽑힐 확률이 높기 때문</b>이다.
작다고 넘겨짚고 버리면 답이 크게 틀어진다.

## 노하우

<b>작은 수가 많으면 <span class="m">X</span>가 커진다.</b>
세 문항의 답을 늘어놓으면 방향이 보인다.</p>
<p class="m">각 2장씩 64/27 ≒ 2.37 &lt; 원본 65/24 ≒ 2.71 &lt; 1이 4장 80/27 ≒ 2.96</p>
<p><b>큰 수가 잘 나오면 빨리 멈추고, 작은 수가 잘 나오면 늦게 멈춘다.</b>
계산을 끝낸 뒤 이 방향이 맞는지 보면 실수를 잡을 수 있다.<br><br>

<b>가장 느린 경로가 <span class="m">X</span>의 최댓값을 정한다.</b>
<span class="m">1</span>만 계속 뽑는 것이 가장 느리고,
그 확률이 <span class="m">P(X = 4)</span>를 거의 다 만든다.
<b>작은 수가 많을수록 이 경로가 두꺼워진다</b>는 것을 기억해 두면
답의 크기를 미리 가늠할 수 있다.
