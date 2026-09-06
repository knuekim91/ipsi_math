---
id: DIF-W01
unit: 05-미분
topic: 수열합 조건과 다항함수 결정
level: 4점
difficulty: 상
source: 2019-06모평 나형 30번
exam: 2019-06모평
origin: 오답노트
core: "(나)의 부등식이 '값이 1이 되는 길'을 막아 f(4)=f(5)=0을 강제한다"
tags: [사차함수,수열합,평균변화율,수열의합]
status: wrong
added: 2026-09-06
answer: 65
---

## 문제

<p>사차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킨다.</p><span class="cond">(가) <span class="m">5</span> 이하의 모든 자연수 <span class="m">n</span>에 대하여 <span class="m">Σ<sub>k=1</sub><sup>n</sup> f(k) = f(n)f(n+1)</span>이다.<br><br>(나) <span class="m">n = 3, 4</span>일 때, 함수 <span class="m">f(x)</span>에서 <span class="m">x</span>의 값이 <span class="m">n</span>에서 <span class="m">n+2</span>까지 변할 때의 평균변화율은 <b>양수가 아니다</b>.</span><p><span class="m">128 × f(5/2)</span>의 값을 구하시오.</p>

## 발상

<b>합이 나오면 이웃한 두 합의 차를 본다.</b> <span class='m'>S(n) = f(n)f(n+1)</span>에서 <span class='m'>S(n) − S(n−1) = f(n)</span>을 쓰면 <span class='m'>f(n)[f(n+1) − f(n−1) − 1] = 0</span>. 즉 <b>각 <span class='m'>n</span>마다 &lsquo;<span class='m'>f(n)=0</span>&rsquo;이거나 &lsquo;<span class='m'>f(n+1)−f(n−1)=1</span>&rsquo;</b> 둘 중 하나다.<br><br>여기서 <b>(나)가 결정적</b>이다. (나)는 <span class='m'>f(5)−f(3) ≤ 0</span>, <span class='m'>f(6)−f(4) ≤ 0</span>이라는 뜻인데, 이 두 값은 <b>절대 1이 될 수 없다</b>. 그러니 <span class='m'>n=4, 5</span>에서는 다른 쪽 갈래, 곧 <span class='m'>f(4)=0</span>과 <span class='m'>f(5)=0</span>이 강제된다.

## 풀이

