---
id: STA-W01
unit: 08-통계
topic: 멈추는 시행의 횟수와 기댓값
level: 4점
difficulty: 상
source: 2027 설맞이 아카이브 57번
exam: 오답노트
origin: 기출
core: "멈추지 않고 살아남는 상태는 누적합 1, 2, 3 뿐이다. 뽑은 수의 순서를 나열하지 말고 이 세 상태의 확률만 단계마다 갱신한다"
tags: [이산확률변수,기댓값,시행,상태추적,누적합]
status: wrong
added: 2026-10-09
answer: 130
---

## 문제

<p>숫자 <span class="m">1, 1, 1, 2, 2, 3</span>이 하나씩 적혀 있는
<span class="m">6</span>장의 카드가 들어 있는 주머니가 있다.
이 주머니에서 임의로 <span class="m">1</span>장의 카드를 꺼내어
카드에 적힌 수를 확인한 후 다시 넣는 시행을 한다.
이 시행을 반복하여 확인한 모든 수의 합이
<b>처음으로 <span class="m">4</span> 이상이 되면</b> 이 시행을 멈춘다.
시행을 멈출 때까지 시행을 반복한 횟수를 확률변수
<span class="m">X</span>라 할 때,
<span class="m">E(48X)</span>의 값을 구하시오.</p>

## 발상

<b>뽑은 수의 순서를 하나하나 적어 나가면 금방 감당이 안 된다.</b>
시행마다 <span class="m">3</span>가지가 갈라지므로
<span class="m">4</span>번이면 경우가 <span class="m">81</span>가지가 된다.
<b>세어야 할 것은 순서가 아니라 &lsquo;지금까지의 합&rsquo;뿐</b>이다.<br><br>

<b>살아남는 상태가 몇 개 안 된다는 것이 열쇠다.</b>
합이 <span class="m">4</span> 이상이면 그 자리에서 멈추므로,
<b>계속 이어지는 상태는 합이 <span class="m">1, 2, 3</span>인 세 가지뿐</b>이다.
어떤 순서로 그 합에 닿았는지는 앞으로 일어날 일에 아무 영향이 없다.
그러므로 <b>세 상태의 확률만 단계마다 갱신</b>하면 된다.<br><br>

<b>먼저 <span class="m">X</span>가 가질 수 있는 값의 범위를 잡아 둔다.</b>
한 번에 얻는 수는 많아야 <span class="m">3</span>이므로 한 번으로는
<span class="m">4</span>에 닿을 수 없어 <span class="m">X ≥ 2</span>이고,
가장 느린 경우가 <span class="m">1</span>을 네 번 뽑는 것이므로
<span class="m">X ≤ 4</span>이다. 곧 <span class="m">X</span>는
<span class="m">2, 3, 4</span> 중 하나다.

## 풀이

<p><span class="step">① 한 번의 시행에서 각 수가 나올 확률을 적는다.</span>
카드는 <span class="m">1</span>이 <span class="m">3</span>장,
<span class="m">2</span>가 <span class="m">2</span>장,
<span class="m">3</span>이 <span class="m">1</span>장이고 매번 다시 넣으므로
시행마다 확률이 같다.</p>
<p class="m">P(1) = 3/6 = 1/2, &nbsp; P(2) = 2/6 = 1/3, &nbsp; P(3) = 1/6</p>

<p><span class="step">② X의 범위를 정한다.</span>
한 번에 얻는 수는 많아야 <span class="m">3</span>이므로
<span class="m">1</span>번 만에 합이 <span class="m">4</span> 이상이 될 수 없다.
또 <span class="m">1</span>을 네 번 뽑으면 합이 <span class="m">4</span>가 되므로
늦어도 <span class="m">4</span>번째에는 멈춘다.</p>
<p class="m">X = 2, 3, 4</p>

<p><span class="step">③ 1번 시행 뒤의 상태를 적는다.</span>
어떤 수가 나와도 합이 <span class="m">3</span> 이하라 멈추지 않는다.
<b>이 세 줄이 앞으로 쓸 표의 첫 줄이다.</b></p>
<p class="m">합 1 : 1/2 &nbsp;/&nbsp; 합 2 : 1/3 &nbsp;/&nbsp; 합 3 : 1/6</p>

<p><span class="step">④ 각 상태에서 멈출 확률을 구해 둔다.</span>
다음 한 번으로 합이 <span class="m">4</span> 이상이 되려면
얼마가 더 필요한지만 보면 된다.</p>
<p class="m">합 1 → 3이 나와야 한다 : 1/6</p>
<p class="m">합 2 → 2 또는 3 : 1/3 + 1/6 = 1/2</p>
<p class="m">합 3 → 무엇이든 : 1</p>

<p><span class="step">⑤ P(X = 2)를 구한다.</span>
<span class="m">2</span>번째에 멈춘다는 것은
<span class="m">1</span>번 시행 뒤의 상태에서 곧바로 멈춘다는 뜻이다.
③의 확률에 ④의 확률을 곱해 더한다.</p>
<p class="m">P(X = 2) = (1/2)(1/6) + (1/3)(1/2) + (1/6)(1)</p>
<p class="m">= 1/12 + 1/6 + 1/6 = 1/12 + 4/12 = 5/12</p>

