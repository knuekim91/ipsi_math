---
id: DIF-J21
unit: 05-미분
topic: 삼차함수와 불연속
level: 4점
difficulty: 상
source: 2027-06모평 21번
exam: 2027-06모평
origin: 기출
core: "최대근이 튀는 순간은 값이 극솟값을 지날 때뿐이다"
tags: [삼차함수,불연속,최대근,극값]
status: seed
added: 2026-09-06
answer: 11
---

## 문제

<p>최고차항의 계수가 1인 삼차함수 <span class="m">f(x)</span>가 있다. 실수 <span class="m">t</span>에 대하여 방정식</p><span class="cond m">f(α) = f′(t) − 4t<sup>2</sup> + 4</span><p>를 만족시키는 실수 <span class="m">α</span>의 최댓값을 <span class="m">g(t)</span>라 하자. 함수 <span class="m">g(t)</span>가 <span class="m">t = 3</span>에서만 불연속이고 <span class="m">g(3) = 1</span>일 때, <span class="m">f(2)</span>의 값을 구하시오.</p>

## 발상

<span class='m'>h(t) = f′(t) − 4t<sup>2</sup> + 4</span>로 두면 <span class='m'>g(t)</span>는 <b><span class='m'>f(x) = h(t)</span>의 가장 큰 근</b>이다. <b>삼차함수에서 최대근이 갑자기 튀는 것은 값이 극솟값을 통과할 때 단 한 번</b>. 그러니 <span class='m'>h(t) = (극솟값)</span>인 <span class='m'>t</span>가 정확히 3 하나여야 한다.

## 풀이

<p><span class="step">① 문제를 다시 읽기 좋게 바꾼다.</span>
오른쪽 식을 <span class="m">t</span>만의 함수로 묶는다.</p>
<p class="m">h(t) = f′(t) − 4t<sup>2</sup> + 4</p>
<p>그러면 <span class="m">g(t)</span>는 <b>방정식 <span class="m">f(x) = h(t)</span>의 가장 큰 근</b>이다.
즉 <span class="m">y = f(x)</span>의 그래프에 <b>수평선 <span class="m">y = h(t)</span>를 긋고
가장 오른쪽 교점의 <span class="m">x</span>좌표</b>를 읽는 것이다.</p>

<p><span class="step">② 수평선을 위아래로 움직이며 최대근이 언제 튀는지 본다.</span>
최고차항의 계수가 <span class="m">1</span>인 삼차함수 <span class="m">f</span>의
극댓값을 <span class="m">M</span>(<span class="m">x = p</span>에서),
극솟값을 <span class="m">n</span>(<span class="m">x = q</span>에서, <span class="m">p &lt; q</span>)이라 하자.
수평선의 높이를 <span class="m">c</span>라 하면</p>
<p class="m">c &gt; n : 교점의 최댓값은 q보다 오른쪽</p>
<p class="m">c = n : 교점의 최댓값은 정확히 q</p>
<p class="m">c &lt; n : 교점이 하나뿐이고 그것은 p보다 왼쪽</p>
<p>즉 <b><span class="m">c</span>가 극솟값 <span class="m">n</span>을 지나는 순간
최대근이 <span class="m">q</span>에서 <span class="m">p</span> 아래로 뚝 떨어진다.</b>
반대로 <span class="m">c = M</span>을 지날 때는 교점이 늘어나기는 하지만
<b>새로 생기는 교점이 모두 왼쪽</b>이라 최대근은 그대로다.
그러므로 <b>불연속은 <span class="m">h(t) = n</span>일 때만</b> 생긴다.</p>

<p><span class="step">③ h(t)의 모양을 확인한다.</span>
<span class="m">f(x) = x<sup>3</sup> + bx<sup>2</sup> + cx + d</span>라 하면
<span class="m">f′(t) = 3t<sup>2</sup> + 2bt + c</span>이므로</p>
<p class="m">h(t) = (3t<sup>2</sup> + 2bt + c) − 4t<sup>2</sup> + 4 = −t<sup>2</sup> + 2bt + (c + 4)</p>
<p><span class="m">t<sup>2</sup></span>의 계수가 음수이므로 <b>위로 볼록한 포물선</b>이다.</p>

