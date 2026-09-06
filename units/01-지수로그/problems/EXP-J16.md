---
id: EXP-J16
unit: 01-지수로그
topic: 지수방정식
level: 3점
difficulty: 하
source: 2027-06모평 16번
exam: 2027-06모평
origin: 기출
core: "양변의 밑을 같게 만들면 지수끼리의 방정식이 된다"
tags: [지수방정식,밑통일]
status: seed
added: 2026-09-06
answer: 2
---

## 문제

<p class="m">방정식 3<sup>x−6</sup> = (1/9)<sup>x</sup>을 만족시키는 실수 x의 값을 구하시오.</p>

## 발상

<span class='m'>1/9 = 3<sup>−2</sup></span>. <b>밑을 3으로 통일하면 지수만 비교</b>하면 된다.

## 풀이

<p><span class="step">① 양변의 밑이 다르다는 것을 본다.</span>
왼쪽의 밑은 <span class="m">3</span>, 오른쪽의 밑은 <span class="m">1/9</span>다.
<b>밑이 같아야 지수를 비교할 수 있으므로</b> 오른쪽을 밑 <span class="m">3</span>으로 고친다.</p>
<p class="m">1/9 = 1/3<sup>2</sup> = 3<sup>−2</sup></p>

<p><span class="step">② 오른쪽을 정리한다.</span>
지수법칙 <span class="m">(a<sup>m</sup>)<sup>n</sup> = a<sup>mn</sup></span>을 쓴다.</p>
<p class="m">(1/9)<sup>x</sup> = (3<sup>−2</sup>)<sup>x</sup> = 3<sup>−2x</sup></p>

<p><span class="step">③ 밑이 같으므로 지수를 비교한다.</span>
<span class="m">a &gt; 0, a ≠ 1</span>일 때
<span class="m">a<sup>m</sup> = a<sup>n</sup></span>이면 <span class="m">m = n</span>이다.</p>
<p class="m">3<sup>x−6</sup> = 3<sup>−2x</sup> → x − 6 = −2x</p>

<p><span class="step">④ 일차방정식을 푼다.</span>
오른쪽의 <span class="m">−2x</span>를 왼쪽으로 넘긴다.</p>
<p class="m">x + 2x − 6 = 0 → 3x = 6 → x = 2</p>
<p class="m">답 2</p>

## 노하우

<b>지수방정식은 밑 통일이 전부다.</b> 밑이 같아지면 <span class='m'>a<sup>m</sup>=a<sup>n</sup> ⟺ m=n</span> (단 <span class='m'>a&gt;0, a≠1</span>).
