---
id: PRB-D24
unit: 07-경우의수확률
topic: 배반사건과 여사건의 확률
level: 3점
difficulty: 하
source: 2027 수능완성 실전 모의고사 2회 24번
exam: 2027-수능완성
origin: 기출
core: "배반이면 합사건의 확률이 두 확률의 합이고, 여사건의 확률은 1에서 뺀 것이다"
tags: [배반사건,여사건,확률의덧셈정리]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>두 사건 <span class="m">A</span>와 <span class="m">B</span>는 서로
배반사건이고</p>
<p class="m">4P(A) = P(B<sup>c</sup>), &nbsp; P(A ∪ B) = 1/2</p>
<p>일 때, <span class="m">P(A)</span>의 값은?</p>

<div class="choices"><span>① 1/24</span><span>② 1/12</span><span>③ 1/8</span>
<span>④ 1/6</span><span>⑤ 5/24</span></div>

## 발상

<b>모르는 것이 두 개이므로 식도 두 개를 만든다.</b>
<span class="m">P(A)</span>와 <span class="m">P(B)</span>를
각각 미지수로 두고, 주어진 두 조건을 그 미지수의 식으로 바꾸면
연립일차방정식이 된다.<br><br>

<b>두 조건을 각각 번역하는 데 필요한 공식은 하나씩이다.</b>
<span class="m">P(B<sup>c</sup>)</span>는 여사건의 확률이므로
<span class="m">1 − P(B)</span>이다.
<span class="m">P(A ∪ B)</span>는 확률의 덧셈정리에서
<span class="m">P(A) + P(B) − P(A ∩ B)</span>인데,
<b>두 사건이 배반이므로 <span class="m">P(A ∩ B) = 0</span></b>이 되어
그냥 <span class="m">P(A) + P(B)</span>가 된다.

## 풀이

<p><span class="step">① 미지수를 잡는다.</span></p>
<p class="m">P(A) = x, &nbsp; P(B) = y</p>

<p><span class="step">② 배반 조건으로 첫 번째 식을 만든다.</span>
두 사건 <span class="m">A</span>와 <span class="m">B</span>가
서로 배반사건이므로 동시에 일어나지 않는다.</p>
<p class="m">P(A ∩ B) = 0</p>
<p>확률의 덧셈정리에 이를 대입한다.</p>
<p class="m">P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = x + y</p>
<p>주어진 조건에서 이 값이 <span class="m">1/2</span>이다.</p>
<p class="m">x + y = 1/2 &nbsp; … ㉠</p>

<p><span class="step">③ 여사건 조건으로 두 번째 식을 만든다.</span>
여사건의 확률은 전체에서 뺀 것이다.</p>
<p class="m">P(B<sup>c</sup>) = 1 − P(B) = 1 − y</p>
<p>주어진 조건 <span class="m">4P(A) = P(B<sup>c</sup>)</span>에 대입한다.</p>
<p class="m">4x = 1 − y &nbsp; … ㉡</p>

<p><span class="step">④ 연립방정식을 푼다.</span>
㉡에서 <span class="m">y = 1 − 4x</span>를 얻어 ㉠에 대입한다.</p>
<p class="m">x + (1 − 4x) = 1/2</p>
<p class="m">−3x + 1 = 1/2</p>
<p><span class="m">1</span>을 우변으로 옮긴다.</p>
<p class="m">−3x = 1/2 − 1 = −1/2</p>
<p class="m">x = 1/6</p>

<p><span class="step">⑤ 값이 확률로서 타당한지 확인한다.</span>
<span class="m">y = 1 − 4 × (1/6) = 1 − 2/3 = 1/3</span>이다.
두 값 모두 <span class="m">0</span>과 <span class="m">1</span> 사이에 있고,
<span class="m">x + y = 1/6 + 1/3 = 1/2</span>로 ㉠도 만족시킨다.</p>
<p class="m">P(A) = 1/6</p>
<p class="m">답 ④</p>

## 함정

<b><span class="m">P(B<sup>c</sup>)</span>를
<span class="m">P(B)</span>로 잘못 읽으면 안 된다.</b>
어깨에 붙은 <span class="m">c</span>는 여사건을 뜻한다.
<span class="m">4x = y</span>로 놓으면
<span class="m">x = 1/10</span>이 되어 선택지에도 없는 값이 나온다.<br><br>

<b>배반사건과 독립사건을 헷갈리면 안 된다.</b>
<b>배반</b>은 <span class="m">P(A ∩ B) = 0</span>이고,
<b>독립</b>은 <span class="m">P(A ∩ B) = P(A)P(B)</span>이다.
이 문제는 배반이라고 했으므로
<span class="m">P(A ∩ B)</span>가 <span class="m">0</span>이다.
독립으로 착각하면 이차방정식이 되어 길을 잃는다.<br><br>

<b>합사건의 확률을 그냥 더하는 것은 배반일 때만 옳다.</b>
일반적으로는 겹치는 부분
<span class="m">P(A ∩ B)</span>를 한 번 빼 주어야 한다.
배반이라는 조건이 있어야 그 항이 사라진다.

## 노하우

<b>확률 문제는 모르는 것에 문자를 붙이는 것부터 시작한다.</b>
<span class="m">P(A) = x</span>, <span class="m">P(B) = y</span>처럼
이름을 붙이고 나면, 주어진 조건이 <b>기계적으로 방정식이 된다.</b>
머릿속으로 풀려 하지 말고 식을 두 줄 적는 편이 빠르다.<br><br>

<b>여사건은 <span class="m">1</span>에서 빼고, 배반은 겹침을 지운다.</b>
이 두 가지가 확률의 기본 변환이다.
문제에 <span class="m">c</span>가 보이면 <span class="m">1 −</span>를,
&lsquo;배반&rsquo;이 보이면 <span class="m">P(A ∩ B) = 0</span>을
<b>읽는 즉시 옆에 적어 둔다.</b><br><br>

<b>답이 나오면 확률의 범위를 확인한다.</b>
확률은 <span class="m">0</span> 이상 <span class="m">1</span> 이하여야 한다.
또 배반이므로 <span class="m">P(A) + P(B) ≤ 1</span>이어야 한다.
이 검산을 습관화하면 계산 실수를 스스로 잡을 수 있다.
