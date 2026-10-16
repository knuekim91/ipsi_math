---
id: DIF-W04
unit: 05-미분
topic: 실근의 개수가 같을 조건과 사차함수 결정
level: 4점
difficulty: 상
source: 나은이가 가져온 문제 (수학 15번)
exam: 오답노트
origin: 기출
core: "g(x)=k의 실근 개수를 k의 구간별 표로 만들면, 조건은 t와 f(t)가 같은 칸에 있다는 뜻이 된다. 예외가 꼭 하나이려면 f의 최솟값이 경계값에 정확히 닿아야 한다"
tags: [실근의개수,사차함수,절댓값,경계값,그래프개형]
status: wrong
added: 2026-10-16
answer: ③
---

## 문제

<p>최고차항의 계수가 양수이고 <span class="m">f′(0) = 0</span>인 사차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키지 <b>않는</b> 실수
<span class="m">t</span>가 하나뿐일 때, <span class="m">f(3)</span>의 값은?</p>

<div class="cond">
<span class="cond m">x에 대한 두 방정식 |x|(2x + 4) = t, &nbsp; |x|(2x + 4) = f(t)의 서로 다른 실근의 개수가 같다.</span>
</div>

<div class="choices"><span>① 30</span><span>② 32</span><span>③ 34</span>
<span>④ 36</span><span>⑤ 38</span></div>

## 발상

<b><span class="m">g(x) = |x|(2x + 4)</span>라 두고
<span class="m">g(x) = k</span>의 실근 개수를
<span class="m">k</span>의 구간별로 적는 것</b>이 모든 것의 출발이다.
이 표만 있으면 문제의 조건이 아주 단순한 말로 바뀐다.<br><br>

<b>조건은 &lsquo;<span class="m">t</span>와 <span class="m">f(t)</span>가
표의 같은 칸에 있다&rsquo;는 뜻이다.</b>
실근의 개수가 같다는 것은 두 수가 같은 개수를 주는 구간에 들어 있다는 말이기 때문이다.<br><br>

<b>그다음은 &lsquo;예외가 꼭 하나&rsquo;라는 말을 읽는 것이다.</b>
<span class="m">f</span>는 연속이므로, 조건을 어기는 <span class="m">t</span>가
하나라도 생기면 보통은 <b>그 둘레의 구간 전체가 함께 어긋난다.</b>
어긋나는 곳이 <b>딱 한 점</b>이려면, <span class="m">f</span>의 그래프가
칸의 경계선에 <b>스치듯 한 번만 닿아야</b> 한다.
곧 <b>최솟값이 경계값과 정확히 같아지는 순간</b>이고, 그것이 계수를 하나로 정한다.

## 풀이

<p><span class="step">① g의 개형을 그린다.</span>
<span class="m">g(x) = |x|(2x + 4)</span>를 절댓값을 벗겨 두 조각으로 쓴다.</p>
<p class="m">x ≥ 0 : g(x) = 2x<sup>2</sup> + 4x</p>
<p class="m">x &lt; 0 : g(x) = −2x<sup>2</sup> − 4x = −2(x + 1)<sup>2</sup> + 2</p>
<p>오른쪽 조각은 <span class="m">0</span>에서 시작해 계속 커지고,
왼쪽 조각은 <span class="m">x = −1</span>에서 <b>극대 <span class="m">2</span></b>를 갖는
위로 볼록한 포물선이다.
<span class="m">x = 0</span>에서 두 조각이 모두 <span class="m">0</span>이라
<b>극소 <span class="m">0</span></b>이 된다.</p>

<p><span class="step">② 실근의 개수를 표로 만든다.</span>
수평선 <span class="m">y = k</span>를 위아래로 움직이며 교점을 센다.</p>
<p class="m">k &lt; 0 → 1개 &nbsp;/&nbsp; k = 0 → 2개 &nbsp;/&nbsp; 0 &lt; k &lt; 2 → 3개</p>
<p class="m">k = 2 → 2개 &nbsp;/&nbsp; k &gt; 2 → 1개</p>
<p><b>개수가 같은 것끼리 묶는다.</b></p>
<p class="m">1개 : k &lt; 0 또는 k &gt; 2</p>
<p class="m">2개 : k = 0 또는 k = 2</p>
<p class="m">3개 : 0 &lt; k &lt; 2</p>

