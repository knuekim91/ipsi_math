---
id: PRB-W01-V4
parent: PRB-W01
unit: 07-경우의수확률
topic: 동전 뒤집기 시행과 뒤집힐 확률
level: 4점
difficulty: 중상
source: 자체 개발 (PRB-W01 변형 · 규칙을 바꾼 경우)
origin: 유사문항
core: "매 시행이 정확히 한 개를 뒤집으므로, 동전마다 '뽑힐 확률'을 먼저 구해 두고 같은 동전이 두 번 나올 확률을 센다"
tags: [확률,시행,독립시행,여사건]
status: variant
added: 2026-09-30
answer: ④
---

## 문제

<p>탁자 위에 <span class="m">6</span>개의 동전이 모두 앞면이 보이도록
일렬로 놓여 있다.
이 <span class="m">6</span>개의 동전과 한 개의 주사위를 사용하여
다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">주사위를 한 번 던져 나온 눈의 수가 k일 때,</span>
<span class="cond m">k가 3의 배수이면 임의로 하나의 동전을 선택하여 한 번 뒤집어 제자리에 놓고,</span>
<span class="cond m">k가 3의 배수가 아니면 k번째 자리의 동전을 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>이 시행을 <span class="m">2</span>번 반복한 후 이
<span class="m">6</span>개의 동전이 모두 같은 면이 보이도록 놓여 있을 확률은?</p>

<div class="choices"><span>① 4/27</span><span>② 1/6</span><span>③ 5/27</span>
<span>④ 11/54</span><span>⑤ 2/9</span></div>

## 발상

<b>규칙이 바뀌었지만 오히려 단순해졌다.
어떤 눈이 나오든 <b>동전은 정확히 한 개만</b> 뒤집힌다.</b><br><br>

그러므로 <span class="m">2</span>번의 시행에서 뒤집기는 모두 두 번이다.
처음에 모두 앞면이었으므로,
<b>모두 뒷면이 되려면 여섯 개를 다 뒤집어야 하는데 두 번으로는 불가능</b>하다.
남는 것은 모두 앞면인 경우뿐이고,
그것은 <b>두 번이 같은 동전을 뒤집어 제자리로 돌아왔다</b>는 뜻이다.<br><br>

<b>그러면 문제는 &lsquo;두 번 모두 같은 동전이 뽑힐 확률&rsquo;로 바뀐다.</b>
그래서 동전마다 <b>한 번의 시행에서 뽑힐 확률</b>을 먼저 구해 두면 된다.
여기에 함정이 하나 있다.
<span class="m">3</span>번째와 <span class="m">6</span>번째 동전은
<b>눈의 수로 직접 지목되지 않는다.</b>
<span class="m">k = 3</span>과 <span class="m">k = 6</span>은
&lsquo;임의로 하나&rsquo; 쪽 규칙으로 가 버리기 때문이다.
<b>여섯 개의 동전이 뽑힐 확률이 서로 같지 않다.</b>

## 풀이

<p><span class="step">① 두 번으로 도달할 수 있는 상태를 따진다.</span>
어떤 눈이 나오든 한 번의 시행은 동전 한 개를 뒤집는다.
<span class="m">2</span>번의 시행에서 바뀔 수 있는 동전은 많아야 두 개이므로,
모두 앞면에서 시작하여 <b>모두 뒷면이 되는 것은 불가능</b>하다.<br>
모두 앞면이 되려면 바뀐 동전이 하나도 없어야 하고,
두 번의 뒤집기가 <b>같은 동전</b>에 일어나야 한다.</p>