<p><span class="step">⑥ 2번 시행 뒤의 상태를 구한다.</span>
멈추지 않고 남은 경우만 모은다. 합이 <span class="m">2</span>가 되려면
<span class="m">1</span>에서 <span class="m">1</span>을 더한 것뿐이고,
합이 <span class="m">3</span>이 되려면 <span class="m">1</span>에서
<span class="m">2</span>를 더하거나 <span class="m">2</span>에서
<span class="m">1</span>을 더한 것이다.</p>
<p class="m">합 2 : (1/2)(1/2) = 1/4</p>
<p class="m">합 3 : (1/2)(1/3) + (1/3)(1/2) = 1/6 + 1/6 = 1/3</p>

<p><span class="step">⑦ P(X = 3)을 구한다.</span>
⑥의 상태에서 ④의 확률로 멈춘다.</p>
<p class="m">P(X = 3) = (1/4)(1/2) + (1/3)(1) = 1/8 + 1/3</p>
<p class="m">= 3/24 + 8/24 = 11/24</p>

<p><span class="step">⑧ P(X = 4)를 구한다.</span>
<span class="m">3</span>번 시행 뒤에도 안 멈추려면 합이
<span class="m">3</span> 이하여야 하는데, 세 번 뽑아 합이
<span class="m">3</span> 이하인 것은 <span class="m">1</span>을 세 번 뽑은 경우뿐이다.
그때 합이 <span class="m">3</span>이므로 네 번째에는 반드시 멈춘다.</p>
<p class="m">P(X = 4) = (1/2)<sup>3</sup> × 1 = 1/8</p>
<p>세 확률을 더해 <span class="m">1</span>이 되는지 확인한다.</p>
<p class="m">5/12 + 11/24 + 1/8 = 10/24 + 11/24 + 3/24 = 24/24 = 1</p>

<p><span class="step">⑨ 기댓값을 구한다.</span></p>
<p class="m">E(X) = 2 × 5/12 + 3 × 11/24 + 4 × 1/8</p>
<p class="m">= 10/12 + 33/24 + 1/2 = 20/24 + 33/24 + 12/24 = 65/24</p>

<p><span class="step">⑩ 답을 만든다.</span>
<span class="m">E(aX) = aE(X)</span>이므로 그대로 곱한다.</p>
<p class="m">E(48X) = 48 × 65/24 = 2 × 65 = 130</p>
<p class="m">답 130</p>

## 함정

<b>뽑은 수의 순서를 전부 나열하려 들면 시간을 잃는다.</b>
<span class="m">X = 3</span>인 경우만 해도
<span class="m">(1,1,⋯), (1,2,⋯), (2,1,⋯)</span>로 갈라지고
각각 뒤에 올 수가 또 갈라진다.
<b>&lsquo;어떤 순서로 왔는가&rsquo;는 앞으로 일어날 일에 영향을 주지 않는다.</b>
오직 <b>지금까지의 합</b>만 보면 된다.<br><br>

<b><span class="m">X = 1</span>을 넣으면 안 된다.</b>
한 번에 얻는 수는 많아야 <span class="m">3</span>이라
<span class="m">1</span>번 만에 <span class="m">4</span>에 닿을 수 없다.
<b>범위를 먼저 잡아 두면 나중에 빠뜨리거나 더 세는 일이 없다.</b><br><br>

<b>&lsquo;<span class="m">4</span> 이상&rsquo;이지 &lsquo;<span class="m">4</span>&rsquo;가 아니다.</b>
합이 <span class="m">5</span>나 <span class="m">6</span>이 되어도 멈춘다.
합이 정확히 <span class="m">4</span>가 되는 경우만 세면 전부 틀린다.<br><br>

<b>확률의 합이 <span class="m">1</span>인지 꼭 확인한다.</b>
<span class="m">5/12 + 11/24 + 1/8 = 1</span>이 맞아야 세 확률이 모두 옳다.
이 한 줄이 가장 빠른 검산이다.

## 노하우

<b>&lsquo;어떤 조건이 되면 멈춘다&rsquo;는 시행은 상태를 따라간다.</b>
멈추지 않고 살아남는 상태가 몇 개인지 먼저 세어 본다.
이 문제에서는 합이 <span class="m">1, 2, 3</span>인 세 가지뿐이었다.
<b>상태가 적으면 표 하나로 끝난다.</b><br><br>

<b>표는 두 줄씩 짝지어 쓴다.</b>
한 줄은 <b>&lsquo;그 상태에 있을 확률&rsquo;</b>,
다음 줄은 <b>&lsquo;그 상태에서 멈출 확률&rsquo;</b>이다.
둘을 곱해 더하면 그 단계에서 멈출 확률이 되고,
안 멈춘 쪽은 다음 상태로 넘긴다.
<span class="m">P(X = k)</span>를 따로따로 구하는 것이 아니라
<b>한 번 내려가며 한꺼번에</b> 구하는 것이다.<br><br>

<b>범위를 먼저 잡는다.</b>
가장 빠른 경우와 가장 느린 경우를 생각하면
<span class="m">X</span>가 가질 수 있는 값이 정해진다.
가장 느린 경우는 보통 <b>가장 작은 수만 계속 뽑는 것</b>이다.<br><br>

<b>검산 한 가지를 더 알아 두면 좋다.</b>
<span class="m">P(X ≥ k)</span>는 <span class="m">k − 1</span>번 시행 뒤에도
안 멈췄을 확률, 곧 <b>그 단계에서 살아남은 상태들의 확률의 합</b>이다.
여기서는 <span class="m">1, 1, 7/12, 1/8</span>이고 이것을 모두 더하면
<span class="m">65/24</span>로 <span class="m">E(X)</span>와 같아진다.
시험장에서 답을 빠르게 다시 확인할 때 쓸 수 있다.
