---
id: STA-W01-V1
parent: STA-W01
unit: 08-통계
topic: 멈추는 시행의 횟수와 기댓값
level: 4점
difficulty: 상
source: 자체 개발 (STA-W01 변형 · 카드 구성을 고르게)
origin: 유사문항
core: "세 수가 똑같이 1/3로 나오면 상태 확률이 분모 3의 거듭제곱으로만 쌓여 표 갱신이 한결 가벼워진다"
tags: [이산확률변수,기댓값,시행,상태추적,누적합]
status: variant
added: 2026-10-09
answer: 64
---

## 문제

<p>숫자 <span class="m">1, 1, 2, 2, 3, 3</span>이 하나씩 적혀 있는
<span class="m">6</span>장의 카드가 들어 있는 주머니가 있다.
이 주머니에서 임의로 <span class="m">1</span>장의 카드를 꺼내어
카드에 적힌 수를 확인한 후 다시 넣는 시행을 한다.
이 시행을 반복하여 확인한 모든 수의 합이
<b>처음으로 <span class="m">4</span> 이상이 되면</b> 이 시행을 멈춘다.
시행을 멈출 때까지 시행을 반복한 횟수를 확률변수
<span class="m">X</span>라 할 때,
<span class="m">E(27X)</span>의 값을 구하시오.</p>

## 발상

<b>멈추는 규칙은 그대로이고 카드 구성만 고르게 바뀌었다.</b>
<span class="m">1, 2, 3</span>이 각각 두 장씩이므로
세 수가 모두 <span class="m">1/3</span>로 나온다.<br><br>

<b>구조가 같으니 풀이의 틀도 똑같다.</b>
살아남는 상태는 여전히 합이
<span class="m">1, 2, 3</span>인 세 가지뿐이고,
<span class="m">X</span>는 <span class="m">2, 3, 4</span> 중 하나다.<br><br>

<b>달라지는 것은 숫자가 가벼워진다는 점이다.</b>
모든 확률이 <span class="m">1/3</span>의 거듭제곱으로만 쌓이므로
분모가 <span class="m">3, 9, 27, 81</span>로 단정하게 간다.
<b>원본에서 분모가 <span class="m">12, 24</span>로 지저분했던 것은
카드 수가 <span class="m">3 : 2 : 1</span>로 치우쳤기 때문</b>이었다.

## 풀이

<p><span class="step">① 한 번의 시행에서의 확률을 적는다.</span>
각 수가 두 장씩이므로 모두 같다.</p>
<p class="m">P(1) = P(2) = P(3) = 2/6 = 1/3</p>

<p><span class="step">② X의 범위를 정한다.</span>
한 번에 많아야 <span class="m">3</span>이므로 한 번으로는 못 멈추고,
<span class="m">1</span>을 네 번 뽑으면 합이 <span class="m">4</span>가 된다.</p>
<p class="m">X = 2, 3, 4</p>

<p><span class="step">③ 1번 시행 뒤의 상태와 멈출 확률을 적는다.</span>
어떤 수가 나와도 합이 <span class="m">3</span> 이하라 멈추지 않는다.</p>
<p class="m">합 1 : 1/3 &nbsp;/&nbsp; 합 2 : 1/3 &nbsp;/&nbsp; 합 3 : 1/3</p>
<p>각 상태에서 다음 한 번에 멈출 확률은 다음과 같다.</p>
<p class="m">합 1 → 3이 필요 : 1/3</p>
<p class="m">합 2 → 2 또는 3 : 2/3</p>
<p class="m">합 3 → 무엇이든 : 1</p>

<p><span class="step">④ P(X = 2)를 구한다.</span></p>
<p class="m">P(X = 2) = (1/3)(1/3) + (1/3)(2/3) + (1/3)(1)</p>
<p class="m">= 1/9 + 2/9 + 3/9 = 6/9 = 2/3</p>

<p><span class="step">⑤ 2번 시행 뒤의 상태를 구한다.</span>
멈추지 않고 남은 경우만 모은다.</p>
<p class="m">합 2 : (1/3)(1/3) = 1/9</p>
<p class="m">합 3 : (1/3)(1/3) + (1/3)(1/3) = 2/9</p>

<p><span class="step">⑥ P(X = 3)을 구한다.</span></p>
<p class="m">P(X = 3) = (1/9)(2/3) + (2/9)(1) = 2/27 + 6/27 = 8/27</p>

<p><span class="step">⑦ P(X = 4)를 구한다.</span>
<span class="m">3</span>번 뽑아 합이 <span class="m">3</span> 이하인 것은
<span class="m">1</span>을 세 번 뽑은 경우뿐이고, 그때 네 번째에는 반드시 멈춘다.</p>
<p class="m">P(X = 4) = (1/3)<sup>3</sup> = 1/27</p>
<p>확률의 합을 확인한다.</p>
<p class="m">2/3 + 8/27 + 1/27 = 18/27 + 8/27 + 1/27 = 27/27 = 1</p>

<p><span class="step">⑧ 기댓값을 구하고 답을 만든다.</span></p>
<p class="m">E(X) = 2 × 2/3 + 3 × 8/27 + 4 × 1/27</p>
<p class="m">= 36/27 + 24/27 + 4/27 = 64/27</p>
<p class="m">E(27X) = 27 × 64/27 = 64</p>
<p class="m">답 64</p>

## 함정

<b>&lsquo;각 수가 두 장씩&rsquo;을 <span class="m">1/2</span>로 읽으면 안 된다.</b>
카드가 여섯 장이고 같은 수가 두 장이므로 <span class="m">2/6 = 1/3</span>이다.
<b>분모는 언제나 전체 카드 수</b>다.<br><br>

<b>원본보다 답이 작아진 것이 맞는지 확인한다.</b>
원본은 <span class="m">E(X) = 65/24 ≒ 2.71</span>이고 여기서는
<span class="m">64/27 ≒ 2.37</span>로 더 작다.
<b>큰 수가 나올 확률이 커져서 더 빨리 멈추기 때문</b>이다.
원본에서 <span class="m">3</span>이 나올 확률은 <span class="m">1/6</span>이었는데
여기서는 <span class="m">1/3</span>로 두 배다.
<b>답이 움직이는 방향이 말이 되는지 보는 것</b>이 좋은 검산이다.

## 노하우

<b>구조가 같은 문제를 만나면 틀을 그대로 가져온다.</b>
살아남는 상태를 적고, 상태별 멈출 확률을 적고, 둘을 곱해 더한다.
<b>바뀐 것은 숫자뿐이므로 새로 생각할 것이 없다.</b>
같은 유형을 두세 번 풀어 이 틀이 손에 붙으면
시험장에서 <span class="m">3</span>분이면 끝난다.<br><br>

<b>확률이 고를수록 분모가 깔끔해진다.</b>
세 수가 모두 <span class="m">1/3</span>이면 분모는
<span class="m">3</span>의 거듭제곱으로만 간다.
문제가 <span class="m">E(27X)</span>를 물은 것은
<span class="m">E(X)</span>의 분모가 <span class="m">27</span>이기 때문이다.
<b>곱하라는 수를 보고 분모를 짐작</b>할 수 있으면
계산이 맞게 가고 있는지 중간에 확인할 수 있다.
