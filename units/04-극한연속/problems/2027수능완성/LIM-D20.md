---
id: LIM-D20
unit: 04-극한연속
topic: 두 조각함수의 곱의 연속
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 20번
exam: 2027-수능완성
origin: 기출
core: "곱이 연속이려면 한쪽이 끊기는 자리에서 다른 쪽이 0이면 된다. 두 분기점 x=1, x=a를 따로 따진다"
tags: [연속,조각함수,좌극한우극한,경우나누기]
status: seed
added: 2026-09-07
answer: 49
---

## 문제

<p>실수 <span class="m">a</span>에 대하여 두 함수
<span class="m">f(x)</span>, <span class="m">g(x)</span>를</p>
<p class="m">f(x) = x − a &nbsp; (x ≤ 1), &nbsp; f(x) = x<sup>2</sup> − 4a &nbsp; (x &gt; 1)</p>
<p class="m">g(x) = (x − 1)<sup>2</sup> &nbsp; (x ≤ a), &nbsp; g(x) = −(16/9)x + a<sup>2</sup> &nbsp; (x &gt; a)</p>
<p>라 하자. 함수 <span class="m">f(x)g(x)</span>가 실수 전체의 집합에서
연속이 되도록 하는 모든 <span class="m">a</span>의 값의 합은
<span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>두 함수가 끊길 수 있는 자리는 딱 두 곳이다.</b>
<span class="m">f</span>는 <span class="m">x = 1</span>에서,
<span class="m">g</span>는 <span class="m">x = a</span>에서 식이 바뀐다.
다른 곳에서는 둘 다 다항함수이므로 연속이고, 따라서 곱도 연속이다.
<b>이 두 점만 확인하면 된다.</b><br><br>

<b>곱이 연속이 되는 방법은 두 가지다.</b>
하나는 <b>끊기는 함수 자체가 사실은 끊기지 않는 경우</b>이고,
다른 하나는 <b>끊기더라도 상대편 함수가 그 점에서
<span class="m">0</span>이 되어 점프를 지워 버리는 경우</b>다.
<span class="m">0</span>에 어떤 유한한 값을 곱해도 <span class="m">0</span>이므로,
좌극한과 우극한이 모두 <span class="m">0</span>으로 같아진다.<br><br>

그러므로 각 분기점마다
<b>&lsquo;끊기지 않거나, 상대편이 <span class="m">0</span>이거나&rsquo;</b>라는
두 갈래 조건이 나오고, 두 분기점의 조건을 <b>동시에</b> 만족시키는
<span class="m">a</span>를 찾으면 된다.

## 풀이

<p><span class="step">① x = 1에서의 조건을 세운다.</span>
먼저 <span class="m">a ≠ 1</span>인 경우를 본다.
이때 <span class="m">g</span>는 <span class="m">x = 1</span>에서 연속이므로
좌우 극한이 모두 <span class="m">g(1)</span>이다.
<span class="m">f</span>의 좌극한과 우극한을 각각 구한다.</p>
<p class="m">f(1−) = 1 − a, &nbsp; f(1+) = 1<sup>2</sup> − 4a = 1 − 4a</p>
<p>곱의 좌극한과 우극한이 같아야 한다.</p>
<p class="m">(1 − a)g(1) = (1 − 4a)g(1)</p>
<p class="m">3a × g(1) = 0 → a = 0 또는 g(1) = 0</p>

<p><span class="step">② g(1) = 0인 a를 구한다.</span>
<span class="m">g(1)</span>이 어느 식으로 계산되는지는
<span class="m">1</span>과 <span class="m">a</span>의 대소가 정한다.<br>
<span class="m">1 ≤ a</span>이면 <span class="m">g(1) = (1 − 1)<sup>2</sup> = 0</span>이므로
<b>항상 성립한다.</b><br>
<span class="m">1 &gt; a</span>이면 <span class="m">g(1) = −16/9 + a<sup>2</sup></span>이므로</p>
<p class="m">a<sup>2</sup> = 16/9 → a = 4/3 또는 a = −4/3</p>
<p><span class="m">a &lt; 1</span>이어야 하므로 <span class="m">a = −4/3</span>만 남는다.
정리하면 <span class="m">x = 1</span>에서의 조건은 다음과 같다.</p>
<p class="m">a ≥ 1 또는 a = −4/3 또는 a = 0</p>