<p><span class="step">① 이웃한 두 합의 차를 본다.</span> <span class="m">S(n) = Σ<sub>k=1</sub><sup>n</sup>f(k) = f(n)f(n+1)</span>이라 하면 <span class="m">n = 2, 3, 4, 5</span>에서</p><p class="m">f(n) = S(n) − S(n−1) = f(n)f(n+1) − f(n−1)f(n)</p><p class="m">f(n)[f(n+1) − f(n−1) − 1] = 0 &nbsp;&nbsp; … (★)</p><p><span class="m">n = 1</span>일 때는 <span class="m">f(1) = f(1)f(2)</span>, 곧 <span class="m">f(1)[1 − f(2)] = 0</span>.</p><p><span class="step">② (나)를 식으로.</span> 평균변화율이 양수가 아니므로</p><p class="m">(f(5) − f(3))/2 ≤ 0, &nbsp; (f(6) − f(4))/2 ≤ 0</p><p class="m">f(5) − f(3) ≤ 0, &nbsp; f(6) − f(4) ≤ 0</p><p><span class="step">③ f(4) = f(5) = 0 을 끌어낸다.</span> (★)에서 <span class="m">n = 4</span>는 <span class="m">f(4) = 0</span> 또는 <span class="m">f(5) − f(3) = 1</span>인데, ②에 의해 뒤쪽은 불가능하다. 따라서 <b><span class="m">f(4) = 0</span></b>. 같은 이유로 <span class="m">n = 5</span>에서 <b><span class="m">f(5) = 0</span></b>.</p><p><span class="step">④ 남은 조건으로 경우를 나눈다.</span> (★)의 <span class="m">n = 3</span>은 <span class="m">f(3) = 0</span> 또는 <span class="m">f(4) − f(2) = 1</span>, 곧 <span class="m">f(2) = −1</span>.</p><p><b>[경우 1] f(3) = 0</b> &nbsp; 이때 <span class="m">f(3)=f(4)=f(5)=0</span>.</p><p>(★)의 <span class="m">n=2</span>는 <span class="m">f(2)=0</span> 또는 <span class="m">f(3)−f(1)=1</span>, 곧 <span class="m">f(1) = −1</span>.</p><p>· <span class="m">f(2)=0</span>이면 근이 <span class="m">2,3,4,5</span> 네 개라 <span class="m">f = a(x−2)(x−3)(x−4)(x−5)</span>. <span class="m">n=1</span> 조건에서 <span class="m">f(2)=0≠1</span>이므로 <span class="m">f(1)=0</span>이 되어 근이 다섯 개 → 모든 <span class="m">x</span>에서 <span class="m">f(x) = 0</span>이 되어 사차함수가 아니다. 탈락.</p><p>· 따라서 <span class="m">f(1) = −1</span>. <span class="m">n=1</span> 조건에서 <span class="m">f(1) ≠ 0</span>이므로 <b><span class="m">f(2) = 1</span></b>.</p><p><b>[경우 2] f(2) = −1</b> &nbsp; <span class="m">n=2</span>에서 <span class="m">f(2)≠0</span>이므로 <span class="m">f(3) = f(1)+1</span>, <span class="m">n=1</span>에서 <span class="m">f(2) = −1 ≠ 1</span>이므로 <span class="m">f(1) = 0</span>, 따라서 <span class="m">f(3) = 1</span>.</p><p>이 경우 <span class="m">f</span>는 근 <span class="m">1, 4, 5</span>를 가지고 <span class="m">f(2)=−1, f(3)=1</span>에서 <span class="m">f = (5/12)(x−1)(x−4)(x−5)(x − 12/5)</span>. 그런데 <span class="m">f(6) = 15</span>이라 <span class="m">f(6) − f(4) = 15 &gt; 0</span>이다. <b>(나)에 어긋난다. 탈락.</b></p><p><span class="step">⑤ f를 결정한다.</span> 경우 1이 살아남았다.</p><p class="m">f(1) = −1, f(2) = 1, f(3) = f(4) = f(5) = 0</p><p><span class="m">3, 4, 5</span>가 근이므로 <span class="m">f(x) = a(x−3)(x−4)(x−5)(x−s)</span>로 두면</p><p class="m">f(2) = −6a(2−s) = 1, &nbsp; f(1) = −24a(1−s) = −1</p><p>두 식을 나누면 <span class="m">4(1−s)/(2−s) = −1</span> → <span class="m">s = 6/5</span>, 그리고 <span class="m">a = −5/24</span>.</p><p class="m">f(x) = −(1/24)(x−3)(x−4)(x−5)(5x−6)</p><p><span class="step">⑥ 확인과 답.</span> <span class="m">f(6) = −6</span>이므로 <span class="m">f(6)−f(4) = −6 ≤ 0</span>, <span class="m">f(5)−f(3) = 0 ≤ 0</span>으로 (나) 만족 ✓</p><p class="m">f(5/2) = −(1/24)(−1/2)(−3/2)(−5/2)(13/2) = 65/128</p><p class="m">128 × f(5/2) = 65</p>

## 함정

<b>(나)를 마지막에 검산용으로만 쓰면 경우가 열 갈래로 터진다.</b> (가)만으로 나오는 사차함수는 열 개나 되고, 그걸 다 구한 뒤 거르면 시험 시간에 못 끝낸다. (나)는 <b>맨 처음에 갈래를 쳐내는 칼</b>로 써야 한다. &lsquo;<span class='m'>≤ 0</span>인 값이 <span class='m'>1</span>일 수는 없다&rsquo;는 한 줄이 <span class='m'>f(4)=f(5)=0</span>을 공짜로 준다.

## 노하우

<b>Σ 조건이 나오면 반사적으로 <span class='m'>S(n) − S(n−1) = f(n)</span>을 쓴다.</b> 수열에서 <span class='m'>S<sub>n</sub></span>과 <span class='m'>a<sub>n</sub></span>의 관계로 배운 그것이다. 그러면 곱 꼴의 조건이 <b><span class='m'>f(n) × [무엇] = 0</span></b>이라는 두 갈래 조건으로 바뀐다.<br><br>그리고 이 문제의 진짜 교훈: <b>부등식 조건은 답을 검산하는 도구가 아니라 갈래를 죽이는 도구다.</b> &lsquo;<span class='m'>A ≤ 0</span>&rsquo;과 &lsquo;<span class='m'>A = 1</span> 또는 …&rsquo;이 함께 있으면 <span class='m'>A = 1</span> 쪽은 그 자리에서 사망한다. 이런 조건은 <b>읽자마자 부등호로 바꿔 적어 두는 습관</b>이 시간을 반으로 줄인다.
