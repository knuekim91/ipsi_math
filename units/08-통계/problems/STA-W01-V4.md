---
id: STA-W01-V4
parent: STA-W01
unit: 08-통계
topic: 멈추는 시행과 조건부확률
level: 4점
difficulty: 상
source: 자체 개발 (STA-W01 변형 · 조건부확률)
origin: 유사문항
core: "분모는 원문항에서 이미 구한 P(X=3)이고, 분자는 그 경우를 첫 시행의 값으로 한 번 더 쪼개면 나온다"
tags: [이산확률변수,조건부확률,시행,상태추적,누적합]
status: variant
added: 2026-10-09
answer: ④
---

## 문제

<p>숫자 <span class="m">1, 1, 1, 2, 2, 3</span>이 하나씩 적혀 있는
<span class="m">6</span>장의 카드가 들어 있는 주머니가 있다.
이 주머니에서 임의로 <span class="m">1</span>장의 카드를 꺼내어
카드에 적힌 수를 확인한 후 다시 넣는 시행을 한다.
이 시행을 반복하여 확인한 모든 수의 합이
처음으로 <span class="m">4</span> 이상이 되면 이 시행을 멈춘다.
시행을 멈출 때까지 시행을 반복한 횟수를 확률변수
<span class="m">X</span>라 하자.
<span class="m">X = 3</span>일 때, 첫 번째 시행에서 확인한 수가
<span class="m">1</span>이었을 확률은?</p>

<div class="choices"><span>① 1/2</span><span>② 6/11</span><span>③ 7/12</span>
<span>④ 7/11</span><span>⑤ 3/4</span></div>

## 발상

<b>조건부확률이지만 새로 셀 것이 많지 않다.</b>
사건을 이렇게 둔다.</p>
<p class="m">A : X = 3 &nbsp;/&nbsp; B : 첫 번째 시행에서 확인한 수가 1</p>
<p class="m">P(B | A) = P(A ∩ B) / P(A)</p>
<p><b>분모 <span class="m">P(A)</span>는 원문항에서 구한
<span class="m">11/24</span></b>를 그대로 쓴다.<br><br>

<b>분자는 <span class="m">X = 3</span>인 경우를 첫 시행의 값으로 쪼개면 된다.</b>
<span class="m">X = 3</span>이려면 두 번째까지의 합이
<span class="m">3</span> 이하여야 하는데,
<b>그런 상태는 합 <span class="m">2</span>와 합 <span class="m">3</span>뿐</b>이고
거기에 닿는 길이 몇 개 없다.<br><br>

<b>첫 시행이 <span class="m">3</span>이면 그 자리에서 멈춘다는 점</b>을 쓰면
경우가 더 줄어든다. 곧 <span class="m">X = 3</span>인 경우의 첫 시행은
<span class="m">1</span> 아니면 <span class="m">2</span>다.

## 풀이

<p><span class="step">① 확률을 적고 사건을 정한다.</span></p>
<p class="m">P(1) = 1/2, &nbsp; P(2) = 1/3, &nbsp; P(3) = 1/6</p>
<p class="m">A : X = 3 &nbsp;/&nbsp; B : 첫 번째 시행의 수가 1</p>

<p><span class="step">② 2번 시행 뒤에 살아남는 상태를 구한다.</span>
<span class="m">X = 3</span>이려면 두 번 뽑고도 합이
<span class="m">3</span> 이하여야 한다.
<b>이때 첫 시행이 무엇이었는지를 함께 적어 둔다.</b>
첫 시행이 <span class="m">3</span>이면 합이 <span class="m">3</span>이 되고
두 번째에 반드시 멈추므로 <span class="m">X = 2</span>다.
따라서 첫 시행은 <span class="m">1</span> 또는 <span class="m">2</span>이다.</p>
<p class="m">첫 1 → 합 2 : (1/2)(1/2) = 1/4</p>
<p class="m">첫 1 → 합 3 : (1/2)(1/3) = 1/6</p>
<p class="m">첫 2 → 합 3 : (1/3)(1/2) = 1/6</p>

