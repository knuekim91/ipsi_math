---
id: SEQ-C21
unit: 03-수열
topic: 곱이 0인 점화식의 갈래
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 21번
exam: 2027-수능완성
origin: 기출
core: "각 단계마다 두 갈래이므로 a₁을 문자로 두고 네 경로를 모두 따라간다"
tags: [점화식,경우나누기,수열]
status: seed
added: 2026-09-07
answer: 16
---

## 문제

<p>다음 조건을 만족시키는 모든 수열 <span class="m">{a<sub>n</sub>}</span>에 대하여
서로 다른 <span class="m">a<sub>4</sub></span>의 값의 집합을 <span class="m">X</span>라 할 때,
집합 <span class="m">X</span>의 모든 원소의 합을 구하시오.</p>
<span class="cond">(가) <span class="m">a<sub>1</sub> = a<sub>3</sub></span><br>
(나) 모든 자연수 <span class="m">n</span>에 대하여<br>
<span class="m">(a<sub>n+1</sub> + 2a<sub>n</sub> − 12)(a<sub>n+1</sub> − a<sub>n</sub> + 2) = 0</span>이다.</span>

## 발상

(나)는 <b>곱이 <span class="m">0</span></b>이므로 각 <span class="m">n</span>마다
둘 중 하나가 성립한다.</p>
<p class="m">㉠ a<sub>n+1</sub> = −2a<sub>n</sub> + 12 &nbsp;&nbsp; 또는 &nbsp;&nbsp; ㉡ a<sub>n+1</sub> = a<sub>n</sub> − 2</p>
<p><b>매 단계마다 갈래가 둘</b>이므로
<span class="m">a<sub>1</sub> → a<sub>2</sub> → a<sub>3</sub></span>까지 가는 길이
<span class="m">2 × 2 = 4</span>가지다.<br><br>
<span class="m">a<sub>1</sub></span>을 모르지만 <b>문자 <span class="m">t</span>로 두면
(가)가 각 경로마다 <span class="m">t</span>를 하나로 결정</b>해 준다.
그 다음 <span class="m">a<sub>4</sub></span>로 가는 갈래가 또 둘이다.

## 풀이

<p><span class="step">① 두 갈래를 적어 둔다.</span>
곱이 <span class="m">0</span>이면 둘 중 하나가 <span class="m">0</span>이다.</p>
<p class="m">㉠ a<sub>n+1</sub> + 2a<sub>n</sub> − 12 = 0 → a<sub>n+1</sub> = −2a<sub>n</sub> + 12</p>
<p class="m">㉡ a<sub>n+1</sub> − a<sub>n</sub> + 2 = 0 → a<sub>n+1</sub> = a<sub>n</sub> − 2</p>
<p><span class="m">a<sub>1</sub> = t</span>로 놓는다.</p>

<p><span class="step">② 네 경로를 따라가며 a₃를 t로 나타낸다.</span></p>
<p><b>[경로 ㉠㉠]</b></p>
<p class="m">a<sub>2</sub> = −2t + 12, &nbsp; a<sub>3</sub> = −2(−2t+12) + 12 = 4t − 12</p>
<p><b>[경로 ㉠㉡]</b></p>
<p class="m">a<sub>2</sub> = −2t + 12, &nbsp; a<sub>3</sub> = (−2t+12) − 2 = −2t + 10</p>
<p><b>[경로 ㉡㉠]</b></p>
<p class="m">a<sub>2</sub> = t − 2, &nbsp; a<sub>3</sub> = −2(t−2) + 12 = −2t + 16</p>
<p><b>[경로 ㉡㉡]</b></p>
<p class="m">a<sub>2</sub> = t − 2, &nbsp; a<sub>3</sub> = (t−2) − 2 = t − 4</p>

<p><span class="step">③ 조건 (가) a₁ = a₃ 로 t를 정한다.</span>
각 경로에서 <span class="m">a<sub>3</sub> = t</span>로 놓고 푼다.</p>
<p class="m">㉠㉠ : 4t − 12 = t → 3t = 12 → t = 4</p>
<p class="m">㉠㉡ : −2t + 10 = t → 3t = 10 → t = 10/3</p>
<p class="m">㉡㉠ : −2t + 16 = t → 3t = 16 → t = 16/3</p>
<p class="m">㉡㉡ : t − 4 = t → −4 = 0 → <b>해가 없다</b></p>
<p>마지막 경로는 <span class="m">a<sub>3</sub></span>가
<span class="m">a<sub>1</sub></span>보다 항상 <span class="m">4</span>만큼 작아
같아질 수 없다. 살아남는 경로는 <b>세 개</b>다.</p>

