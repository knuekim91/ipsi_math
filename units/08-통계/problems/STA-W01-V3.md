---
id: STA-W01-V3
parent: STA-W01
unit: 08-통계
topic: 멈추는 시행의 횟수와 기댓값
level: 4점
difficulty: 상
source: 자체 개발 (STA-W01 변형 · 멈춤 기준을 5로)
origin: 유사문항
core: "멈춤 기준이 1 올라가면 살아남는 상태가 합 4까지 넷으로 늘어난다. 상태가 늘어도 표를 한 줄 더 쓰면 그만이다"
tags: [이산확률변수,기댓값,시행,상태추적,누적합]
status: variant
added: 2026-10-09
answer: 475
---

## 문제

<p>숫자 <span class="m">1, 1, 1, 2, 2, 3</span>이 하나씩 적혀 있는
<span class="m">6</span>장의 카드가 들어 있는 주머니가 있다.
이 주머니에서 임의로 <span class="m">1</span>장의 카드를 꺼내어
카드에 적힌 수를 확인한 후 다시 넣는 시행을 한다.
이 시행을 반복하여 확인한 모든 수의 합이
<b>처음으로 <span class="m">5</span> 이상이 되면</b> 이 시행을 멈춘다.
시행을 멈출 때까지 시행을 반복한 횟수를 확률변수
<span class="m">X</span>라 할 때,
<span class="m">E(144X)</span>의 값을 구하시오.</p>

## 발상

<b>카드는 원본과 같고 멈춤 기준만 <span class="m">4</span>에서
<span class="m">5</span>로 올라갔다.</b>
그런데 이 한 칸이 문제를 눈에 띄게 무겁게 만든다.<br><br>

<b>살아남는 상태가 하나 늘어난다.</b>
이제 합이 <span class="m">1, 2, 3, 4</span>이면 아직 안 멈추므로
따라가야 할 상태가 <b>넷</b>이다.
<span class="m">X</span>의 범위도 늘어 <span class="m">1</span>을
다섯 번 뽑는 경우까지 생기므로 <span class="m">X ≤ 5</span>이다.<br><br>

<b>그래도 방법은 똑같다.</b>
상태를 적고, 상태마다 멈출 확률을 적고, 곱해서 더한다.
<b>표를 한 줄 더 쓰면 그만</b>이다.
상태를 따라가는 방식의 장점이 여기서 드러난다.
순서를 나열하는 방식이었다면 경우가
<span class="m">3<sup>5</sup> = 243</span>가지로 폭발한다.

## 풀이

<p><span class="step">① 확률과 범위를 적는다.</span></p>
<p class="m">P(1) = 1/2, &nbsp; P(2) = 1/3, &nbsp; P(3) = 1/6</p>
<p>한 번에 많아야 <span class="m">3</span>이므로 한 번으로는 못 멈추고,
<span class="m">1</span>을 다섯 번 뽑으면 합이 <span class="m">5</span>가 된다.</p>
<p class="m">X = 2, 3, 4, 5</p>

<p><span class="step">② 상태별로 멈출 확률을 미리 적어 둔다.</span>
합이 <span class="m">5</span> 이상이 되려면 얼마가 더 필요한지 본다.</p>
<p class="m">합 1 → 4 이상이 필요한데 최대가 3이다 : 0</p>
<p class="m">합 2 → 3이 나와야 한다 : 1/6</p>
<p class="m">합 3 → 2 또는 3 : 1/2</p>
<p class="m">합 4 → 무엇이든 : 1</p>
<p><b>합이 <span class="m">1</span>이면 다음 한 번으로는 절대 못 멈춘다.</b>
이것이 원본과 가장 다른 점이다.</p>

<p><span class="step">③ 1번 시행 뒤의 상태를 적는다.</span></p>
<p class="m">합 1 : 1/2 &nbsp;/&nbsp; 합 2 : 1/3 &nbsp;/&nbsp; 합 3 : 1/6</p>

<p><span class="step">④ P(X = 2)를 구한다.</span>
합 <span class="m">1</span>에서는 멈출 수 없으므로 두 항만 더한다.</p>
<p class="m">P(X = 2) = (1/3)(1/6) + (1/6)(1/2) = 1/18 + 1/12</p>
<p class="m">= 2/36 + 3/36 = 5/36</p>

<p><span class="step">⑤ 2번 시행 뒤의 상태를 구한다.</span>
안 멈춘 경우를 합이 얼마인지로 모은다.</p>
<p class="m">합 2 : (1/2)(1/2) = 1/4</p>
<p class="m">합 3 : (1/2)(1/3) + (1/3)(1/2) = 1/3</p>
<p class="m">합 4 : (1/2)(1/6) + (1/3)(1/3) + (1/6)(1/2) = 1/12 + 1/9 + 1/12</p>
<p>분모를 <span class="m">36</span>으로 통일한다.</p>
<p class="m">= 3/36 + 4/36 + 3/36 = 10/36 = 5/18</p>

