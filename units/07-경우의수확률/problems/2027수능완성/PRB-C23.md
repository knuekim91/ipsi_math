---
id: PRB-C23
unit: 07-경우의수확률
topic: 이항정리의 일반항
level: 2점
difficulty: 하
source: 2027 수능완성 실전 모의고사 1회 23번
exam: 2027-수능완성
origin: 기출
core: "지수만 방정식으로 놓으면 r이 하나로 정해진다"
tags: [이항정리,전개식,계수]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p><span class="m">(x<sup>2</sup> + 2/x)<sup>4</sup></span>의 전개식에서
<span class="m">x<sup>2</sup></span>의 계수는?</p>
<div class="choices"><span>① 12</span><span>② 16</span><span>③ 20</span>
<span>④ 24</span><span>⑤ 28</span></div>

## 발상

전개식을 다 펼치지 않는다. <b>일반항을 세우고 <span class="m">x</span>의 지수만
방정식으로 놓으면</b> 어느 항인지 바로 나온다.

## 풀이

<p><span class="step">① 일반항을 세운다.</span>
<span class="m">(A + B)<sup>4</sup></span>의 일반항은
<span class="m"><sub>4</sub>C<sub>r</sub>A<sup>4−r</sup>B<sup>r</sup></span>이다.
여기서 <span class="m">A = x<sup>2</sup></span>,
<span class="m">B = 2/x = 2x<sup>−1</sup></span>이다.</p>
<p class="m">일반항 = <sub>4</sub>C<sub>r</sub>(x<sup>2</sup>)<sup>4−r</sup>(2x<sup>−1</sup>)<sup>r</sup></p>

<p><span class="step">② x의 지수를 하나로 모은다.</span>
<span class="m">(x<sup>2</sup>)<sup>4−r</sup> = x<sup>8−2r</sup></span>이고
<span class="m">(2x<sup>−1</sup>)<sup>r</sup> = 2<sup>r</sup>x<sup>−r</sup></span>이므로,
곱할 때 지수를 더한다.</p>
<p class="m">일반항 = <sub>4</sub>C<sub>r</sub>2<sup>r</sup>x<sup>(8−2r) + (−r)</sup> = <sub>4</sub>C<sub>r</sub>2<sup>r</sup>x<sup>8−3r</sup></p>

<p><span class="step">③ 지수가 2가 되는 r을 찾는다.</span></p>
<p class="m">8 − 3r = 2 → 3r = 6 → r = 2</p>

<p><span class="step">④ 계수를 계산한다.</span></p>
<p class="m"><sub>4</sub>C<sub>2</sub> × 2<sup>2</sup> = 6 × 4 = 24</p>
<p class="m">답 ④</p>

## 함정

<b><span class="m">2/x</span>의 <span class="m">2</span>를 빠뜨리기 쉽다.</b>
<span class="m">B<sup>r</sup> = (2/x)<sup>r</sup> = 2<sup>r</sup>/x<sup>r</sup></span>이므로
<span class="m">2<sup>r</sup></span>이 계수에 곱해진다.
이것을 잊으면 <span class="m"><sub>4</sub>C<sub>2</sub> = 6</span>이 되어 보기에 없는 값이 나온다.

## 노하우

<b>이항정리는 &lsquo;일반항 → 지수 방정식 → 대입&rsquo; 세 단계다.</b>
분모에 있는 <span class="m">x</span>는 <span class="m">x<sup>−1</sup></span>로 바꿔
지수를 더하기만 하면 된다.
<span class="m">r</span>가 정수로 나오지 않으면 그런 항이 없다는 뜻이다.
