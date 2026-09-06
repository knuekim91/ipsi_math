---
id: PRB-J24
unit: 07-경우의수확률
topic: 확률의 덧셈
level: 3점
difficulty: 하
source: 2027-06모평 24번
exam: 2027-06모평
origin: 기출
core: "A는 A∩B와 A∩B^C로 정확히 둘로 쪼개진다"
tags: [확률,여사건,분할]
status: seed
added: 2026-09-06
answer: ②
---

## 문제

<p>두 사건 <span class="m">A, B</span>에 대하여</p><span class="cond m">P(A ∩ B) = 1/3, &nbsp; P(A ∩ B<sup>C</sup>) = 3/8</span><p>일 때, <span class="m">P(A<sup>C</sup>)</span>의 값은?</p><div class="choices"><span>① 5/24</span><span>② 7/24</span><span>③ 3/8</span><span>④ 11/24</span><span>⑤ 13/24</span></div>

## 발상

<b><span class='m'>A</span>는 <span class='m'>B</span>와 겹치는 부분과 겹치지 않는 부분으로 빈틈없이 둘로 나뉜다.</b> 그 둘을 더하면 <span class='m'>P(A)</span>.

## 풀이

<p><span class="step">① 사건 A가 어떻게 나뉘는지 본다.</span>
벤다이어그램에서 <span class="m">A</span>라는 원 안은
<span class="m">B</span>와 겹치는 부분과 겹치지 않는 부분으로
<b>빈틈없이 정확히 둘로 갈라진다.</b></p>
<p class="m">P(A) = P(A ∩ B) + P(A ∩ B<sup>C</sup>)</p>

<p><span class="step">② 값을 넣어 P(A)를 구한다.</span>
분모를 <span class="m">24</span>로 통일한다.</p>
<p class="m">P(A) = 1/3 + 3/8 = 8/24 + 9/24 = 17/24</p>

<p><span class="step">③ 여사건의 확률을 구한다.</span>
어떤 사건과 그 여사건의 확률의 합은 <span class="m">1</span>이다.</p>
<p class="m">P(A<sup>C</sup>) = 1 − P(A) = 1 − 17/24 = 24/24 − 17/24 = 7/24</p>
<p class="m">답 ②</p>

## 노하우

<b><span class='m'>P(A) = P(A∩B) + P(A∩B<sup>C</sup>)</span>, 이것을 &lsquo;분할&rsquo;이라 한다.</b> 벤다이어그램에서 <span class='m'>A</span> 원 안이 두 조각으로 갈라지는 그림 하나면 충분하다.
