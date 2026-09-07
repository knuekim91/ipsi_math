---
id: EXP-D19
unit: 01-지수로그
topic: 거듭제곱근과 실근의 개수
level: 3점
difficulty: 중상
source: 2027 수능완성 실전 모의고사 2회 19번
exam: 2027-수능완성
origin: 기출
core: "세제곱근이 자연수 n이라는 말은 그 수가 n의 세제곱이라는 뜻이고, 각 n마다 이차방정식의 판별식이 x의 개수를 준다"
tags: [거듭제곱근,세제곱근,판별식,실근의개수]
status: seed
added: 2026-09-07
answer: 575
---

## 문제

<p>다음 조건을 만족시키는 모든 자연수 <span class="m">a</span>의 값의 합을 구하시오.</p>

<div class="cond">
<span class="cond m">(3/2)√(−x<sup>2</sup> + ax)의 세제곱근 중 자연수가 존재하도록 하는 실수 x의 개수는 4이다.</span>
</div>

## 발상

<b>&lsquo;세제곱근 중 자연수가 존재한다&rsquo;를 식으로 옮기는 것이 첫 관문이다.</b>
실수의 세제곱근은 실수 범위에서 딱 하나뿐이다.
그 값이 자연수 <span class="m">n</span>이라는 것은,
원래 수가 <span class="m">n<sup>3</sup></span>이라는 뜻이다.</p>
<p class="m">(3/2)√(−x<sup>2</sup> + ax) = n<sup>3</sup> &nbsp; (n은 자연수)</p>

<p><b>여기서 <span class="m">n</span>을 하나 고정하면
<span class="m">x</span>에 대한 이차방정식이 하나 생긴다.</b>
근호를 없애기 위해 양변을 제곱하면 되는데,
좌변이 <span class="m">0</span> 이상이고 우변도 양수이므로
제곱해도 무연근이 생기지 않는다.<br><br>

그러면 <span class="m">n = 1, 2, 3, …</span>마다 이차방정식이 하나씩 생기고,
<b>각 방정식의 실근의 개수를 판별식으로 세어 모두 더한 것</b>이
문제에서 말하는 <span class="m">x</span>의 개수다.
그 총합이 <span class="m">4</span>가 되도록 <span class="m">a</span>를 고르면 된다.
<span class="m">n</span>이 커질수록 <span class="m">n<sup>6</sup></span>이 급격히 커져
실근이 사라지므로, 실제로 살아남는 <span class="m">n</span>은 몇 개뿐이다.

## 풀이

<p><span class="step">① 조건을 방정식으로 옮긴다.</span>
어떤 실수의 세제곱근이 자연수 <span class="m">n</span>이라는 것은
그 실수가 <span class="m">n<sup>3</sup></span>과 같다는 뜻이다.</p>
<p class="m">(3/2)√(−x<sup>2</sup> + ax) = n<sup>3</sup></p>
<p>근호 부분만 남기도록 양변에 <span class="m">2/3</span>을 곱한다.</p>
<p class="m">√(−x<sup>2</sup> + ax) = (2/3)n<sup>3</sup></p>

<p><span class="step">② 근호를 없앤다.</span>
좌변은 <span class="m">0</span> 이상이고 우변은 양수이므로
양변을 제곱해도 근이 늘어나지 않는다.</p>
<p class="m">−x<sup>2</sup> + ax = (4/9)n<sup>6</sup></p>
<p>모든 항을 좌변으로 옮겨 <span class="m">x</span>에 대한 이차방정식으로 정리한다.</p>
<p class="m">x<sup>2</sup> − ax + (4/9)n<sup>6</sup> = 0 &nbsp; … ㉠</p>
<p>이 방정식의 해 <span class="m">x</span>는
<span class="m">−x<sup>2</sup> + ax = (4/9)n<sup>6</sup> ≥ 0</span>을 자동으로 만족시키므로
<b>근호 안이 음수가 되는 문제는 생기지 않는다.</b></p>

<p><span class="step">③ 판별식으로 실근의 개수를 센다.</span>
㉠의 판별식을 <span class="m">D</span>라 하면</p>
<p class="m">D = a<sup>2</sup> − 4 × (4/9)n<sup>6</sup> = a<sup>2</sup> − (16/9)n<sup>6</sup></p>
<p><span class="m">D &gt; 0</span>이면 서로 다른 실근이 <span class="m">2</span>개,
<span class="m">D = 0</span>이면 <span class="m">1</span>개,
<span class="m">D &lt; 0</span>이면 <span class="m">0</span>개이다.
<span class="m">a</span>가 자연수이므로 부등식을 <span class="m">a</span>에 대해 정리한다.</p>
<p class="m">D ≥ 0 ⟺ a<sup>2</sup> ≥ (16/9)n<sup>6</sup> ⟺ a ≥ (4/3)n<sup>3</sup></p>

<p><span class="step">④ n의 값마다 경계를 구한다.</span>
<span class="m">n = 1, 2, 3, 4</span>에 대하여
<span class="m">(4/3)n<sup>3</sup></span>을 계산한다.</p>
<p class="m">n = 1 : (4/3) × 1 = 4/3 ≒ 1.33</p>
<p class="m">n = 2 : (4/3) × 8 = 32/3 ≒ 10.67</p>
<p class="m">n = 3 : (4/3) × 27 = 36</p>
<p class="m">n = 4 : (4/3) × 64 = 256/3 ≒ 85.33</p>

