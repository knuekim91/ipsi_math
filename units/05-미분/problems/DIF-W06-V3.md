---
id: DIF-W06-V3
parent: DIF-W06
unit: 05-미분
topic: 극한값을 특정한 점에서 구하기 (구하는 대상 바꾸기)
level: 4점
difficulty: 중상
source: 자체 개발 (DIF-W06 변형 · 함수 대신 극한값을 묻기)
origin: 유사문항
core: "조건에서 함수를 정한 뒤, 극한을 일반식으로 정리해 두면 어떤 t 에서든 값을 바로 읽는다. 함수를 찾는 것보다 극한의 꼴을 쓸 수 있는지가 관건이다"
tags: [극한,부정형,삼차함수,인수분해,극한값]
status: variant
added: 2026-11-01
answer: -6
---

## 문제

<p>삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킨다.</p>

<div class="cond">
<span class="cond m">모든 실수 t에 대하여 &nbsp; lim<sub>x→t</sub> (x + t)(x − f(t)) / (f(x) + x<sup>2</sup>) 의 값이 존재하고, 이 값은 모두 0이 아니다.</span>
</div>

<p>이때 <span class="m">lim<sub>x→2</sub> (x + 2)(x − f(2)) / (f(x) + x<sup>2</sup>)</span>의 값을 구하시오.</p>

## 발상

<b>이 조건을 만족시키는 함수는 하나뿐이다.</b>
원문항에서 <span class="m">f(x) = −x<sup>3</sup> − 2x<sup>2</sup></span>임을 이미 구했다.
이 문항은 그 함수를 쓴 뒤 <b>극한값 자체</b>를 묻는다.<br><br>

<b>극한은 함수를 대입하기 전에 정리해 두면 편하다.</b>
<span class="m">t ≠ 0, −1</span>에서는 분모가 0이 아니므로 극한은 그냥 대입한 값이다.
그 식을 한 번 정리해 두면 어떤 점이든 바로 읽힌다.

## 풀이

<p><span class="step">① 함수를 정한다.</span>
원문항과 같은 과정으로 <span class="m">f(x) = −x<sup>3</sup> − 2x<sup>2</sup></span>이다.
<span class="m">f(x) + x<sup>2</sup> = −x<sup>2</sup>(x + 1)</span>이다.</p>

<p><span class="step">② t = 2 에서 극한을 정리한다.</span>
<span class="m">t = 2</span>에서 분모 <span class="m">−4·3 = −12</span>와 분자의 값을 구한다.</p>
<p class="m">f(2) = −8 − 8 = −16</p>
<p class="m">(x + 2)(x − f(2)) = (x + 2)(x + 16)</p>
<p>분모는 <span class="m">f(x) + x<sup>2</sup> = −x<sup>2</sup>(x + 1)</span>이다.
<span class="m">t = 2</span>에서 분모는 0이 아니므로 극한은 대입값이다.</p>

<p><span class="step">③ 대입한다.</span></p>
<p class="m">lim<sub>x→2</sub> (x + 2)(x + 16) / (−x<sup>2</sup>(x + 1)) = (4)(18) / (−4 · 3)</p>
<p class="m">= 72 / (−12) = −6</p>
<p class="m">답 −6</p>

<p><span class="step">④ 확인한다.</span>
일반식으로 쓰면 <span class="m">t ≠ 0, −1</span>에서 극한은 <span class="m">−2(t + 1)</span>이다.
<span class="m">t = 2</span>를 넣으면 <span class="m">−6</span>으로 같다. ✓</p>

## 함정

<b>분자의 <span class="m">f(t)</span>를 <span class="m">t</span>로 바꾸면 안 된다.</b>
분자는 <span class="m">(x + t)(x − f(t))</span>이다.
<span class="m">f(2) = −16</span>을 먼저 구하지 않고 <span class="m">2</span>를 넣으면 <span class="m">(x+2)(x−2)</span>가 되어 답이 달라진다.<br><br>

<b>분모는 <span class="m">f(x) + x<sup>2</sup></span>이다.</b>
<span class="m">f(x)</span>만 대입하면 <span class="m">−x<sup>3</sup> − 2x<sup>2</sup></span>의 값이 나와 틀린다.

## 노하우

<b>함수를 찾는 문제가 극한값을 묻는 문제로 바뀌면 단계가 하나 늘어난다.</b>
먼저 조건으로 함수를 정하고, 그다음 극한을 대입한다.
<b>극한이 부정형이 아니면 바로 대입하고, 부정형이면 그때 인수분해한다.</b>