<p><span class="step">④ 각 경로에서 a₄를 구한다.</span>
<span class="m">a<sub>3</sub> = a<sub>1</sub> = t</span>이므로
<span class="m">a<sub>4</sub></span>는 <span class="m">t</span>에서 ㉠ 또는 ㉡으로 한 걸음 간 것이다.</p>

<p><b>㉠㉠ (<span class="m">t = 4</span>)</b> — 수열은
<span class="m">4, 4, 4, …</span>로 시작한다.</p>
<p class="m">㉠ : a<sub>4</sub> = −2(4) + 12 = 4 &nbsp;/&nbsp; ㉡ : a<sub>4</sub> = 4 − 2 = 2</p>

<p><b>㉠㉡ (<span class="m">t = 10/3</span>)</b> —
<span class="m">a<sub>2</sub> = −20/3 + 12 = 16/3</span>,
<span class="m">a<sub>3</sub> = 16/3 − 2 = 10/3</span> ✓</p>
<p class="m">㉠ : a<sub>4</sub> = −20/3 + 12 = 16/3 &nbsp;/&nbsp; ㉡ : a<sub>4</sub> = 10/3 − 2 = 4/3</p>

<p><b>㉡㉠ (<span class="m">t = 16/3</span>)</b> —
<span class="m">a<sub>2</sub> = 16/3 − 2 = 10/3</span>,
<span class="m">a<sub>3</sub> = −20/3 + 12 = 16/3</span> ✓</p>
<p class="m">㉠ : a<sub>4</sub> = −32/3 + 12 = 4/3 &nbsp;/&nbsp; ㉡ : a<sub>4</sub> = 16/3 − 2 = 10/3</p>

<p><span class="step">⑤ 집합 X를 만든다.</span>
나온 값을 모두 모으면
<span class="m">4, 2, 16/3, 4/3, 4/3, 10/3</span>인데
<b>집합이므로 겹치는 <span class="m">4/3</span>은 한 번만 센다.</b></p>
<p class="m">X = {2, 4, 4/3, 10/3, 16/3}</p>

<p><span class="step">⑥ 원소의 합을 구한다.</span>
분모가 <span class="m">3</span>인 것끼리 먼저 더한다.</p>
<p class="m">4/3 + 10/3 + 16/3 = 30/3 = 10</p>
<p class="m">2 + 4 = 6</p>
<p class="m">합 = 10 + 6 = 16</p>
<p class="m">답 16</p>

## 함정

<b>㉡㉡ 경로를 &lsquo;해가 없다&rsquo;고 버려야 한다.</b>
<span class="m">t − 4 = t</span>는 <span class="m">t</span>가 지워지면서
<span class="m">−4 = 0</span>이라는 거짓이 남는다.
이것을 <span class="m">t = 0</span>으로 잘못 처리하면 없는 수열이 하나 생긴다.<br><br>
그리고 <b><span class="m">X</span>는 집합이다.</b>
<span class="m">4/3</span>이 서로 다른 두 경로에서 나오지만
<b>한 번만 센다.</b> 두 번 더하면 답이 <span class="m">52/3</span>이 된다.

## 노하우

<b>곱이 <span class="m">0</span>인 점화식은 &lsquo;매 단계 두 갈래&rsquo;로 읽는다.</b>
<span class="m">n</span>단계까지 가는 경로가 <span class="m">2<sup>n</sup></span>가지이므로,
단계가 적을 때만 이렇게 전부 따라갈 수 있다.
이 문제는 <span class="m">a<sub>1</sub> → a<sub>3</sub></span>까지 두 걸음이라
<span class="m">4</span>가지로 감당할 수 있다.<br><br>
<b>첫째항을 모를 때는 문자로 두고 조건이 그것을 잡게 한다.</b>
경로마다 <span class="m">t</span>가 다르게 결정된다는 점이 이 문제의 핵심이고,
&lsquo;해가 없는 경로&rsquo;가 나오는 것도 정상이다.