<p><span class="step">③ 세 번째에 멈출 확률을 곱한다.</span>
합 <span class="m">2</span>에서는 <span class="m">2</span> 또는
<span class="m">3</span>이 나와야 하므로 <span class="m">1/2</span>,
합 <span class="m">3</span>에서는 무엇이든 되므로 <span class="m">1</span>이다.</p>
<p class="m">첫 1, 합 2 : (1/4)(1/2) = 1/8</p>
<p class="m">첫 1, 합 3 : (1/6)(1) = 1/6</p>
<p class="m">첫 2, 합 3 : (1/6)(1) = 1/6</p>

<p><span class="step">④ 분모와 분자를 모은다.</span>
세 항을 모두 더하면 <span class="m">P(A)</span>이고,
첫 시행이 <span class="m">1</span>인 두 항만 더하면
<span class="m">P(A ∩ B)</span>다.
분모를 <span class="m">24</span>로 통일한다.</p>
<p class="m">P(A) = 3/24 + 4/24 + 4/24 = 11/24</p>
<p class="m">P(A ∩ B) = 3/24 + 4/24 = 7/24</p>
<p><span class="m">P(A)</span>가 원문항에서 구한 값과 같은지 확인되었다.</p>

<p><span class="step">⑤ 조건부확률을 구한다.</span>
분모가 같으므로 분자끼리의 비가 곧 답이다.</p>
<p class="m">P(B | A) = (7/24) / (11/24) = 7/11</p>
<p class="m">답 ④</p>

## 함정

<b>분모를 <span class="m">1</span>로 두면 안 된다.</b>
조건이 &lsquo;<span class="m">X = 3</span>일 때&rsquo;이므로
<b>표본공간이 <span class="m">X = 3</span>인 경우로 줄어든다.</b>
<span class="m">7/24</span>를 그대로 답으로 쓰면
<span class="m">P(A ∩ B)</span>이지 조건부확률이 아니다.<br><br>

<b>첫 시행이 <span class="m">1</span>일 확률이 <span class="m">1/2</span>이니
답도 <span class="m">1/2</span>이라고 넘겨짚으면 안 된다.</b>
①번이 바로 그 함정이다.
<b><span class="m">X = 3</span>이라는 조건이 붙으면 첫 시행이
<span class="m">1</span>이었을 가능성이 더 커진다.</b>
작은 수로 시작해야 세 번까지 끌 수 있기 때문이다.
실제로 <span class="m">7/11 ≒ 0.64</span>로 <span class="m">1/2</span>보다 크다.<br><br>

<b>첫 시행이 <span class="m">3</span>인 경우를 빠뜨리지 말고 &lsquo;제외된다&rsquo;고 밝힌다.</b>
빠뜨린 것과 따져 보고 제외한 것은 다르다.
첫 시행이 <span class="m">3</span>이면 두 번째에 반드시 멈추므로
<span class="m">X = 3</span>이 될 수 없다.

## 노하우

<b>경우를 나눌 때 &lsquo;나중에 조건이 될 만한 기준&rsquo;으로 나눠 둔다.</b>
원문항에서 <span class="m">P(X = 3)</span>을 구할 때
<b>첫 시행의 값까지 적어 두었다면</b> 이 문제는 그 표를 다시 읽는 것으로 끝난다.
조건부확률 문제는 거의 언제나 <b>앞에서 이미 센 것을 쪼개는 일</b>이다.<br><br>

<b>조건이 붙으면 어느 쪽으로 쏠리는지 먼저 느껴 본다.</b>
<span class="m">X</span>가 크다는 조건은 <b>작은 수로 시작했을 가능성</b>을 키우고,
<span class="m">X</span>가 작다는 조건은 큰 수로 시작했을 가능성을 키운다.
계산 결과가 이 방향과 어긋나면 어딘가 틀린 것이다.<br><br>

<b>분모가 같으면 분자끼리의 비로 바로 답을 쓴다.</b>
<span class="m">7/24</span>와 <span class="m">11/24</span>이므로
<span class="m">7 : 11</span>이 그대로 답이 된다.
<b>통분해 둔 상태를 끝까지 유지</b>하면 마지막 계산이 한 줄로 끝난다.
