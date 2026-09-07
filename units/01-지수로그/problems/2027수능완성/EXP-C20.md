---
id: EXP-C20
unit: 01-지수로그
topic: 로그 곡선들의 교점
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 20번
exam: 2027-수능완성
origin: 기출
core: "log₂(−x+k) = −log₂x 는 두 진수의 곱이 1이라는 뜻이라 이차방정식이 된다"
tags: [로그함수,교점,근과계수의관계]
status: seed
added: 2026-09-07
answer: 38
---

## 문제

<p>그림과 같이 <span class="m">k &gt; 2</span>인 상수 <span class="m">k</span>에 대하여
곡선 <span class="m">y = log<sub>2</sub>(−x+k)</span>가 곡선
<span class="m">y = log<sub>2</sub>x</span>와 만나는 점을 <span class="m">P</span>,
곡선 <span class="m">y = log<sub>2</sub>(−x+k)</span>가 곡선
<span class="m">y = log<sub>1/2</sub>x</span>와 제1사분면에서 만나는 점을
<span class="m">Q</span>, 제4사분면에서 만나는 점을 <span class="m">R</span>이라 하고,
세 점 <span class="m">P, Q, R</span>의 <span class="m">x</span>좌표를 각각
<span class="m">p, q, r</span>이라 하자.
<span class="m">p − q = 2√2</span>일 때,
<span class="m">k + (r−q)<sup>2</sup></span>의 값을 구하시오.</p>

<div class="fig"><img src="img/EXP-C20.png" width="848" height="706"
  alt="세 곡선 y=log2 x, y=log(1/2) x, y=log2(-x+k) 가 그려져 있다. 두 점 P와 Q, R가 곡선들의 교점에 표시되어 있다."></div>

## 발상

<b>두 종류의 교점을 따로 본다.</b><br><br>
<span class="m">P</span>는 <span class="m">log<sub>2</sub>(−x+k) = log<sub>2</sub>x</span>이므로
밑이 같아 <b>진수끼리 같다</b>고 놓으면 끝난다.<br><br>
<span class="m">Q, R</span>는 <span class="m">log<sub>1/2</sub>x = −log<sub>2</sub>x</span>이므로
<span class="m">log<sub>2</sub>(−x+k) + log<sub>2</sub>x = 0</span>이 되고,
로그의 합은 <b>진수의 곱</b>이므로 <span class="m">x(k−x) = 1</span>이라는
<b>이차방정식</b>이 나온다. 두 근이 곧 <span class="m">q</span>와 <span class="m">r</span>이다.

## 풀이

<p><span class="step">① 점 P의 x좌표를 구한다.</span>
두 로그의 밑이 모두 <span class="m">2</span>로 같으므로 진수끼리 같다.</p>
<p class="m">−x + k = x → k = 2x → x = k/2</p>
<p class="m">p = k/2</p>

<p><span class="step">② 점 Q, R가 만족시키는 식을 세운다.</span>
밑변환으로 <span class="m">log<sub>1/2</sub>x = −log<sub>2</sub>x</span>이므로</p>
<p class="m">log<sub>2</sub>(−x+k) = −log<sub>2</sub>x</p>
<p><span class="m">log<sub>2</sub>x</span>를 왼쪽으로 넘긴다.</p>
<p class="m">log<sub>2</sub>(−x+k) + log<sub>2</sub>x = 0</p>
<p>로그의 합은 진수의 곱이다.</p>
<p class="m">log<sub>2</sub>{x(k − x)} = 0</p>
<p>로그값이 <span class="m">0</span>이라는 것은 진수가 <span class="m">1</span>이라는 뜻이다.</p>
<p class="m">x(k − x) = 1 → x<sup>2</sup> − kx + 1 = 0 &nbsp;&nbsp; … (★)</p>

