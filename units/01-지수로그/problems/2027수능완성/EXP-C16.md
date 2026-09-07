---
id: EXP-C16
unit: 01-지수로그
topic: 지수부등식
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 1회 16번
exam: 2027-수능완성
origin: 기출
core: "밑을 3으로 통일하면 지수끼리의 일차부등식이 된다"
tags: [지수부등식,밑통일]
status: seed
added: 2026-09-07
answer: 6
---

## 문제

<p>부등식 <span class="m">9<sup>x</sup> &lt; √27 × 3<sup>8−x</sup></span>을
만족시키는 모든 자연수 <span class="m">x</span>의 값의 합을 구하시오.</p>

## 발상

<b>밑이 <span class="m">9</span>, <span class="m">27</span>, <span class="m">3</span>으로 섞여 있다.</b>
셋 다 <span class="m">3</span>의 거듭제곱이므로 밑을 <span class="m">3</span>으로 통일한다.
밑이 같아지면 <b>지수만 비교</b>하면 되고, 밑 <span class="m">3</span>이
<span class="m">1</span>보다 크므로 <b>부등호 방향은 그대로</b>다.

## 풀이

<p><span class="step">① 왼쪽을 밑 3으로 고친다.</span>
<span class="m">9 = 3<sup>2</sup></span>이므로</p>
<p class="m">9<sup>x</sup> = (3<sup>2</sup>)<sup>x</sup> = 3<sup>2x</sup></p>

<p><span class="step">② 오른쪽도 밑 3으로 고친다.</span>
<span class="m">√27</span>은 제곱근이므로 지수 <span class="m">1/2</span>이고,
<span class="m">27 = 3<sup>3</sup></span>이다.</p>
<p class="m">√27 = 27<sup>1/2</sup> = (3<sup>3</sup>)<sup>1/2</sup> = 3<sup>3/2</sup></p>
<p>이제 곱하면서 <b>지수를 더한다.</b></p>
<p class="m">√27 × 3<sup>8−x</sup> = 3<sup>3/2</sup> × 3<sup>8−x</sup> = 3<sup>3/2 + 8 − x</sup> = 3<sup>19/2 − x</sup></p>

<p><span class="step">③ 지수를 비교한다.</span>
밑이 <span class="m">3</span>으로 같고 <span class="m">3 &gt; 1</span>이므로
<b>지수가 큰 쪽이 큰 수</b>다. 부등호 방향이 그대로 유지된다.</p>
<p class="m">3<sup>2x</sup> &lt; 3<sup>19/2 − x</sup> → 2x &lt; 19/2 − x</p>

<p><span class="step">④ 일차부등식을 푼다.</span>
오른쪽의 <span class="m">−x</span>를 왼쪽으로 넘긴다.</p>
<p class="m">2x + x &lt; 19/2 → 3x &lt; 19/2</p>
<p>양변을 <span class="m">3</span>으로 나눈다.</p>
<p class="m">x &lt; 19/6</p>

<p><span class="step">⑤ 자연수만 고른다.</span>
<span class="m">19/6 = 3.166…</span>이므로
이보다 작은 자연수는 <span class="m">1, 2, 3</span>이다.</p>
<p class="m">1 + 2 + 3 = 6</p>
<p class="m">답 6</p>

## 함정

<b>밑이 <span class="m">1</span>보다 작으면 부등호가 뒤집힌다.</b>
이 문제는 밑이 <span class="m">3</span>이라 그대로지만,
<span class="m">(1/2)<sup>x</sup></span> 같은 꼴이 나오면 지수를 비교할 때 방향을 바꿔야 한다.
밑을 통일한 뒤 <b><span class="m">1</span>보다 큰지 작은지 반드시 확인</b>한다.<br><br>
그리고 <b><span class="m">x &lt; 19/6</span>에서 <span class="m">x = 3</span>이 포함된다.</b>
<span class="m">19/6 ≒ 3.17</span>이므로 <span class="m">3</span>은 이보다 작다.
어림으로 &lsquo;<span class="m">3</span>쯤&rsquo;이라 생각하고 빼면 답이 <span class="m">3</span>이 된다.

## 노하우

<b>지수부등식은 밑 통일 → 지수 비교 → 방향 확인, 이 세 단계다.</b>
거듭제곱근은 분수 지수로 바꾼다
(<span class="m">√a = a<sup>1/2</sup></span>, <span class="m">∛a = a<sup>1/3</sup></span>).<br><br>
<b>답이 &lsquo;자연수의 합&rsquo;이면 범위를 구한 뒤 반드시 하나씩 적어 본다.</b>
경계값이 포함되는지 아닌지에서 갈리는 경우가 많아,
소수로 고쳐 놓고 비교하는 것이 안전하다.
