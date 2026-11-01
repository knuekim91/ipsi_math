---
id: STA-W02
unit: 08-통계
topic: 절댓값으로 변환한 확률변수가 이항분포를 따를 때
level: 4점
difficulty: 상
source: 확률과 통계 29번 (2026-10-31 나은이 질문)
origin: 오답노트
core: "B(n,p)를 따르는 확률변수가 가질 수 있는 값은 0,1,…,n 뿐이다. 그래서 n 은 그 변수의 최댓값이고, 변환한 값을 전부 적어 보면 n 이 나온다"
tags: [이항분포,이산확률변수,절댓값,확률분포표,평균]
status: wrong
added: 2026-11-01
answer: 47
---

## 문제

<p>이산확률변수 <span class="m">X</span>가 가지는 값은 절댓값이
<span class="m">2</span> 이하인 정수이고, 확률변수
<span class="m">Y = |X + 1|</span>은 평균이 <span class="m">2</span>인
이항분포를 따른다.
<span class="m">E(X) = 5/6</span>일 때,
<span class="m">108 × P(|X − 1| = 1)</span>의 값을 구하시오.</p>

## 발상

<b>이항분포라는 말이 나오면 가장 먼저
&lsquo;그 변수가 가질 수 있는 값&rsquo;을 전부 적는다.</b><br><br>

<span class="m">B(n, p)</span>를 따르는 확률변수는
<span class="m">n</span>번의 시행에서 성공한 횟수이므로
<b><span class="m">0, 1, 2, …, n</span>만 가질 수 있다.</b>
곧 <b><span class="m">n</span>은 그 변수가 가질 수 있는 가장 큰 값</b>이다.
그러니 <span class="m">n</span>은 문제가 알려 주는 것이 아니라
<b>내가 세어서 찾는 것</b>이다.<br><br>

<b>두 번째로 볼 것은 변환이 일대일인가다.</b>
<span class="m">Y = |X + 1|</span>은 절댓값이라
<b>서로 다른 두 <span class="m">X</span>가 같은
<span class="m">Y</span>로 간다.</b>
그 칸에서는 확률이 합쳐져 버려서 <b>하나만으로는 갈라지지 않는다.</b>
<b>미지수가 하나 남는다.</b><br><br>

<b>남은 미지수를 잡으라고 준 것이 <span class="m">E(X) = 5/6</span>이다.</b>
조건이 왜 거기 있는지가 이걸로 설명된다.

## 풀이

<p><span class="step">① X가 가지는 값을 적고 Y로 옮긴다.</span>
절댓값이 <span class="m">2</span> 이하인 정수이므로</p>
<p class="m">X = −2, −1, 0, 1, 2</p>
<p>각각을 <span class="m">Y = |X + 1|</span>에 넣는다.</p>
<p class="m">X = −2 → Y = |−1| = 1</p>
<p class="m">X = −1 → Y = |0| = 0</p>
<p class="m">X = 0 → Y = |1| = 1</p>
<p class="m">X = 1 → Y = |2| = 2</p>
<p class="m">X = 2 → Y = |3| = 3</p>

<p><span class="step">② n을 찾는다.</span>
<span class="m">Y</span>가 가질 수 있는 값은
<span class="m">0, 1, 2, 3</span>이고
<b>그 최댓값이 <span class="m">3</span></b>이다.
<span class="m">B(n, p)</span>를 따르는 변수는
<span class="m">0</span>부터 <span class="m">n</span>까지만 가지므로</p>
<p class="m">n = 3</p>

<p><span class="step">③ p를 구한다.</span>
이항분포의 평균은 <span class="m">np</span>이고 이것이
<span class="m">2</span>이므로</p>
<p class="m">3p = 2 → p = 2/3</p>

<p><span class="step">④ Y의 분포를 적는다.</span>
<span class="m">Y</span>는 <span class="m">B(3, 2/3)</span>을 따르므로
<span class="m">P(Y = y) = <sub>3</sub>C<sub>y</sub> (2/3)<sup>y</sup> (1/3)<sup>3−y</sup></span>이다.
분모를 <span class="m">27</span>로 맞춰 적는다.</p>
<p class="m">P(Y=0) = 1/27, &nbsp; P(Y=1) = 6/27, &nbsp; P(Y=2) = 12/27, &nbsp; P(Y=3) = 8/27</p>

<p><span class="step">⑤ X의 분포로 되돌린다.</span>
①의 대응을 거꾸로 읽는다.
<b><span class="m">Y = 1</span>만 두 군데에서 오는 것에 주의한다.</b></p>
<p class="m">P(X = −1) = P(Y=0) = 1/27</p>
<p class="m">P(X = −2) + P(X = 0) = P(Y=1) = 6/27</p>
<p class="m">P(X = 1) = P(Y=2) = 12/27</p>
<p class="m">P(X = 2) = P(Y=3) = 8/27</p>
<p><span class="m">P(X = −2)</span>와 <span class="m">P(X = 0)</span>은
<b>합만 알 뿐 따로는 모른다.</b>
<span class="m">P(X = −2) = a</span>로 놓는다.</p>

<p><span class="step">⑥ E(X)로 a를 잡는다.</span></p>
<p class="m">E(X) = (−2)a + (−1)(1/27) + 0 + (1)(12/27) + (2)(8/27)</p>
<p class="m">= −2a − 1/27 + 12/27 + 16/27 = −2a + 27/27 = −2a + 1</p>
<p><span class="m">E(X) = 5/6</span>이므로</p>
<p class="m">−2a + 1 = 5/6 → 2a = 1/6 → a = 1/12</p>
<p class="m">P(X = 0) = 6/27 − 1/12 = 2/9 − 1/12 = 5/36</p>

