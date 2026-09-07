---
id: INT-D10
unit: 06-적분
topic: 속도와 거리
level: 4점
difficulty: 중상
source: 2027 수능완성 실전 모의고사 2회 10번
exam: 2027-수능완성
origin: 기출
core: "두 점 사이의 거리가 최소인 시각은 위치의 차를 미분해서 찾고, 움직인 거리는 속도의 절댓값을 적분해서 구한다"
tags: [속도와거리,정적분,절댓값적분,극소]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>두 점 <span class="m">P</span>와 <span class="m">Q</span>는 시각
<span class="m">t = 0</span>일 때 각각 점 <span class="m">A(5)</span>와 점
<span class="m">B(0)</span>에서 동시에 출발하여 수직선 위를 움직인다.
두 점 <span class="m">P</span>, <span class="m">Q</span>의 시각
<span class="m">t (t ≥ 0)</span>에서의 속도는 각각</p>
<p class="m">v<sub>1</sub>(t) = t<sup>2</sup> − 2t, &nbsp; v<sub>2</sub>(t) = −t + 2</p>
<p>이다. 시각 <span class="m">t = a (a &gt; 0)</span>에서 두 점
<span class="m">P</span>, <span class="m">Q</span> 사이의 거리가 최소일 때,
시각 <span class="m">t = 0</span>에서 <span class="m">t = 2a</span>까지
점 <span class="m">P</span>가 움직인 거리는?</p>

<div class="choices"><span>① 13/2</span><span>② 7</span><span>③ 15/2</span>
<span>④ 8</span><span>⑤ 17/2</span></div>

## 발상

<b>이 문제는 서로 다른 두 가지를 차례로 묻고 있다.</b>
앞부분은 <b>두 점 사이의 거리</b>를 묻고, 뒷부분은 <b>한 점이 움직인 거리</b>를 묻는다.
이 둘은 계산 방법이 전혀 다르다.<br><br>

두 점 사이의 거리는 <b>두 점의 위치의 차의 절댓값</b>이다.
그러므로 먼저 속도를 적분하여 두 점의 위치를 각각 구해야 한다.
이때 <b>출발점의 좌표를 적분상수로 반드시 넣어야 한다.</b>
점 <span class="m">P</span>는 <span class="m">5</span>에서, 점 <span class="m">Q</span>는
<span class="m">0</span>에서 출발하므로 두 점의 출발 위치가 다르다.<br><br>

한 점이 움직인 거리는 <b>속도의 절댓값을 적분</b>한 것이다.
위치의 변화량이 아니다. 점 <span class="m">P</span>의 속도
<span class="m">v<sub>1</sub>(t) = t(t − 2)</span>는
<span class="m">0 &lt; t &lt; 2</span>에서 음수이므로,
점 <span class="m">P</span>는 도중에 방향을 바꾼다.
방향을 바꾸는 시각을 경계로 적분을 <b>끊어서</b> 계산해야 한다.

## 풀이

<p><span class="step">① 두 점의 위치를 각각 구한다.</span>
속도를 시각에 대하여 적분하면 위치의 변화량이 나온다. 여기에 출발 위치를 더하면
그 시각에서의 위치가 된다. 점 <span class="m">P</span>는
<span class="m">A(5)</span>에서 출발했으므로 <span class="m">5</span>를 더한다.</p>
<p class="m">x<sub>P</sub>(t) = 5 + ∫<sub>0</sub><sup>t</sup>(s<sup>2</sup> − 2s)ds
= 5 + [s<sup>3</sup>/3 − s<sup>2</sup>]<sub>0</sub><sup>t</sup>
= t<sup>3</sup>/3 − t<sup>2</sup> + 5</p>
<p>점 <span class="m">Q</span>는 <span class="m">B(0)</span>에서 출발했으므로
<span class="m">0</span>을 더한다.</p>
<p class="m">x<sub>Q</sub>(t) = 0 + ∫<sub>0</sub><sup>t</sup>(−s + 2)ds
= [−s<sup>2</sup>/2 + 2s]<sub>0</sub><sup>t</sup> = −t<sup>2</sup>/2 + 2t</p>

<p><span class="step">② 두 점 사이의 거리를 식으로 나타낸다.</span>
두 점 사이의 거리는 두 위치의 차의 절댓값이다.
계산의 편의를 위하여 <b>차 자체를</b> <span class="m">h(t)</span>라 하자.</p>
<p class="m">h(t) = x<sub>P</sub>(t) − x<sub>Q</sub>(t)
= (t<sup>3</sup>/3 − t<sup>2</sup> + 5) − (−t<sup>2</sup>/2 + 2t)</p>
<p class="m">h(t) = t<sup>3</sup>/3 − t<sup>2</sup>/2 − 2t + 5</p>
<p>두 점 사이의 거리는 <span class="m">|h(t)|</span>이다.</p>

<p><span class="step">③ h(t)의 극값을 찾는다.</span>
<span class="m">h(t)</span>를 <span class="m">t</span>에 대하여 미분한다.</p>
<p class="m">h′(t) = t<sup>2</sup> − t − 2 = (t − 2)(t + 1)</p>
<p>구하는 범위는 <span class="m">t ≥ 0</span>이므로
<span class="m">t = −1</span>은 버린다.
<span class="m">0 ≤ t &lt; 2</span>에서 <span class="m">h′(t) &lt; 0</span>이고
<span class="m">t &gt; 2</span>에서 <span class="m">h′(t) &gt; 0</span>이므로,
<span class="m">h(t)</span>는 <span class="m">t = 2</span>에서 극소이면서 최소이다.</p>