<p><span class="step">④ &lsquo;t = 3에서만 불연속&rsquo;을 식으로 바꾼다.</span>
②에서 불연속은 <span class="m">h(t) = n</span>인 <span class="m">t</span>에서만 생긴다고 했다.
그런 <span class="m">t</span>가 <b>딱 하나</b>여야 하는데,
위로 볼록한 포물선이 수평선 <span class="m">y = n</span>과 <b>한 점에서만 만나려면
꼭짓점에서 만나야</b> 한다.</p>
<p>꼭짓점의 <span class="m">t</span>좌표는 <span class="m">−2b/(2 × (−1)) = b</span>이므로</p>
<p class="m">b = 3</p>
<p>그때의 값이 극솟값 <span class="m">n</span>과 같다.</p>
<p class="m">n = h(3) = −9 + 2 × 3 × 3 + c + 4 = −9 + 18 + c + 4 = c + 13</p>

<p><span class="step">⑤ g(3) = 1을 쓴다.</span>
<span class="m">t = 3</span>일 때 수평선의 높이가 극솟값과 같으므로
②에 따라 최대근은 <b>극소점 <span class="m">q</span> 자체</b>다.</p>
<p class="m">q = 1</p>
<p><span class="m">f′(q) = 0</span>이므로 <span class="m">b = 3</span>을 넣은 도함수에 <span class="m">x = 1</span>을 대입한다.</p>
<p class="m">f′(x) = 3x<sup>2</sup> + 6x + c</p>
<p class="m">f′(1) = 3 + 6 + c = 9 + c = 0 → c = −9</p>
<p>확인해 보면</p>
<p class="m">f′(x) = 3x<sup>2</sup> + 6x − 9 = 3(x + 3)(x − 1)</p>
<p>이므로 극대는 <span class="m">x = −3</span>, 극소는 <span class="m">x = 1</span>로 <b>가정과 맞는다.</b></p>

<p><span class="step">⑥ d를 정한다.</span>
극솟값을 두 가지로 표현해 같게 놓는다.
④에서 <span class="m">n = c + 13 = −9 + 13 = 4</span>이고,
직접 계산하면</p>
<p class="m">n = f(1) = 1 + 3 − 9 + d = d − 5</p>
<p class="m">d − 5 = 4 → d = 9</p>
<p class="m">f(x) = x<sup>3</sup> + 3x<sup>2</sup> − 9x + 9</p>

<p><span class="step">⑦ 답을 계산한다.</span></p>
<p class="m">f(2) = 8 + 12 − 18 + 9 = 11</p>
<p class="m">답 11</p>

## 함정

<b>극댓값 <span class='m'>M</span>을 지날 때도 불연속일 것 같지만 아니다.</b> <span class='m'>c</span>가 <span class='m'>M</span>보다 조금 작아지면 근이 3개가 되지만 <b>가장 큰 근은 그대로</b>다. 새로 생긴 두 근은 모두 작은 쪽에 있다. &lsquo;최댓값&rsquo;을 묻는다는 점을 놓치면 여기서 틀린다.

## 노하우

<b>&lsquo;방정식 <span class='m'>f(x)=c</span>의 최대근&rsquo;은 c가 극솟값을 지날 때만 불연속.</b> (최소근이라면 극댓값을 지날 때다.) 그림을 수평선 하나로 그려 놓고 위아래로 움직여 보면 즉시 보인다. 그리고 <b>&lsquo;딱 한 점에서만 불연속&rsquo; = 포물선이 수평선과 꼭짓점에서 접함</b>으로 번역하는 것이 두 번째 열쇠다.