<p><span class="step">⑦ 묻는 확률을 구한다.</span>
<span class="m">|X − 1| = 1</span>이면
<span class="m">X − 1 = 1</span> 또는
<span class="m">X − 1 = −1</span>이므로</p>
<p class="m">X = 2 또는 X = 0</p>
<p class="m">P(|X − 1| = 1) = 8/27 + 5/36 = 32/108 + 15/108 = 47/108</p>
<p class="m">108 × 47/108 = 47</p>
<p class="m">답 47</p>

<p><span class="step">⑧ 확인한다.</span>
분모를 <span class="m">108</span>로 맞춰 다섯 확률을 더해 본다.</p>
<p class="m">9 + 4 + 15 + 48 + 32 = 108 ✓</p>
<p class="m">E(X) = (−18 − 4 + 0 + 48 + 64)/108 = 90/108 = 5/6 ✓</p>

## 함정

<b><span class="m">n</span>이 어디서 나오는지 몰라 멈추는 것이 이 문항의 첫 관문이다.</b>
실제로 여기서 막혀 해설을 봤다.
그런데 <b>풀다 만 종이에 이미 답이 있었다</b> —
<span class="m">X = −2, −1, 0, 1, 2</span> 아래에
<span class="m">Y = 1, 0, 1, 2, 3</span>이라고 적어 두었다.
<b>거기서 &lsquo;최댓값이 3이니까 n = 3&rsquo; 한 줄만 더 가면 됐다.</b>
막힌 것이 아니라 <b>다 해 놓고 연결을 안 한 것</b>이다.<br><br>

<b>겹치는 칸을 못 보면 <span class="m">56</span>이 나온다.</b>
<span class="m">Y = 1</span>이 <span class="m">X = −2</span>와
<span class="m">X = 0</span> 두 군데에서 오는데,
이걸 놓치고 <span class="m">P(X = 0) = 6/27</span>이라 두면</p>
<p class="m">108 × (8/27 + 6/27) = 56</p>
<p>이 된다. <b><span class="m">56</span>이 나왔다면 겹침을 놓친 것</b>이다.
그리고 그렇게 두면 <span class="m">E(X) = 5/6</span>이 쓰이지 않는다 —
<b>주어진 조건이 안 쓰이면 뭔가 빠뜨린 것</b>이다.<br><br>

<b><span class="m">n</span>을 평균에서 거꾸로 구하려 들면 안 된다.</b>
<span class="m">np = 2</span> 하나로는
<span class="m">n</span>과 <span class="m">p</span>가 둘 다 미지수라 정해지지 않는다.
<b><span class="m">n</span>은 값을 세어서 먼저 정하고, 그다음에
<span class="m">p</span>를 평균으로 구한다.</b> 순서가 정해져 있다.<br><br>

<b><span class="m">|X − 1| = 1</span>을 <span class="m">X = 2</span>만으로 읽지 않는다.</b>
<span class="m">X = 0</span>도 답이다.
<b>절댓값 방정식은 언제나 두 개</b>다
(다만 이 문항에서는 두 값 모두 <span class="m">X</span>의 범위 안에 있는지 확인해야 한다).

## 노하우

<b>이항분포가 보이면 값부터 전부 적는다.</b></p>
<p class="m">B(n, p) 를 따르는 확률변수가 가지는 값 = 0, 1, 2, …, n</p>
<p>그래서 <b><span class="m">n</span>은 최댓값</b>이고,
<b><span class="m">0</span>부터 빠짐없이 나와야</b> 한다.
둘 중 하나라도 어긋나면 그 변수는 이항분포를 따를 수 없다.
<b>이 한 줄이 이 유형의 입구를 전부 연다.</b><br><br>

<b>변환이 일대일인지 본다.</b>
절댓값·제곱처럼 <b>서로 다른 값을 같은 값으로 보내는 변환</b>이 있으면
그 칸에서 확률이 합쳐진다.</p>
<p class="m">겹치는 칸의 개수 = 남는 미지수의 개수 = 더 필요한 조건의 개수</p>
<p>이 문항은 겹치는 칸이 하나뿐이라 조건도
<span class="m">E(X)</span> 하나면 충분했다.
<b>겹침이 둘이면 조건도 둘이 필요하다.</b>
문제에 조건이 몇 개 있는지를 보면 겹침이 몇 군데인지 짐작할 수 있다.<br><br>

<b>분모를 하나로 맞춰 적는다.</b>
<span class="m">1/27, 6/27, 12/27, 8/27</span>처럼
<span class="m">27</span>로 맞춰 두면 더하고 빼기가 쉽고,
마지막에 <span class="m">108</span>을 곱하라고 하는 이유도 보인다.
<b>문제가 곱하라고 준 수는 대개 공통분모</b>다.
<span class="m">108 = 4 × 27</span>이니 <span class="m">36</span>과
<span class="m">27</span>을 함께 담는 수다.<br><br>

<b>주어진 조건이 전부 쓰였는지 확인하고 끝낸다.</b>
<span class="m">E(X) = 5/6</span>을 안 쓰고 답이 나왔다면
<b>어딘가에서 겹침을 뭉갠 것</b>이다.
검산은 확률의 합이 <span class="m">1</span>인지,
그리고 <span class="m">E(X)</span>가 정말
<span class="m">5/6</span>인지 두 가지를 본다.
