---
id: PRB-C24
unit: 07-경우의수확률
topic: 조건부확률과 합집합
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 1회 24번
exam: 2027-수능완성
origin: 기출
core: "두 조건부확률이 같으면 P(A)=P(B)이고 모든 것을 P(A∩B) 하나로 쓸 수 있다"
tags: [조건부확률,합집합,미지수하나로]
status: seed
added: 2026-09-07
answer: ②
---

## 문제

<p>두 사건 <span class="m">A, B</span>에 대하여</p>
<p class="m">P(A|B) = P(B|A) = 1/3, &nbsp; P(A ∪ B) = 2/3</p>
<p>일 때, <span class="m">P(A ∩ B)</span>의 값은?</p>
<div class="choices"><span>① 1/15</span><span>② 2/15</span><span>③ 1/5</span>
<span>④ 4/15</span><span>⑤ 1/3</span></div>

## 발상

구하는 것이 <span class="m">P(A∩B)</span>이므로
<b>그것을 <span class="m">x</span>로 두고 나머지를 전부 <span class="m">x</span>로 쓴다.</b><br><br>
조건부확률의 정의를 뒤집으면
<span class="m">P(A)</span>와 <span class="m">P(B)</span>가 모두
<span class="m">x</span>의 상수배로 나오고, 그러면 합집합 공식이
<span class="m">x</span>에 대한 일차방정식이 된다.

## 풀이

<p><span class="step">① 구하는 것을 문자로 둔다.</span></p>
<p class="m">P(A ∩ B) = x</p>

<p><span class="step">② 두 조건부확률을 뒤집는다.</span>
조건부확률의 정의는
<span class="m">P(A|B) = P(A∩B)/P(B)</span>이다.
분모를 없애기 위해 양변에 <span class="m">P(B)</span>를 곱하고
<span class="m">P(B)</span>에 대해 정리한다.</p>
<p class="m">x / P(B) = 1/3 → P(B) = 3x</p>
<p>같은 방법으로 <span class="m">P(B|A) = P(A∩B)/P(A) = 1/3</span>에서</p>
<p class="m">P(A) = 3x</p>
<p><b>두 조건부확률이 같으므로 <span class="m">P(A) = P(B)</span></b>가 되었다.</p>

<p><span class="step">③ 합집합 공식에 넣는다.</span></p>
<p class="m">P(A ∪ B) = P(A) + P(B) − P(A ∩ B)</p>
<p class="m">2/3 = 3x + 3x − x = 5x</p>

<p><span class="step">④ x를 구한다.</span>
양변을 <span class="m">5</span>로 나눈다.</p>
<p class="m">x = (2/3) ÷ 5 = 2/15</p>
<p class="m">답 ②</p>

## 함정

<b>합집합에서 교집합을 빼는 것을 잊으면 안 된다.</b>
<span class="m">3x + 3x = 6x</span>로 놓으면
<span class="m">x = 1/9</span>이 되어 보기에 없다.
<span class="m">P(A∪B) = P(A) + P(B) − P(A∩B)</span>에서
<b>겹치는 부분을 두 번 세었으니 한 번 뺀다.</b>

## 노하우

<b>구하는 것을 문자로 두고 나머지를 그것으로 표현한다.</b>
확률 문제에서 미지수가 여러 개로 보여도
조건부확률의 정의를 뒤집으면 대개 <b>하나로 줄어든다.</b><br><br>
<span class="m">P(A|B) = P(B|A)</span>는
<span class="m">P(A∩B)/P(B) = P(A∩B)/P(A)</span>이므로
<b>곧바로 <span class="m">P(A) = P(B)</span></b>를 뜻한다.
이 관찰을 먼저 하면 계산이 절반으로 준다.