<p><span class="step">③ x = a에서의 조건을 세운다.</span>
역시 <span class="m">a ≠ 1</span>인 경우이다.
이때 <span class="m">f</span>는 <span class="m">x = a</span>에서 연속이다.
<span class="m">g</span>의 좌극한과 우극한을 구한다.</p>
<p class="m">g(a−) = (a − 1)<sup>2</sup>, &nbsp; g(a+) = −(16/9)a + a<sup>2</sup></p>
<p>곱의 좌극한과 우극한이 같아야 한다.</p>
<p class="m">f(a) × (a − 1)<sup>2</sup> = f(a) × (a<sup>2</sup> − (16/9)a)</p>
<p class="m">f(a) × [(a − 1)<sup>2</sup> − a<sup>2</sup> + (16/9)a] = 0</p>
<p>대괄호 안을 전개하여 정리한다.</p>
<p class="m">a<sup>2</sup> − 2a + 1 − a<sup>2</sup> + (16/9)a = 1 − (2/9)a</p>
<p class="m">f(a) × (1 − (2/9)a) = 0 → f(a) = 0 또는 a = 9/2</p>

<p><span class="step">④ f(a) = 0인 a를 구한다.</span>
<span class="m">f(a)</span>가 어느 식으로 계산되는지는
<span class="m">a</span>와 <span class="m">1</span>의 대소가 정한다.<br>
<span class="m">a ≤ 1</span>이면 <span class="m">f(a) = a − a = 0</span>이므로
<b>항상 성립한다.</b><br>
<span class="m">a &gt; 1</span>이면
<span class="m">f(a) = a<sup>2</sup> − 4a = a(a − 4)</span>이므로</p>
<p class="m">a = 0 또는 a = 4</p>
<p><span class="m">a &gt; 1</span>이어야 하므로 <span class="m">a = 4</span>만 남는다.
정리하면 <span class="m">x = a</span>에서의 조건은 다음과 같다.</p>
<p class="m">a ≤ 1 또는 a = 4 또는 a = 9/2</p>

<p><span class="step">⑤ 두 조건을 함께 만족시키는 a를 찾는다.</span>
②의 조건과 ④의 조건을 모두 만족시켜야 한다.
경우를 빠짐없이 맞춰 본다.</p>
<p class="m">a ≥ 1 이고 a ≤ 1 → a = 1</p>
<p class="m">a ≥ 1 이고 a = 4 → a = 4</p>
<p class="m">a ≥ 1 이고 a = 9/2 → a = 9/2</p>
<p class="m">a = −4/3 이고 a ≤ 1 → a = −4/3</p>
<p class="m">a = 0 이고 a ≤ 1 → a = 0</p>
<p>후보는 <span class="m">a = 1, 4, 9/2, −4/3, 0</span>의 다섯 개이다.</p>

<p><span class="step">⑥ a = 1인 경우를 따로 확인한다.</span>
①과 ③에서는 <span class="m">a ≠ 1</span>을 가정했으므로
<span class="m">a = 1</span>은 직접 확인해야 한다.
이때 두 분기점이 <span class="m">x = 1</span> 한 곳에서 겹친다.</p>
<p class="m">f(1−) = 1 − 1 = 0, &nbsp; f(1+) = 1 − 4 = −3</p>
<p class="m">g(1−) = (1 − 1)<sup>2</sup> = 0, &nbsp; g(1+) = −16/9 + 1 = −7/9</p>
<p>곱의 좌극한과 우극한을 각각 계산한다.</p>
<p class="m">(좌극한) = 0 × 0 = 0</p>
<p class="m">(우극한) = (−3) × (−7/9) = 21/9 = 7/3</p>
<p>두 값이 다르므로 <span class="m">a = 1</span>일 때
<span class="m">f(x)g(x)</span>는 <span class="m">x = 1</span>에서
연속이 아니다. <b><span class="m">a = 1</span>은 버린다.</b></p>

