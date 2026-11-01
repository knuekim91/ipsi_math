---
id: DIF-W06-V2
parent: DIF-W06
unit: 05-미분
topic: 분모의 부호가 바뀐 극한 조건으로 삼차함수 결정하기 (심화)
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W06 변형 · 분모를 f(x)−x² 로 바꿔 근의 위치를 옮김)
origin: 유사문항
core: "분모가 0이 되는 자리에서 분자도 0이어야 한다는 원리는 그대로다. 분모를 f+x² 에서 f−x² 로 바꾸면 근이 0 과 1 로 옮겨가므로 식을 새로 세워야 한다"
tags: [극한,부정형,삼차함수,인수분해,함숫값]
status: variant
added: 2026-11-01
answer: 45
---

## 문제

<p>최고차항의 계수가 실수인 삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킬 때,
<span class="m">f(−3)</span>의 값을 구하시오.</p>

<div class="cond">
<span class="cond m">모든 실수 t에 대하여 &nbsp; lim<sub>x→t</sub> (x + t)(x − f(t)) / (f(x) − x<sup>2</sup>) 의 값이 존재하고, 이 값은 모두 0이 아니다.</span>
</div>

## 발상

<b>원리는 원문항과 같다.</b>
분모가 0이 되는 자리에서는 분자도 0이어야 한다.
<b>다만 분모가 <span class="m">f(x) − x<sup>2</sup></span>로 바뀌었으므로 근이 옮겨간다.</b><br><br>

<b>분모가 0이 되는 t를 다시 찾는다.</b>
<span class="m">f(t) = t<sup>2</sup></span>이고 분자 <span class="m">2t(t − f(t))</span>도 0이어야 하므로
<span class="m">t</span>의 후보는 <span class="m">0</span>과 <span class="m">1</span>이다.
원문항의 <span class="m">−1</span>이 <span class="m">1</span>로 바뀌었다.

## 풀이

<p><span class="step">① 분모가 0이 되는 자리를 찾는다.</span>
<span class="m">g(x) = f(x) − x<sup>2</sup></span>라 하자.
<span class="m">g(t) = 0</span>이면 분자 <span class="m">2t(t − f(t)) = 2t(t − t<sup>2</sup>)</span>도 0이어야 하므로
<span class="m">t = 0</span> 또는 <span class="m">t = 1</span>이다.
또 <span class="m">t = 0</span>에서 극한이 0이 되지 않으려면 <span class="m">f(0) = 0</span>이고
<span class="m">g</span>는 <span class="m">x<sup>2</sup></span>을 인수로 가진다.</p>

<p><span class="step">② g의 꼴을 정한다.</span>
최고차항 계수를 <span class="m">c</span>라 하면 <span class="m">g(x) = c·x<sup>2</sup>(x − 1)</span>이고</p>
<p class="m">f(x) = c·x<sup>3</sup> − c·x<sup>2</sup> + x<sup>2</sup></p>

<p><span class="step">③ 나머지 t에서 극한이 0이 되지 않아야 한다.</span>
<span class="m">f(t) = t</span>이면 분자가 0이 되므로 이 t는 <span class="m">0</span>이나 <span class="m">1</span>이어야 한다.</p>
<p class="m">f(t) − t = t(t − 1)(ct + 1)</p>
<p>따라서 <span class="m">t = −1/c</span>가 <span class="m">0</span> 또는 <span class="m">1</span>이어야 한다.</p>
<p class="m">−1/c = 1 → c = −1</p>

<p><span class="step">④ f를 정하고 f(−3)을 구한다.</span></p>
<p class="m">f(x) = −x<sup>3</sup> + 2x<sup>2</sup></p>
<p class="m">f(−3) = 27 + 18 = 45</p>
<p class="m">답 45</p>

<p><span class="step">⑤ 확인한다.</span>
<span class="m">t = 1</span>에서는 <span class="m">f(1) = 1</span>이고 극한은 <span class="m">(x + 1)(x − 1) / (−x<sup>2</sup>(x − 1))</span>이므로 <span class="m">−2</span>이다.
<span class="m">t = 0</span>에서는 극한이 <span class="m">1</span>이다. 둘 다 0이 아니다. ✓</p>

## 함정

<b>분모를 <span class="m">f + x²</span>로 읽으면 원문항 답 <span class="m">9</span>가 나온다.</b>
이 변형은 부호가 바뀌었으므로 근이 <span class="m">0</span>과 <span class="m">1</span>로 옮겨 간다.
<b>원문항의 <span class="m">−1</span>을 그대로 옮기면 틀린다.</b><br><br>

<b>c = −1을 구한 뒤 <span class="m">f(x)</span>를 다시 쓰지 않는다.</b>
<span class="m">f(x) = c x<sup>3</sup> − c x<sup>2</sup> + x<sup>2</sup></span>에서
<span class="m">c = −1</span>을 넣으면 <span class="m">x<sup>2</sup></span>의 계수가 <span class="m">+2</span>가 된다.
부호를 바꾸는 것을 빠뜨리기 쉽다.

## 노하우

<b>분모가 <span class="m">f(x) ± x<sup>2</sup></span>꼴이면 그 식의 근 위치부터 확인한다.</b>
<span class="m">+</span>이면 <span class="m">t = −1</span>, <span class="m">−</span>이면 <span class="m">t = 1</span>이 기준이 된다.
나머지 과정은 같다.