<p><span class="step">⑥ P(X = 3)을 구한다.</span></p>
<p class="m">P(X = 3) = (1/4)(1/6) + (1/3)(1/2) + (5/18)(1)</p>
<p class="m">= 1/24 + 1/6 + 5/18</p>
<p>분모를 <span class="m">72</span>로 통일한다.</p>
<p class="m">= 3/72 + 12/72 + 20/72 = 35/72</p>

<p><span class="step">⑦ 3번 시행 뒤의 상태를 구한다.</span></p>
<p class="m">합 3 : (1/4)(1/2) = 1/8</p>
<p class="m">합 4 : (1/4)(1/3) + (1/3)(1/2) = 1/12 + 1/6 = 1/4</p>

<p><span class="step">⑧ P(X = 4)와 P(X = 5)를 구한다.</span></p>
<p class="m">P(X = 4) = (1/8)(1/2) + (1/4)(1) = 1/16 + 1/4 = 5/16</p>
<p><span class="m">4</span>번 시행 뒤에도 안 멈추려면 합이
<span class="m">4</span>여야 하는데, 그것은
<span class="m">1</span>을 네 번 뽑은 경우뿐이다.</p>
<p class="m">P(X = 5) = (1/2)<sup>4</sup> × 1 = 1/16</p>
<p>확률의 합을 확인한다. 분모를 <span class="m">144</span>로 통일한다.</p>
<p class="m">20/144 + 70/144 + 45/144 + 9/144 = 144/144 = 1</p>

<p><span class="step">⑨ 기댓값을 구하고 답을 만든다.</span></p>
<p class="m">E(X) = 2 × 5/36 + 3 × 35/72 + 4 × 5/16 + 5 × 1/16</p>
<p class="m">= 40/144 + 210/144 + 180/144 + 45/144 = 475/144</p>
<p class="m">E(144X) = 475</p>
<p class="m">답 475</p>

## 함정

<b>합 <span class="m">1</span>에서 멈출 확률이 <span class="m">0</span>이라는 것을 놓치면 안 된다.</b>
한 번에 얻는 수가 많아야 <span class="m">3</span>이므로
<span class="m">1 + 3 = 4 &lt; 5</span>다.
<b>원본에서는 합 <span class="m">1</span>에서도 멈출 수 있었기 때문에</b>
그 감각으로 풀면 <span class="m">P(X = 2)</span>부터 틀린다.<br><br>

<b>상태가 넷이 되었으므로 ⑤에서 세 갈래를 모두 더해야 한다.</b>
합 <span class="m">4</span>에 닿는 길이
<span class="m">1 + 3</span>, <span class="m">2 + 2</span>,
<span class="m">3 + 1</span>로 세 가지다. 하나라도 빠뜨리면
뒤의 모든 값이 어긋난다.<br><br>

<b>분모가 커지므로 통분을 미루지 않는다.</b>
<span class="m">16, 18, 24, 36, 72</span>가 섞여 나오는데,
<b>마지막에 <span class="m">144</span>로 한꺼번에 맞추는 것</b>이
중간에 자꾸 바꾸는 것보다 안전하다.
문제가 <span class="m">E(144X)</span>를 물은 것이
<span class="m">144</span>로 맞추라는 힌트이기도 하다.

## 노하우

<b>멈춤 기준이 <span class="m">m</span>이면 살아남는 상태는
합이 <span class="m">1</span>부터 <span class="m">m − 1</span>까지다.</b>
기준이 올라갈수록 따라갈 줄이 늘어날 뿐,
<b>방법 자체는 조금도 달라지지 않는다.</b>
이것이 상태를 따라가는 방식의 가장 큰 장점이다.<br><br>

<b>어떤 상태에서는 아예 못 멈춘다는 것을 먼저 확인한다.</b>
<b>&lsquo;남은 거리&rsquo;가 한 번에 얻을 수 있는 최댓값보다 크면</b>
그 상태에서 멈출 확률은 <span class="m">0</span>이다.
표를 만들 때 이 칸을 먼저 <span class="m">0</span>으로 채워 두면
쓸데없는 계산을 하지 않는다.<br><br>

<b>곱하라는 수가 분모를 알려 준다.</b>
<span class="m">E(144X)</span>라고 물었으면
<span class="m">E(X)</span>의 분모가 <span class="m">144</span>를 나눈다는 뜻이다.
<b>중간 계산에서 분모가 <span class="m">144</span>와 맞지 않는 수가 나오면
그 자리에서 다시 본다.</b>
