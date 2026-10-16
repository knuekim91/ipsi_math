---
id: DIF-W04-V1
parent: DIF-W04
unit: 05-미분
topic: 실근의 개수가 같을 조건과 사차함수 결정
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W04 변형 · 극댓값이 4인 경우)
origin: 유사문항
core: "g의 극댓값이 b²/(4a)로 바뀌면 표의 경계가 그만큼 옮겨갈 뿐, 세우는 식의 모양은 그대로다"
tags: [실근의개수,사차함수,절댓값,경계값,그래프개형]
status: variant
added: 2026-10-16
answer: ③
---

## 문제

<p>최고차항의 계수가 양수이고 <span class="m">f′(0) = 0</span>인 사차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키지 <b>않는</b> 실수
<span class="m">t</span>가 하나뿐일 때, <span class="m">f(−3)</span>의 값은?</p>

<div class="cond">
<span class="cond m">x에 대한 두 방정식 |x|(x + 4) = t, &nbsp; |x|(x + 4) = f(t)의 서로 다른 실근의 개수가 같다.</span>
</div>

<div class="choices"><span>① 28</span><span>② 30</span><span>③ 32</span>
<span>④ 34</span><span>⑤ 36</span></div>

## 발상

<b>틀은 원문항과 똑같다. 바뀐 것은 <span class="m">g</span>의 극댓값과
묻는 점뿐이다.</b><br><br>

<b>먼저 극댓값을 다시 구해야 한다.</b>
<span class="m">g(x) = |x|(x + 4)</span>의 왼쪽 조각은
<span class="m">−x<sup>2</sup> − 4x</span>이고,
완전제곱으로 고치면 <span class="m">x = −2</span>에서
<b>극대 <span class="m">4</span></b>다.
원문항의 <span class="m">2</span>가 <span class="m">4</span>로 바뀌었으므로
<b>표의 경계도 <span class="m">0</span>과 <span class="m">4</span></b>가 된다.<br><br>

<b>그 뒤로는 모양이 그대로다.</b>
<span class="m">f(0) = 4</span>, <span class="m">f(t) − 4</span>가
<span class="m">t = 0</span>에서 삼중근,
그리고 <span class="m">(0, 4)</span>에서의 최솟값이 정확히
<span class="m">0</span>. 이 세 줄이 계수를 정한다.<br><br>

<b>묻는 점이 음수라는 것만 주의한다.</b>
<span class="m">f(−3)</span>이므로 <span class="m">t<sup>3</sup></span>과
<span class="m">t − 4</span>가 모두 음수가 되어 곱이 양수가 된다.

## 풀이

<p><span class="step">① g의 개형과 극댓값을 구한다.</span></p>
<p class="m">x ≥ 0 : g(x) = x<sup>2</sup> + 4x</p>
<p class="m">x &lt; 0 : g(x) = −x<sup>2</sup> − 4x = −(x + 2)<sup>2</sup> + 4</p>
<p>왼쪽 조각은 <span class="m">x = −2</span>에서 극대
<span class="m">4</span>이고, <span class="m">x = 0</span>에서 극소
<span class="m">0</span>이다.</p>

<p><span class="step">② 실근의 개수를 표로 만든다.</span></p>
<p class="m">k &lt; 0 → 1개 &nbsp;/&nbsp; k = 0 → 2개 &nbsp;/&nbsp; 0 &lt; k &lt; 4 → 3개</p>
<p class="m">k = 4 → 2개 &nbsp;/&nbsp; k &gt; 4 → 1개</p>

<p><span class="step">③ f가 만족시켜야 할 것을 적는다.</span></p>
<p class="m">0 &lt; t &lt; 4 이면 0 &lt; f(t) &lt; 4</p>
<p class="m">t = 0 또는 t = 4 이면 f(t) = 0 또는 f(t) = 4</p>
<p class="m">그 밖에서는 f(t)가 [0, 4] 밖</p>