<p><span class="step">⑤ 각 n이 주는 근의 개수를 정리한다.</span>
<span class="m">a</span>가 자연수이므로 <span class="m">4/3</span>이나
<span class="m">32/3</span>과 같아질 수 없고, 따라서
<span class="m">n = 1</span>과 <span class="m">n = 2</span>에서는
근이 <span class="m">2</span>개이거나 <span class="m">0</span>개뿐이다.</p>
<p class="m">n = 1 : a ≥ 2 이면 2개, a = 1 이면 0개</p>
<p class="m">n = 2 : a ≥ 11 이면 2개, a ≤ 10 이면 0개</p>
<p><span class="m">n = 3</span>에서는 <span class="m">36</span>이 자연수이므로
<span class="m">a = 36</span>일 때 <span class="m">D = 0</span>이 되어
근이 <span class="m">1</span>개가 된다.</p>
<p class="m">n = 3 : a = 36 이면 1개, a ≥ 37 이면 2개, a ≤ 35 이면 0개</p>

<p><span class="step">⑥ 개수가 4가 되는 a의 범위를 찾는다.</span>
<span class="m">a</span>를 작은 값부터 키우며 근의 총개수를 센다.</p>
<p class="m">a = 1 : 0개</p>
<p class="m">2 ≤ a ≤ 10 : n = 1 에서만 2개 → 2개</p>
<p class="m">11 ≤ a ≤ 35 : n = 1, 2 에서 2개씩 → 4개</p>
<p class="m">a = 36 : 4개 + n = 3 의 1개 → 5개</p>
<p class="m">37 ≤ a ≤ 85 : n = 1, 2, 3 에서 2개씩 → 6개</p>
<p>서로 다른 <span class="m">n</span>에서 나온 이차방정식은 상수항
<span class="m">(4/9)n<sup>6</sup></span>이 서로 다르므로 근이 겹치지 않는다.
따라서 개수를 그대로 더하면 된다.
개수가 <span class="m">4</span>인 것은 다음 범위뿐이다.</p>
<p class="m">11 ≤ a ≤ 35</p>

<p><span class="step">⑦ 답을 만든다.</span>
<span class="m">11</span>부터 <span class="m">35</span>까지의 자연수는
<span class="m">35 − 11 + 1 = 25</span>개이다.
등차수열의 합 공식을 쓴다.</p>
<p class="m">(합) = (첫항 + 끝항) × (개수) / 2 = (11 + 35) × 25 / 2</p>
<p class="m">= 46 × 25 / 2 = 23 × 25 = 575</p>
<p class="m">답 575</p>

## 함정

<b>세제곱근을 제곱근처럼 다루면 안 된다.</b>
실수의 <b>세제곱근은 실수 범위에서 하나뿐</b>이므로,
&lsquo;세제곱근 중 자연수&rsquo;라는 표현은
<b>그 하나가 자연수인 경우</b>를 뜻한다.
제곱근처럼 두 개가 나오는 것으로 착각하면 개수가 두 배가 된다.<br><br>

<b><span class="m">a = 36</span>을 넣으면 안 된다.</b>
<span class="m">n = 3</span>에서 판별식이 <span class="m">0</span>이 되어
중근이 생기므로 근이 하나 늘어 <span class="m">5</span>개가 된다.
<b>등호가 성립하는 자리를 따로 확인하는 것</b>이 이 문제의 핵심이다.
<span class="m">n = 1, 2</span>에서는 경계값이 분수라서
자연수 <span class="m">a</span>가 그 값이 될 수 없어 중근이 생기지 않는다.<br><br>

<b><span class="m">n = 0</span>을 넣으면 안 된다.</b>
자연수는 <span class="m">1</span>부터 시작한다.
<span class="m">n = 0</span>이면 <span class="m">0</span>은 자연수가 아니다.

## 노하우

<b>&lsquo;세제곱근이 자연수&rsquo;는 &lsquo;<span class="m">n</span>의 세제곱과 같다&rsquo;로 바꾼다.</b>
거듭제곱근 조건은 언제나 <b>거듭제곱 꼴의 방정식</b>으로 옮겨야
계산할 수 있는 식이 된다.<br><br>

<b>개수 조건은 판별식으로 세고 표로 정리한다.</b>
<span class="m">n</span>마다 방정식이 하나씩 생기는 구조에서는,
<span class="m">n</span>을 키우며 <b>경계값을 먼저 계산해 두고</b>
<span class="m">a</span>를 키우며 누적 개수를 세는 것이 가장 빠르다.
<span class="m">n<sup>3</sup></span>은 급격히 커지므로
확인할 <span class="m">n</span>은 서너 개면 충분하다.<br><br>

<b>경계값이 정수인지 분수인지를 반드시 본다.</b>
<span class="m">(4/3)n<sup>3</sup></span>이 정수가 되는 것은
<span class="m">n<sup>3</sup></span>이 <span class="m">3</span>의 배수일 때,
곧 <span class="m">n</span>이 <span class="m">3</span>의 배수일 때다.
그때만 중근이 생겨 개수가 하나 늘어난다.
이 관찰이 <span class="m">a = 36</span>을 걸러 낸다.