<p><span class="step">④ h(t)의 부호를 확인한다.</span>
<b>이 단계를 건너뛰면 안 된다.</b>
거리는 <span class="m">|h(t)|</span>이므로, <span class="m">h(t)</span>가
부호를 바꾸면 거리가 <span class="m">0</span>이 되는 시각이 따로 생긴다.
<span class="m">t ≥ 0</span>에서 <span class="m">h(t)</span>의 최솟값을 확인한다.</p>
<p class="m">h(2) = 8/3 − 2 − 4 + 5 = 8/3 − 1 = 5/3</p>
<p><span class="m">h(t)</span>의 최솟값이 <span class="m">5/3 &gt; 0</span>이므로
<span class="m">t ≥ 0</span>에서 항상 <span class="m">h(t) &gt; 0</span>이고,
따라서 <span class="m">|h(t)| = h(t)</span>이다.
그러므로 두 점 사이의 거리가 최소인 시각은
<span class="m">h(t)</span>가 최소인 시각과 같다.</p>
<p class="m">a = 2</p>

<p><span class="step">⑤ 점 P가 움직인 거리를 세운다.</span>
<span class="m">2a = 4</span>이므로 시각 <span class="m">t = 0</span>에서
<span class="m">t = 4</span>까지 점 <span class="m">P</span>가 움직인 거리를 구한다.
움직인 거리는 <b>속도의 절댓값의 정적분</b>이다.</p>
<p class="m">(움직인 거리) = ∫<sub>0</sub><sup>4</sup>|v<sub>1</sub>(t)|dt
= ∫<sub>0</sub><sup>4</sup>|t<sup>2</sup> − 2t|dt</p>
<p><span class="m">v<sub>1</sub>(t) = t(t − 2)</span>이므로
<span class="m">0 &lt; t &lt; 2</span>에서 음수이고
<span class="m">2 &lt; t &lt; 4</span>에서 양수이다.
<b>부호가 바뀌는 <span class="m">t = 2</span>를 경계로 적분을 끊는다.</b></p>

<p><span class="step">⑥ 두 조각을 각각 적분한다.</span>
앞 구간에서는 절댓값을 벗기면서 부호를 바꾼다.</p>
<p class="m">∫<sub>0</sub><sup>2</sup>(2t − t<sup>2</sup>)dt
= [t<sup>2</sup> − t<sup>3</sup>/3]<sub>0</sub><sup>2</sup>
= 4 − 8/3 = 4/3</p>
<p>뒤 구간에서는 그대로 벗긴다.</p>
<p class="m">∫<sub>2</sub><sup>4</sup>(t<sup>2</sup> − 2t)dt
= [t<sup>3</sup>/3 − t<sup>2</sup>]<sub>2</sub><sup>4</sup></p>
<p class="m">= (64/3 − 16) − (8/3 − 4) = 16/3 − (−4/3) = 20/3</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">(움직인 거리) = 4/3 + 20/3 = 24/3 = 8</p>
<p class="m">답 ④</p>

## 함정

<b>가장 흔한 실수는 출발 위치를 빠뜨리는 것이다.</b>
점 <span class="m">P</span>는 원점이 아니라 <span class="m">A(5)</span>에서 출발한다.
<span class="m">5</span>를 더하지 않으면 <span class="m">h(t)</span>가 달라지고,
<span class="m">h(t)</span>가 부호를 바꾸게 되어 거리가 최소인 시각을 잘못 잡는다.<br><br>

<b>두 번째 실수는 움직인 거리를 위치의 변화량으로 구하는 것이다.</b>
<span class="m">∫<sub>0</sub><sup>4</sup>v<sub>1</sub>(t)dt</span>를 그대로 계산하면
<span class="m">16/3</span>이 나오는데, 이것은
<b>움직인 거리가 아니라 위치의 변화량</b>이다.
점 <span class="m">P</span>가 <span class="m">0 &lt; t &lt; 2</span>에서 뒤로 갔다가
다시 앞으로 나오므로, 실제로 지나온 길의 길이는 이보다 길다.<br><br>

<b>세 번째로, <span class="m">2a</span>를 <span class="m">a</span>로 착각하지 않는다.</b>
구하는 것은 <span class="m">t = 0</span>부터 <span class="m">t = 2a = 4</span>까지이다.

## 노하우

<b>수직선 위 두 점 문제는 항상 위치부터 만든다.</b>
속도가 주어지면 그것은 도함수이므로, 적분하여 위치로 바꾸어야 두 점을 비교할 수 있다.
이때 <b>적분상수는 출발 위치</b>라는 것을 기억한다.<br><br>

<b>거리의 최솟값을 물으면 절댓값의 부호를 반드시 확인한다.</b>
<span class="m">|h(t)|</span>의 최소는 두 곳에서 날 수 있다.
하나는 <span class="m">h(t) = 0</span>인 곳이고, 다른 하나는
<span class="m">h(t)</span>가 부호를 바꾸지 않을 때의 극값이다.
극값의 부호를 확인하는 한 줄이 두 경우를 갈라 준다.<br><br>

<b>움직인 거리에는 절댓값이 붙고, 위치의 변화량에는 붙지 않는다.</b>
속도가 <span class="m">0</span>이 되는 시각을 찾아 구간을 끊는 것이
절댓값 적분의 전부다.