<p><span class="step">④ f의 꼴을 정한다.</span>
<span class="m">t = 0</span>의 좌우에서 안과 밖이 갈리므로
<span class="m">f(0)</span>은 <span class="m">0</span> 또는
<span class="m">4</span>인데, <span class="m">f(0) = 0</span>이면
<span class="m">f′(0) = 0</span> 때문에 부호가 바뀌지 않아 어긋난다.
따라서 <span class="m">f(0) = 4</span>이고,
<span class="m">f − 4</span>가 <span class="m">t = 0</span>에서
삼중근을 가져야 부호가 바뀐다.
원문항과 같은 이유로 남은 인수의 근은 오른쪽 경계와 같아야 한다.</p>
<p class="m">f(t) = a t<sup>3</sup>(t − 4) + 4 &nbsp; (a &gt; 0)</p>

<p><span class="step">⑤ 최솟값이 0이 되도록 a를 정한다.</span>
<span class="m">h(t) = t<sup>3</sup>(t − 4) = t<sup>4</sup> − 4t<sup>3</sup></span>을 미분한다.</p>
<p class="m">h′(t) = 4t<sup>3</sup> − 12t<sup>2</sup> = 4t<sup>2</sup>(t − 3)</p>
<p><span class="m">(0, 4)</span>에서 <span class="m">t = 3</span>이 극소이고</p>
<p class="m">h(3) = 27 × (3 − 4) = −27</p>
<p>이므로 <span class="m">f</span>의 최솟값은
<span class="m">4 − 27a</span>이다. 이것이
<span class="m">0</span>일 때만 어긋나는 점이
<span class="m">t = 3</span> 하나가 된다.</p>
<p class="m">4 − 27a = 0 → a = 4/27</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">f(t) = (4/27)t<sup>3</sup>(t − 4) + 4</p>
<p class="m">f(−3) = (4/27) × (−27) × (−3 − 4) + 4</p>
<p>두 음수의 곱이 양수가 된다.</p>
<p class="m">= (4/27) × (−27) × (−7) + 4 = 28 + 4 = 32</p>
<p class="m">답 ③</p>

## 함정

<b>극댓값을 <span class="m">2</span>로 그대로 쓰면 전부 틀린다.</b>
<span class="m">g(x) = |x|(x + 4)</span>는
<span class="m">x</span>의 계수가 <span class="m">1</span>이라
완전제곱이 <span class="m">−(x + 2)<sup>2</sup> + 4</span>가 된다.
<b>극댓값은 <span class="m">g</span>마다 다시 구한다.</b><br><br>

<b>④번 선지 <span class="m">34</span>는 원문항의 답이다.</b>
숫자만 보고 고르면 걸린다.<br><br>

<b><span class="m">f(−3)</span>에서 부호를 틀리기 쉽다.</b>
<span class="m">(−3)<sup>3</sup> = −27</span>이고
<span class="m">−3 − 4 = −7</span>이다.
<b>음수 곱하기 음수가 양수</b>라는 것을 확인하고 쓴다.
부호를 하나라도 놓치면 <span class="m">−24</span>가 나온다.

## 노하우

<b><span class="m">g(x) = |x|(ax + b)</span>의 극댓값은
<span class="m">b<sup>2</sup>/(4a)</span>다.</b>
왼쪽 조각 <span class="m">−ax<sup>2</sup> − bx</span>를 완전제곱으로 고치면
<span class="m">x = −b/(2a)</span>에서 그 값이 나온다.
<b>이 공식을 외워 두면 개형을 그리지 않고도 표의 경계를 바로 적을 수 있다.</b><br><br>

<b>극댓값을 <span class="m">m</span>이라 하면 답의 모양이 정해진다.</b>
<span class="m">f(t) = a t<sup>3</sup>(t − m) + m</span>이고,
<span class="m">h(t) = t<sup>3</sup>(t − m)</span>의 극소는
<span class="m">t = 3m/4</span>에서 생긴다.
<b>한 번 구조를 익히면 숫자만 갈아 끼우면 된다.</b><br><br>

<b>묻는 점이 음수면 부호를 따로 적어 둔다.</b>
<span class="m">t<sup>3</sup></span>의 부호와
<span class="m">t − m</span>의 부호를 <b>각각 적고 곱한다.</b>
머릿속으로 한꺼번에 하면 꼭 하나를 놓친다.