<p><span class="step">⑦ 답을 만든다.</span>
조건을 만족시키는 <span class="m">a</span>는
<span class="m">−4/3</span>, <span class="m">0</span>,
<span class="m">4</span>, <span class="m">9/2</span>이다.
분모를 <span class="m">6</span>으로 통일하여 더한다.</p>
<p class="m">−4/3 + 0 + 4 + 9/2 = −8/6 + 24/6 + 27/6 = 43/6</p>
<p><span class="m">43</span>과 <span class="m">6</span>은 서로소이므로
<span class="m">q = 43</span>, <span class="m">p = 6</span>이다.</p>
<p class="m">p + q = 6 + 43 = 49</p>
<p class="m">답 49</p>

## 함정

<b>두 분기점이 겹치는 <span class="m">a = 1</span>을 그냥 통과시키면 틀린다.</b>
<span class="m">a ≠ 1</span>일 때의 논리는
&lsquo;한쪽이 끊길 때 다른 쪽은 연속&rsquo;이라는 전제 위에 서 있다.
<span class="m">a = 1</span>이면 <b>두 함수가 같은 자리에서 동시에 끊기므로</b>
그 전제가 무너진다. 반드시 직접 확인해야 한다.<br><br>

<b><span class="m">g(1)</span>과 <span class="m">f(a)</span>를 계산할 때
어느 식을 쓸지 정하지 않으면 안 된다.</b>
<span class="m">g</span>의 분기점이 <span class="m">x = a</span>이므로
<span class="m">g(1)</span>은 <span class="m">1</span>과
<span class="m">a</span>의 대소에 따라 달라진다.
<b>이 대소 비교를 빠뜨리면 <span class="m">a = −4/3</span>을 놓친다.</b><br><br>

<b><span class="m">p</span>와 <span class="m">q</span>의 자리를 바꾸면 안 된다.</b>
합이 <span class="m">q/p</span>이므로
<b>분자가 <span class="m">q</span>, 분모가 <span class="m">p</span></b>이다.
다행히 이 문제는 합을 구하므로 답이 같지만, 습관을 들여 둔다.

## 노하우

<b>곱함수의 연속은 &lsquo;점프 × <span class="m">0</span>&rsquo;으로 푼다.</b>
<span class="m">f</span>가 <span class="m">x = c</span>에서 끊기더라도
<span class="m">g(c) = 0</span>이면 <span class="m">fg</span>는 그 점에서 연속이다.
좌극한도 우극한도 <span class="m">0</span>이 되기 때문이다.
이 성질 하나로 대부분의 조각함수 곱 문제가 풀린다.<br><br>

<b>분기점을 먼저 모두 적어 놓고 시작한다.</b>
이 문제의 분기점은 <span class="m">x = 1</span>과
<span class="m">x = a</span> 두 곳이다.
<b>각 분기점마다 조건을 하나씩 만들고, 마지막에 교집합을 잡는다</b>는
순서를 지키면 경우를 빠뜨리지 않는다.<br><br>

<b>문자가 분기점에 들어 있으면 대소 비교가 경우를 만든다.</b>
<span class="m">g</span>의 분기점이 <span class="m">x = a</span>처럼
문자로 주어지면, <span class="m">a</span>와 다른 상수의 대소에 따라
쓸 식이 달라진다.
<b><span class="m">a ≤ 1</span>인지 <span class="m">a &gt; 1</span>인지</b>로
가르는 습관을 들이면 답을 흘리지 않는다.
