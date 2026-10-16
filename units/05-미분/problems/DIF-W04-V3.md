---
id: DIF-W04-V3
parent: DIF-W04
unit: 05-미분
topic: 실근의 개수가 같을 조건과 사차함수 결정
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W04 변형 · 최고차항의 계수를 묻기)
origin: 유사문항
core: "f(3)만 외워 두면 못 푼다. 계수 a 자체가 답이므로 f를 실제로 복원했는지가 드러난다"
tags: [실근의개수,사차함수,절댓값,경계값,서로소]
status: variant
added: 2026-10-16
answer: 59
---

## 문제

<p>최고차항의 계수가 양수이고 <span class="m">f′(0) = 0</span>인 사차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키지 <b>않는</b> 실수
<span class="m">t</span>가 하나뿐이다.</p>

<div class="cond">
<span class="cond m">x에 대한 두 방정식 |x|(2x + 4) = t, &nbsp; |x|(2x + 4) = f(t)의 서로 다른 실근의 개수가 같다.</span>
</div>

<p>이때 <span class="m">f(x)</span>의 최고차항의 계수는
<span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>설정은 원문항과 똑같다. 묻는 것만 다르다.</b>
원문항은 <span class="m">f(3)</span>을 물었고 여기서는
<b>최고차항의 계수</b>를 묻는다.<br><br>

<b>그런데 이 차이가 작지 않다.</b>
<span class="m">f(3) = 34</span>라는 답만 외운 사람은
여기서 손도 못 댄다. <b><span class="m">f</span>를 실제로 복원했는지</b>가
그대로 드러나는 문항이다.<br><br>

<b>계수 <span class="m">a</span>는 풀이의 마지막에서 두 번째 단계에서 나온다.</b>
<span class="m">f(t) = a t<sup>3</sup>(t − 2) + 2</span>로 꼴을 잡고,
<span class="m">(0, 2)</span>에서의 최솟값을 <span class="m">0</span>으로 놓으면
바로 <span class="m">a</span>가 떨어진다.
<b>원문항은 거기서 한 걸음 더 가 <span class="m">f(3)</span>을 구한 것</b>이다.

## 풀이

<p><span class="step">① g의 개형을 그린다.</span></p>
<p class="m">x ≥ 0 : g(x) = 2x<sup>2</sup> + 4x</p>
<p class="m">x &lt; 0 : g(x) = −2(x + 1)<sup>2</sup> + 2</p>
<p><span class="m">x = −1</span>에서 극대 <span class="m">2</span>,
<span class="m">x = 0</span>에서 극소 <span class="m">0</span>이다.</p>

<p><span class="step">② 실근의 개수를 표로 만든다.</span></p>
<p class="m">k &lt; 0 → 1개 &nbsp;/&nbsp; k = 0 → 2개 &nbsp;/&nbsp; 0 &lt; k &lt; 2 → 3개</p>
<p class="m">k = 2 → 2개 &nbsp;/&nbsp; k &gt; 2 → 1개</p>
<p>개수가 같은 것끼리 묶으면 다음 세 묶음이다.</p>
<p class="m">실근 1개 : k &lt; 0, k &gt; 2</p>
<p class="m">실근 2개 : k = 0, k = 2</p>
<p class="m">실근 3개 : 0 &lt; k &lt; 2</p>

<p><span class="step">③ f의 꼴을 정한다.</span>
<span class="m">t = 0</span>의 왼쪽에서는
<span class="m">f(t)</span>가 <span class="m">[0, 2]</span> 밖,
오른쪽에서는 안쪽이어야 한다.
<span class="m">f(0) = 0</span>이면
<span class="m">f′(0) = 0</span> 때문에 부호가 바뀌지 않아 어긋나므로
<span class="m">f(0) = 2</span>이고,
<span class="m">f − 2</span>는 <span class="m">t = 0</span>에서 삼중근을 갖는다.
남은 인수의 근이 오른쪽 경계보다 크면 어긋나는 곳이 구간이 되므로
그 근은 <span class="m">2</span>다.</p>
<p class="m">f(t) = a t<sup>3</sup>(t − 2) + 2 &nbsp; (a &gt; 0)</p>

