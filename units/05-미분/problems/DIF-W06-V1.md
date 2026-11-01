---
id: DIF-W06-V1
parent: DIF-W06
unit: 05-미분
topic: 근의 중복도로 삼차함수 결정하기 (기본)
level: 4점
difficulty: 하
source: 자체 개발 (DIF-W06 변형 · 극한 없이 근의 구조만)
origin: 유사문항
core: "f(x)+x² 의 근의 중복도가 곧 f 의 꼴이다. 0 은 중근, −1 은 단근이라는 두 정보로 최고차항 계수까지 정해진다"
tags: [삼차함수,인수분해,중근,근과계수,함숫값]
status: variant
added: 2026-11-01
answer: -16
---

## 문제

<p>최고차항의 계수가 <span class="m">−1</span>인 삼차함수 <span class="m">f(x)</span>에 대하여
방정식 <span class="m">f(x) + x<sup>2</sup> = 0</span>의 실근은 <span class="m">0</span>과 <span class="m">−1</span>뿐이다.
<span class="m">0</span>은 중근이고 <span class="m">−1</span>은 단근일 때,
<span class="m">f(2)</span>의 값을 구하시오.</p>

## 발상

<b>방정식 <span class="m">f(x) + x<sup>2</sup> = 0</span>의 좌변을 하나의 함수로 본다.</b>
<span class="m">g(x) = f(x) + x<sup>2</sup></span>라 하면
<span class="m">g</span>의 근이 어디인지와 그 중복도가 주어져 있다.<br><br>

<b>삼차식은 근과 최고차항 계수로 완전히 정해진다.</b>
최고차항 계수와 근 세 개(중근 포함)를 알면 <span class="m">g</span>가 결정된다.

## 풀이

<p><span class="step">① g의 꼴을 세운다.</span>
<span class="m">g(x) = f(x) + x<sup>2</sup></span>의 최고차항 계수는 <span class="m">−1</span>이다.
근이 <span class="m">0</span>(중근)과 <span class="m">−1</span>(단근)이므로</p>
<p class="m">g(x) = −x<sup>2</sup>(x + 1)</p>

<p><span class="step">② f를 구한다.</span></p>
<p class="m">f(x) = g(x) − x<sup>2</sup> = −x<sup>3</sup> − x<sup>2</sup> − x<sup>2</sup> = −x<sup>3</sup> − 2x<sup>2</sup></p>

<p><span class="step">③ f(2)를 구한다.</span></p>
<p class="m">f(2) = −8 − 8 = −16</p>
<p class="m">답 −16</p>

<p><span class="step">④ 확인한다.</span>
<span class="m">f(x) + x<sup>2</sup> = −x<sup>3</sup> − x<sup>2</sup> = −x<sup>2</sup>(x + 1)</span>이므로
근은 <span class="m">0</span>(중근)과 <span class="m">−1</span>뿐이다. ✓</p>

## 함정

<b>중근을 단근으로 읽으면 차수가 맞지 않는다.</b>
<span class="m">0</span>이 중근이므로 <span class="m">x<sup>2</sup></span>이 인수에 들어간다.
<span class="m">x</span>만 곱하면 근의 개수가 맞지 않는다.<br><br>

<b>f + x²를 f 로 착각한다.</b>
주어진 것은 <span class="m">f(x) + x<sup>2</sup></span>의 근이다.
<span class="m">f</span> 자체의 근이 아니므로 마지막에 <span class="m">x<sup>2</sup></span>을 다시 빼야 한다.

## 노하우

<b>&lsquo;어떤 식의 근이 주어지면 그 식을 g 로 두고 인수분해한다.&rsquo;</b>
그 식이 원래 함수에 무엇을 더한 것인지 확인하고, 마지막에 되돌린다.
