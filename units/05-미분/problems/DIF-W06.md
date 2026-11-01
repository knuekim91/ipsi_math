---
id: DIF-W06
unit: 05-미분
topic: 극한값이 모든 실수 t에서 0이 아닐 조건으로 삼차함수 결정하기
level: 4점
difficulty: 상
source: 수학 14번 (2026-11-01 나은이 풀이 사진)
origin: 오답노트
core: "분모가 0이 되는 t 에서는 분자도 0이어야 하므로 그 t 는 0 또는 -1 로 강제된다. 남은 계수는 '다른 t 에서 극한이 0이 되는 자리'가 0 또는 -1 이어야 한다는 한 줄로 정해진다"
tags: [극한,부정형,삼차함수,인수분해,함숫값]
status: wrong
added: 2026-11-01
answer: 9
---

## 문제

<p>삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킬 때,
<span class="m">f(−3)</span>의 값은?</p>

<div class="cond">
<span class="cond m">모든 실수 t에 대하여 &nbsp; lim<sub>x→t</sub> (x + t)(x − f(t)) / (f(x) + x<sup>2</sup>) 의 값이 존재하고, 이 값은 모두 0이 아니다.</span>
</div>

<div class="choices"><span>① 7</span><span>② 8</span><span>③ 9</span>
<span>④ 10</span><span>⑤ 11</span></div>

## 발상

<b>분모가 0이 되는 자리에서 극한이 존재하려면 분자도 0이어야 한다.</b>
그 자리를 먼저 찾는다.<br><br>

<b>분모를 <span class="m">g(x) = f(x) + x<sup>2</sup></span>로 두면</b>
<span class="m">g(t) = 0</span>인 <span class="m">t</span>에서 분자
<span class="m">2t(t − f(t))</span>도 0이어야 한다.
<span class="m">f(t) = −t<sup>2</sup></span>와 <span class="m">f(t) = t</span>가 동시에 성립하므로
<span class="m">t = 0</span> 또는 <span class="m">t = −1</span>뿐이다.<br><br>

<b>그다음에는 다른 t에서 극한이 0이 되는 곳이 없어야 한다.</b>
그 자리는 <span class="m">f(t) = t</span>인 곳이다. 이 한 줄이 남은 계수를 정한다.

## 풀이

<p><span class="step">① 분모가 0인 자리를 찾는다.</span>
<span class="m">g(t) = 0</span>이면 분자 <span class="m">(2t)(t − f(t))</span>도 0이어야 한다.</p>
<p class="m">f(t) = −t<sup>2</sup> 이고 (t − f(t) = 0 이거나 t = 0)</p>
<p>그러면 <span class="m">t = 0</span> 또는 <span class="m">t = −1</span>이다.
또한 <span class="m">t = 0</span>에서 극한이 0이 되지 않으려면 분자 <span class="m">x<sup>2</sup></span>가
분모와 같은 차수로 소거되어야 하므로 <span class="m">g(x)</span>는 <span class="m">x<sup>2</sup></span>을 인수로 가진다.</p>

<p><span class="step">② g(x)의 꼴을 정한다.</span>
<span class="m">f</span>가 삼차함수이므로 <span class="m">g</span>도 삼차식이고,
<span class="m">x<sup>2</sup></span>과 <span class="m">(x + 1)</span>을 인수로 가진다.</p>
<p class="m">g(x) = c · x<sup>2</sup>(x + 1), &nbsp; f(x) = c·x<sup>3</sup> + c·x<sup>2</sup> − x<sup>2</sup></p>

<p><span class="step">③ t = −1 에서 극한을 확인한다.</span>
분자 <span class="m">(x − 1)(x + 1)</span>에서 <span class="m">x + 1</span>이 한 번 소거되고
분모에도 <span class="m">x + 1</span>이 한 번 있으므로 극한은 유한하고 0이 아니다.
<span class="m">f(−1) = −1</span>이 확인된다.</p>

<p><span class="step">④ 나머지 t에서 극한이 0이 되는 자리를 찾는다.</span>
<span class="m">t ≠ 0, −1</span>에서는 분모가 0이 아니므로 극한은 식에 그대로 대입한 값이다.
분자가 0이 되려면 <span class="m">f(t) = t</span>여야 한다.</p>
<p class="m">f(t) − t = t(t + 1)(ct − 1)</p>
<p>따라서 <span class="m">t = 1/c</span>에서 극한이 0이 된다.
이 값이 <span class="m">0</span> 또는 <span class="m">−1</span>이 아니면 조건에 어긋난다.</p>
<p class="m">1/c = −1 → c = −1</p>

<p><span class="step">⑤ f를 정한다.</span></p>
<p class="m">f(x) = −x<sup>3</sup> − 2x<sup>2</sup></p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">f(−3) = −(−27) − 2 · 9 = 27 − 18 = 9</p>
<p class="m">답 ③</p>

<p><span class="step">⑦ 확인한다.</span>
<span class="m">c = −1</span>이면 <span class="m">t ≠ 0, −1</span>에서 극한은 <span class="m">−2(t + 1)</span>이다.
<span class="m">t = 0</span>에서는 <span class="m">−1</span>, <span class="m">t = −1</span>에서는 <span class="m">2</span>이다.
모두 0이 아니다.</p>

## 함정

<b><span class="m">t = 0</span>이 분자에서 어떻게 소거되는지 놓친다.</b>
<span class="m">(x + t)(x − f(t))</span>에 <span class="m">t = 0</span>을 넣으면 <span class="m">x · (x − f(0)) = x<sup>2</sup></span>이다.
분모의 차수가 <span class="m">2</span>보다 낮으면 극한이 발산하거나 0이 된다.<br><br>

<b>c를 정하지 못하고 멈춘다.</b>
<span class="m">f(t) = t</span>의 해 <span class="m">t = 1/c</span>가 0이나 −1이 아니어야 한다는 조건을 빠뜨리면
c가 정해지지 않아 <span class="m">f(−3)</span>이 여러 값이 된다.
나은이가 적은 별표 메모 <span class="m">0, −1이 아닐 때</span>가 바로 이 확인이다.<br><br>

<b>삼차 계수를 1로 가정하면 안 된다.</b>
사진에는 최고차항의 계수 조건이 없다.
계수는 조건에서 정해져야 하고, 임의로 1을 넣으면 답이 틀린다.

## 노하우

<b>분모가 0이 되는 자리에서는 분자도 0이어야 한다.</b>
이 한 줄로 <span class="m">t</span>의 후보가 좁혀진다.
그다음에는 <b>남은 t 에서 극한이 0이 되는 자리를 식으로 찾는다.</b>

<b>극한값을 식으로 쓰면 검산이 쉽다.</b>
<span class="m">t ≠ 0, −1</span>에서 극한은 <span class="m">2t(t − f(t)) / g(t)</span>이다.
이 식을 정리해 두면 특정한 t 를 넣어 값을 바로 확인할 수 있다.