<p><span class="step">④ 최솟값을 0으로 놓는다.</span></p>
<p class="m">h(t) = t<sup>3</sup>(t − 2) = t<sup>4</sup> − 2t<sup>3</sup></p>
<p class="m">h′(t) = 4t<sup>3</sup> − 6t<sup>2</sup> = 2t<sup>2</sup>(2t − 3)</p>
<p><span class="m">(0, 2)</span>에서 <span class="m">t = 3/2</span>이 극소이고</p>
<p class="m">h(3/2) = (27/8)(−1/2) = −27/16</p>
<p>이므로 <span class="m">f</span>의 최솟값은
<span class="m">2 − 27a/16</span>이다.
이 값이 <span class="m">0</span>일 때만 어긋나는 점이 하나가 된다.</p>
<p class="m">2 − 27a/16 = 0</p>
<p>양변에 <span class="m">16</span>을 곱한다.</p>
<p class="m">32 − 27a = 0 → a = 32/27</p>

<p><span class="step">⑤ 답을 만든다.</span>
<span class="m">q/p = 32/27</span>이고
<span class="m">32 = 2<sup>5</sup></span>,
<span class="m">27 = 3<sup>3</sup></span>이라 서로소이므로
<span class="m">q = 32</span>, <span class="m">p = 27</span>이다.</p>
<p class="m">p + q = 27 + 32 = 59</p>
<p class="m">답 59</p>

## 함정

<b><span class="m">p</span>와 <span class="m">q</span>의 자리를 바꾸면 안 된다.</b>
최고차항의 계수가 <span class="m">q/p</span>이므로
<b>분자가 <span class="m">q</span>, 분모가 <span class="m">p</span></b>다.
이 문제는 합을 묻기에 결과가 같지만, 곱이나 차를 물었다면 달라진다.<br><br>

<b>최고차항의 계수를 <span class="m">f</span>를 전개해서 확인한다.</b></p>
<p class="m">f(t) = (32/27)(t<sup>4</sup> − 2t<sup>3</sup>) + 2 = (32/27)t<sup>4</sup> − (64/27)t<sup>3</sup> + 2</p>
<p><span class="m">t<sup>4</sup></span>의 계수가
<span class="m">32/27</span>로 <span class="m">a</span>와 같다.
<b><span class="m">a t<sup>3</sup>(t − 2)</span>에서 <span class="m">a</span>가
그대로 최고차항의 계수</b>가 되는 것을 확인하고 넘어간다.<br><br>

<b>서로소인지 반드시 확인한다.</b>
<span class="m">64/54</span>처럼 약분이 덜 된 꼴로 두면
<span class="m">p + q = 118</span>이 되어 틀린다.

## 노하우

<b>같은 설정에서 묻는 것이 바뀌면 어디까지 갔는지가 드러난다.</b>
<span class="m">f(3)</span>은 마지막 한 걸음이고
<span class="m">a</span>는 그 직전이다.
<b>풀이를 다 하고 나서 &lsquo;무엇을 물었는지&rsquo; 다시 읽는 습관</b>을 들이면
엉뚱한 값을 적는 일이 없다.<br><br>

<b>인수분해된 꼴에서 최고차항의 계수를 바로 읽는다.</b>
<span class="m">a t<sup>3</sup>(t − m) + m</span>에서
<span class="m">t<sup>4</sup></span>이 나오는 길은
<span class="m">a t<sup>3</sup> × t</span> 하나뿐이므로
<b>최고차항의 계수는 <span class="m">a</span></b>다.
전개할 필요가 없다.<br><br>

<b>&lsquo;서로소인 자연수&rsquo;는 끝까지 약분하라는 뜻이다.</b>
답을 적기 전에 <b>분모와 분자의 공약수가 없는지</b> 한 번 더 본다.
<span class="m">32</span>와 <span class="m">27</span>은
각각 <span class="m">2</span>와 <span class="m">3</span>의 거듭제곱이라
서로소임이 한눈에 보인다.