<p><span class="step">③ 조건을 f에 대한 말로 바꾼다.</span>
<span class="m">t</span>와 <span class="m">f(t)</span>가 같은 묶음에 있어야 한다.</p>
<p class="m">t &lt; 0 또는 t &gt; 2 이면 f(t) &lt; 0 또는 f(t) &gt; 2</p>
<p class="m">t = 0 또는 t = 2 이면 f(t) = 0 또는 f(t) = 2</p>
<p class="m">0 &lt; t &lt; 2 이면 0 &lt; f(t) &lt; 2</p>

<p><span class="step">④ t = 0 근처를 보고 f(0)을 정한다.</span>
<span class="m">f</span>는 연속이므로 <span class="m">t = 0</span>의
좌우에서 ③의 요구가 이어져야 한다.
왼쪽에서는 <span class="m">f(t)</span>가
<span class="m">[0, 2]</span> 밖이어야 하고,
오른쪽에서는 안쪽이어야 한다.
<span class="m">t = 0</span>에서의 값은
<span class="m">0</span> 또는 <span class="m">2</span>다.<br>
<b><span class="m">f(0) = 0</span>이면 안 된다.</b>
그러려면 <span class="m">t = 0</span> 왼쪽에서
<span class="m">f(t) &lt; 0</span>, 오른쪽에서
<span class="m">f(t) &gt; 0</span>이어야 하는데,
<span class="m">f(0) = 0</span>이고 <span class="m">f′(0) = 0</span>이면
<span class="m">f</span>는 <span class="m">0</span>을 중근으로 가져
<b>부호가 바뀌지 않는다.</b> 삼중근으로 만들면 부호는 바뀌지만,
그때는 <span class="m">t</span>가 음수인 쪽에서
<span class="m">f</span>가 <span class="m">0</span>부터 커지며
<span class="m">[0, 2]</span>를 통째로 지나가 어긋나는 곳이 구간이 된다.</p>
<p class="m">따라서 f(0) = 2</p>

<p><span class="step">⑤ f의 꼴을 정한다.</span>
<span class="m">t = 0</span> 왼쪽에서는
<span class="m">f(t) &gt; 2</span>, 오른쪽에서는
<span class="m">f(t) &lt; 2</span>여야 하므로
<span class="m">f(t) − 2</span>는 <span class="m">t = 0</span>에서
<b>부호가 바뀐다.</b>
그런데 <span class="m">f′(0) = 0</span>이므로
<span class="m">t = 0</span>은 <span class="m">f − 2</span>의
<b>삼중근</b>이어야 한다. 최고차항의 계수를
<span class="m">a (a &gt; 0)</span>라 하면</p>
<p class="m">f(t) − 2 = a t<sup>3</sup>(t − c)</p>
<p><span class="m">0 &lt; t &lt; 2</span>에서
<span class="m">f(t) &lt; 2</span>여야 하므로
<span class="m">t<sup>3</sup>(t − c) &lt; 0</span>, 곧
<span class="m">c ≥ 2</span>이다.
한편 <span class="m">c &gt; 2</span>이면
<span class="m">2 &lt; t &lt; c</span>에서
<span class="m">f(t) &lt; 2</span>인데 이 구간에서는
<span class="m">[0, 2]</span> 밖이어야 하므로
<span class="m">f(t) &lt; 0</span>이어야 하고,
<span class="m">f(c) = 2</span>이므로 그 사이에서
<span class="m">f</span>가 <span class="m">[0, 2]</span>를 지나
<b>어긋나는 곳이 구간이 된다.</b> 따라서</p>
<p class="m">c = 2, &nbsp; f(t) = a t<sup>3</sup>(t − 2) + 2</p>

<p><span class="step">⑥ 예외가 하나가 되도록 a를 정한다.</span>
남은 요구는 <span class="m">0 &lt; t &lt; 2</span>에서
<span class="m">f(t) &gt; 0</span>이다.
<span class="m">h(t) = t<sup>3</sup>(t − 2) = t<sup>4</sup> − 2t<sup>3</sup></span>의
<span class="m">(0, 2)</span>에서의 최솟값을 찾는다.</p>
<p class="m">h′(t) = 4t<sup>3</sup> − 6t<sup>2</sup> = 2t<sup>2</sup>(2t − 3)</p>
<p><span class="m">t = 3/2</span>에서 극소이고</p>
<p class="m">h(3/2) = (3/2)<sup>3</sup>(3/2 − 2) = (27/8)(−1/2) = −27/16</p>
<p>이다. 따라서 <span class="m">(0, 2)</span>에서
<span class="m">f</span>의 최솟값은
<span class="m">2 − 27a/16</span>이다.<br>
이 값이 <b>양수면 어긋나는 곳이 하나도 없고</b>,
<b>음수면 <span class="m">f(t) &lt; 0</span>인 구간이 생겨 무수히 많아진다.</b>
<b>정확히 <span class="m">0</span>일 때만</b>
<span class="m">t = 3/2</span> 한 점에서
<span class="m">f(t) = 0</span>이 되어
<span class="m">N(t) = 3</span>, <span class="m">N(f(t)) = 2</span>로 어긋난다.</p>
<p class="m">2 − 27a/16 = 0 → a = 32/27</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">f(t) = (32/27)t<sup>3</sup>(t − 2) + 2</p>
<p class="m">f(3) = (32/27) × 27 × (3 − 2) + 2 = 32 + 2 = 34</p>
<p class="m">답 ③</p>

