---
id: INT-D17
unit: 06-적분
topic: 도함수와 한 점의 함숫값으로 함수 결정
level: 3점
difficulty: 하
source: 2027 수능완성 실전 모의고사 2회 17번
exam: 2027-수능완성
origin: 기출
core: "도함수를 적분해 적분상수 C를 남기고, 주어진 한 점의 함숫값으로 C를 정한다"
tags: [부정적분,적분상수,다항함수]
status: seed
added: 2026-09-07
answer: 48
---

## 문제

<p>다항함수 <span class="m">f(x)</span>에 대하여
<span class="m">f′(x) = 8x<sup>3</sup> + 2x + 5</span>이고
<span class="m">f(1) = 10</span>일 때,
<span class="m">f(2)</span>의 값을 구하시오.</p>

## 발상

<b>도함수를 알면 원래 함수는 적분으로 되찾는다.</b>
다만 적분하면 <b>적분상수</b>가 하나 남는다.
미분하면 상수는 사라지므로, 도함수만으로는 원래 함수가 하나로 정해지지 않기 때문이다.<br><br>

<b>그 하나 남은 상수를 정해 주는 것이 <span class="m">f(1) = 10</span>이다.</b>
조건이 딱 하나 주어진 이유가 바로 이것이다.
적분해서 <span class="m">C</span>를 남기고,
<span class="m">x = 1</span>을 대입해 <span class="m">C</span>를 구한 뒤,
<span class="m">x = 2</span>를 넣으면 끝난다.

## 풀이

<p><span class="step">① 도함수를 적분한다.</span>
<span class="m">f(x)</span>는 <span class="m">f′(x)</span>의 부정적분이다.
각 항을 <span class="m">∫x<sup>n</sup>dx = x<sup>n+1</sup>/(n + 1) + C</span>로 적분한다.</p>
<p class="m">f(x) = ∫(8x<sup>3</sup> + 2x + 5)dx</p>
<p class="m">= 8 × x<sup>4</sup>/4 + 2 × x<sup>2</sup>/2 + 5x + C</p>
<p class="m">f(x) = 2x<sup>4</sup> + x<sup>2</sup> + 5x + C</p>

<p><span class="step">② 적분상수 C를 구한다.</span>
<span class="m">f(1) = 10</span>이므로 위 식에
<span class="m">x = 1</span>을 대입한다.</p>
<p class="m">f(1) = 2 × 1 + 1 + 5 + C = 8 + C</p>
<p class="m">8 + C = 10 → C = 2</p>
<p>따라서 함수 <span class="m">f(x)</span>가 완전히 정해진다.</p>
<p class="m">f(x) = 2x<sup>4</sup> + x<sup>2</sup> + 5x + 2</p>

<p><span class="step">③ f(2)를 구한다.</span>
<span class="m">x = 2</span>를 대입한다.</p>
<p class="m">f(2) = 2 × 2<sup>4</sup> + 2<sup>2</sup> + 5 × 2 + 2</p>
<p class="m">= 2 × 16 + 4 + 10 + 2 = 32 + 16 = 48</p>
<p class="m">답 48</p>

## 함정

<b>적분상수를 빠뜨리면 답이 <span class="m">46</span>이 된다.</b>
<span class="m">f′</span>만 보고 바로
<span class="m">f(2) = 32 + 4 + 10 = 46</span>이라고 쓰기 쉽다.
<span class="m">f(1) = 10</span>이라는 조건이 주어진 이유는
오직 <span class="m">C</span>를 정하기 위해서다.
<b>조건이 주어졌다면 반드시 쓰인다.</b><br><br>

<b>계수를 곱하는 순서에서 실수가 나온다.</b>
<span class="m">∫8x<sup>3</sup>dx</span>는
<span class="m">8x<sup>4</sup></span>이 아니라
<span class="m">8 × x<sup>4</sup>/4 = 2x<sup>4</sup></span>이다.
<b>차수를 하나 올리고 그 새 차수로 나눈다</b>는 순서를 지킨다.

## 노하우

<b>도함수와 한 점의 함숫값이 함께 주어지면 곧바로 적분한다.</b>
이 짝은 &lsquo;함수를 완전히 결정하라&rsquo;는 신호다.
미지수는 적분상수 하나뿐이고, 조건도 하나뿐이라 정확히 맞아떨어진다.<br><br>

<b>다른 방법으로도 확인할 수 있다.</b>
정적분의 기본정리를 쓰면 적분상수를 아예 만들지 않고 풀 수 있다.</p>
<p class="m">f(2) − f(1) = ∫<sub>1</sub><sup>2</sup>f′(x)dx</p>
<p class="m">= [2x<sup>4</sup> + x<sup>2</sup> + 5x]<sub>1</sub><sup>2</sup>
= (32 + 4 + 10) − (2 + 1 + 5) = 46 − 8 = 38</p>
<p class="m">f(2) = 10 + 38 = 48</p>
<p>두 방법의 답이 같은지 확인하면 계산 실수를 잡을 수 있다.
<b>시험장에서는 이 방법이 적분상수를 잊을 위험이 없어 더 안전하다.</b>