<p><span class="step">② 각 동전이 뽑힐 확률을 구한다.</span>
<span class="m">n</span>번째 자리의 동전을 <span class="m">c<sub>n</sub></span>이라 하자.
<span class="m">1</span>부터 <span class="m">6</span>까지의 눈 중
<span class="m">3</span>의 배수는 <span class="m">3</span>과
<span class="m">6</span>의 두 개다.
따라서 &lsquo;임의로 하나&rsquo; 규칙이 쓰일 확률은
<span class="m">2/6 = 1/3</span>이고,
그때 각 동전이 뽑힐 확률은 <span class="m">1/6</span>이다.</p>
<p><span class="m">n</span>이 <span class="m">1, 2, 4, 5</span>인 동전은
<b>두 갈래로</b> 뽑힌다. 눈이 <span class="m">n</span>으로 나오거나,
<span class="m">3</span>의 배수가 나온 뒤 임의로 뽑히는 것이다.</p>
<p class="m">P(c<sub>n</sub>) = 1/6 + (1/3) × (1/6) = 3/18 + 1/18 = 4/18 = 2/9</p>
<p><span class="m">n</span>이 <span class="m">3</span> 또는
<span class="m">6</span>인 동전은 <b>임의로 뽑히는 길밖에 없다.</b></p>
<p class="m">P(c<sub>3</sub>) = P(c<sub>6</sub>) = (1/3) × (1/6) = 1/18</p>
<p>합이 <span class="m">1</span>인지 확인한다.</p>
<p class="m">4 × (2/9) + 2 × (1/18) = 8/9 + 1/9 = 1</p>

<p><span class="step">③ 같은 동전이 두 번 뽑힐 확률을 구한다.</span>
두 번의 시행은 서로 독립이므로, 각 동전마다 확률을 제곱하여 더한다.</p>
<p class="m">4 × (2/9)<sup>2</sup> + 2 × (1/18)<sup>2</sup></p>
<p class="m">= 4 × 4/81 + 2 × 1/324 = 16/81 + 2/324</p>
<p>분모를 <span class="m">324</span>로 통분한다.</p>
<p class="m">= 64/324 + 2/324 = 66/324</p>

<p><span class="step">④ 약분하여 답을 만든다.</span>
분모와 분자를 <span class="m">6</span>으로 나눈다.</p>
<p class="m">66/324 = 11/54</p>
<p class="m">답 ④</p>

## 함정

<b>여섯 개의 동전이 똑같이 뽑힌다고 보면 틀린다.</b>
그렇게 보면 답이
<span class="m">6 × (1/6)<sup>2</sup> = 1/6</span>이 되어 ②를 고르게 된다.
<span class="m">3</span>번째와 <span class="m">6</span>번째 동전은
<b>눈의 수로 직접 지목되지 않으므로 뽑힐 확률이 훨씬 작다.</b>
규칙이 어떤 자리를 건너뛰는지 반드시 확인한다.<br><br>

<b>모두 뒷면이 되는 경우를 세려고 하면 안 된다.</b>
두 번의 시행으로는 동전 두 개까지만 바뀐다.
<b>도달할 수 없는 목표는 세기 전에 잘라 낸다.</b><br><br>

<b>확률의 합이 <span class="m">1</span>인지 확인하는 습관을 들인다.</b>
<span class="m">4 × (2/9) + 2 × (1/18) = 1</span>이 맞으므로
②단계의 계산이 옳다고 확신할 수 있다.
여기서 어긋나면 뒤의 계산은 모두 무의미하다.

## 노하우

<b>매 시행이 &lsquo;한 개&rsquo;를 뒤집으면 문제가 뽑기 문제로 바뀐다.</b>
어느 동전이 뒤집히는지만 따지면 되므로,
<b>동전마다 뽑힐 확률을 표로 정리</b>해 두고 시작한다.
그 뒤로는 평범한 독립시행 계산이다.<br><br>

<b>규칙이 갈라지면 &lsquo;두 갈래로 도달하는 것&rsquo;을 더한다.</b>
<span class="m">c<sub>1</sub></span>은 눈이 <span class="m">1</span>로 나와서도 뽑히고,
<span class="m">3</span>의 배수가 나온 뒤 임의로도 뽑힌다.
<b>같은 결과에 이르는 길이 여러 개면 확률을 더한다.</b><br><br>

<b>바뀔 수 있는 개수의 한계를 먼저 센다.</b>
시행 횟수 <span class="m">×</span> 한 번에 뒤집는 개수가
<b>목표에 필요한 개수보다 작으면</b> 그 목표는 확률이
<span class="m">0</span>이다.
이 한 줄이 경우의 절반을 지워 준다.