## 함정

<b>실근의 개수를 세면서 <span class="m">k = 0</span>과
<span class="m">k = 2</span>를 구간에 섞어 넣으면 안 된다.</b>
이 두 값은 <b>각각 따로 한 칸</b>이다.
<span class="m">k = 2</span>에서는 왼쪽 포물선이 꼭짓점에서 접해 근이 하나로 줄고,
<span class="m">k = 0</span>에서는 <span class="m">x = 0</span>이 겹쳐 둘이 된다.
<b>경계값에서 개수가 달라지는 것이 이 문제의 뼈대</b>다.<br><br>

<b>&lsquo;예외가 하나&rsquo;를 &lsquo;아무 데나 하나 어긋나면 된다&rsquo;로 읽으면 안 된다.</b>
<span class="m">f</span>가 연속이라 한 점에서 어긋나기 시작하면
보통 그 둘레가 함께 어긋난다.
<b>스치듯 한 번만 닿는 자리</b>를 찾아야 하고, 그것이 등호를 준다.<br><br>

<b><span class="m">f(0) = 0</span>인 경우를 그냥 버리면 안 된다.</b>
왜 안 되는지 ④에서 확인하고 넘어가야 한다.
<span class="m">f′(0) = 0</span>이라는 조건이 바로 이 갈래를 막기 위해 들어 있다.<br><br>

<b><span class="m">f(3)</span>을 구할 때 <span class="m">27</span>이 약분되는 것을 본다.</b>
<span class="m">a = 32/27</span>에 <span class="m">3<sup>3</sup> = 27</span>이 곱해져
깔끔한 수가 된다. <b>문제가 <span class="m">f(3)</span>을 물은 이유</b>가 여기 있다.

## 노하우

<b>절댓값이 섞인 함수는 조각으로 갈라 개형부터 그린다.</b>
<span class="m">|x|</span>가 붙으면 <span class="m">x = 0</span>에서 꺾이고,
그 꺾인 자리가 <b>극값</b>이 되는 일이 많다.
개형을 그린 뒤 <b>수평선을 위아래로 움직이며 교점을 세는 것</b>이
실근 개수 문제의 정해진 수순이다.<br><br>

<b>&lsquo;개수가 같다&rsquo;는 조건은 구간을 묶는 작업이다.</b>
개수표를 만들고 <b>같은 개수끼리 한 묶음</b>으로 보면,
조건이 &lsquo;<span class="m">t</span>와 <span class="m">f(t)</span>가 같은 묶음&rsquo;이라는
한 줄로 줄어든다. 표를 만들지 않고 머리로 하려 하면 반드시 샌다.<br><br>

<b>&lsquo;조건을 만족시키지 않는 것이 하나뿐&rsquo;은 등호를 준다.</b>
연속함수에서 <b>예외가 유한 개</b>라는 말은
거의 언제나 <b>그래프가 경계에 접한다</b>는 뜻이다.
&lsquo;하나뿐&rsquo;, &lsquo;오직 한 개&rsquo;, &lsquo;단 하나&rsquo; 같은 말이 보이면
<b>최댓값이나 최솟값을 경계값과 같다고 놓는다.</b><br><br>

<b>조건의 개수와 미지수의 개수를 맞춰 본다.</b>
사차함수의 미지수는 다섯 개인데,
<span class="m">f′(0) = 0</span>, <span class="m">f(0) = 2</span>,
삼중근, <span class="m">c = 2</span>, 최솟값이 <span class="m">0</span>이
차례로 하나씩 묶어 결국 하나도 남지 않는다.
<b>조건을 다 썼는지 세어 보는 것</b>이 마지막 점검이다.