<p><span class="step">③ q와 r가 (★)의 두 근임을 확인한다.</span>
근과 계수의 관계에서 <b>두 근의 곱이 <span class="m">1</span></b>이고
<b>합이 <span class="m">k &gt; 2</span></b>이므로 두 근은 모두 양수이고,
곱이 <span class="m">1</span>이니 <b>하나는 <span class="m">1</span>보다 작고
하나는 <span class="m">1</span>보다 크다.</b></p>
<p>한편 교점의 <span class="m">y</span>좌표는
<span class="m">y = log<sub>1/2</sub>x = −log<sub>2</sub>x</span>이므로</p>
<p class="m">x &lt; 1 → y &gt; 0 → 제1사분면 → 이 근이 q</p>
<p class="m">x &gt; 1 → y &lt; 0 → 제4사분면 → 이 근이 r</p>
<p>근의 공식으로 쓰면</p>
<p class="m">q = (k − √(k<sup>2</sup>−4))/2, &nbsp; r = (k + √(k<sup>2</sup>−4))/2</p>

<p><span class="step">④ 조건 p − q = 2√2 를 쓴다.</span></p>
<p class="m">p − q = k/2 − (k − √(k<sup>2</sup>−4))/2 = √(k<sup>2</sup>−4)/2</p>
<p>이것이 <span class="m">2√2</span>이므로</p>
<p class="m">√(k<sup>2</sup>−4) = 4√2</p>
<p>양변을 제곱한다.</p>
<p class="m">k<sup>2</sup> − 4 = 32 → k<sup>2</sup> = 36 → k = 6</p>
<p>(<span class="m">k &gt; 2</span>이므로 <span class="m">k = −6</span>은 버린다.)</p>

<p><span class="step">⑤ (r − q)²을 구한다.</span>
두 근의 차는 근호 부분의 두 배를 <span class="m">2</span>로 나눈 것이다.</p>
<p class="m">r − q = √(k<sup>2</sup>−4) = 4√2</p>
<p class="m">(r − q)<sup>2</sup> = k<sup>2</sup> − 4 = 32</p>
<p><b><span class="m">k</span>를 대입할 필요도 없이 ④에서 이미 나온 값</b>이다.</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">k + (r − q)<sup>2</sup> = 6 + 32 = 38</p>
<p class="m">답 38</p>

## 함정

<b>어느 근이 <span class="m">q</span>이고 어느 근이 <span class="m">r</span>인지
사분면으로 가려야 한다.</b> 두 근이 모두 양수라서
&lsquo;제1사분면 / 제4사분면&rsquo;은 <span class="m">x</span>의 부호가 아니라
<b><span class="m">y</span>의 부호</b>로 갈린다.
<span class="m">y = −log<sub>2</sub>x</span>이므로
<span class="m">x</span>가 <span class="m">1</span>보다 작아야 <span class="m">y &gt; 0</span>이다.
거꾸로 잡으면 <span class="m">p − q</span>가 음수가 되어 식이 성립하지 않는다.<br><br>
그리고 <span class="m">k<sup>2</sup> = 36</span>에서 <span class="m">k = ±6</span>이지만
<b><span class="m">k &gt; 2</span>가 음수를 버리게 한다.</b>

## 노하우

<b>로그의 합이 <span class="m">0</span>이면 진수의 곱이 <span class="m">1</span>이다.</b>
<span class="m">log a + log b = log(ab)</span>이고
<span class="m">log(ab) = 0 ⟺ ab = 1</span>.
밑이 서로 역수인 로그
(<span class="m">log<sub>2</sub></span>와 <span class="m">log<sub>1/2</sub></span>)가 함께 나오면
거의 항상 이 꼴로 정리된다.<br><br>
그리고 <b>두 근의 차를 물으면 근을 각각 구하지 않는다.</b>
<span class="m">x<sup>2</sup> − kx + 1 = 0</span>에서
<span class="m">(r−q)<sup>2</sup> = (r+q)<sup>2</sup> − 4rq = k<sup>2</sup> − 4</span>로
<b>근과 계수의 관계만으로</b> 끝난다.
