---
id: EXP-D21
unit: 01-지수로그
topic: 로그함수와 지수함수 사이의 정사각형
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 21번
exam: 2027-수능완성
origin: 기출
core: "세로 변의 길이가 P의 y좌표이므로 log(x)=n에서 P가 정해지고, 가로 변의 길이 n이 Q를 좌우 두 개로 갈라 k가 두 개 나온다"
tags: [로그함수,지수함수,정사각형,수선의발]
status: seed
added: 2026-09-07
answer: 38
---

## 문제

<p>실수 <span class="m">k</span>와 두 곡선
<span class="m">y = log<sub>2</sub>x</span>,
<span class="m">y = (1/2)<sup>x</sup> + k</span>가 있다.
곡선 <span class="m">y = log<sub>2</sub>x</span> 위에 있는 제1사분면 위의 점
<span class="m">P</span>에 대하여 점 <span class="m">P</span>를 지나고
<span class="m">x</span>축에 평행한 직선이 곡선
<span class="m">y = (1/2)<sup>x</sup> + k</span>와
<span class="m">P</span>가 아닌 점 <span class="m">Q</span>에서 만날 때,
두 점 <span class="m">P</span>, <span class="m">Q</span>에서
<span class="m">x</span>축에 내린 수선의 발을 각각
<span class="m">R</span>, <span class="m">S</span>라 하자.
자연수 <span class="m">n</span>에 대하여 사각형 <span class="m">PQSR</span>이
한 변의 길이가 <span class="m">n</span>인 정사각형이 되도록 하는 모든
<span class="m">k</span>의 값을 <span class="m">α<sub>n</sub></span>,
<span class="m">β<sub>n</sub></span>
<span class="m">(α<sub>n</sub> &gt; β<sub>n</sub>)</span>이라 하자.
<span class="m">f(n) = α<sub>n</sub> − β<sub>n</sub></span>이라 할 때,</p>
<p class="m">2<sup>6</sup> × f(1)/f(2) × f(4)/f(3) = q/p</p>
<p>이다. <span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

<div class="fig">
<svg viewBox="0 0 360 240" role="img" aria-label="증가하는 로그곡선과 감소하는 지수곡선이 그려져 있다. 로그곡선 위의 점 P와 지수곡선 위의 점 Q가 같은 높이에 있고, 두 점에서 x축에 내린 수선의 발 R와 S가 있어 네 점이 정사각형을 이룬다.">
  <path class="rg" d="M120 130 L180 130 L180 190 L120 190 Z"/>
  <path class="ax" d="M40 190 L350 190"/>
  <path class="ax" d="M60 225 L60 30"/>
  <path class="cv" d="M102 221 L114 199 L126 182 L144 161 L168 139 L198 118 L240 95 L288 74 L336 58"/>
  <path class="cv" d="M60 100 L90 118 L120 130 L150 139 L180 145 L240 153 L300 156 L345 158"/>
  <path class="gd" d="M120 130 L180 130 L180 190 L120 190 Z"/>
  <circle class="pt" cx="180" cy="130" r="3.5"/>
  <circle class="pt" cx="120" cy="130" r="3.5"/>
  <circle class="pt" cx="180" cy="190" r="3.5"/>
  <circle class="pt" cx="120" cy="190" r="3.5"/>
  <text x="189" y="126" text-anchor="start">P</text>
  <text x="111" y="126" text-anchor="end">Q</text>
  <text x="189" y="205" text-anchor="start">R</text>
  <text x="111" y="205" text-anchor="end">S</text>
  <text x="330" y="50"  text-anchor="middle">y = log₂x</text>
  <text x="300" y="172" text-anchor="middle">y = (1/2)ˣ + k</text>
  <text x="53"  y="27"  text-anchor="end">y</text>
  <text x="348" y="183" text-anchor="end">x</text>
</svg>
</div>

## 발상

<b>정사각형의 두 변이 서로 다른 것을 재고 있다.</b>
<span class="m">P</span>와 <span class="m">R</span>는
<span class="m">x</span>좌표가 같고 <span class="m">R</span>는
<span class="m">x</span>축 위에 있으므로,
<b>세로 변 <span class="m">PR</span>의 길이는 곧
<span class="m">P</span>의 <span class="m">y</span>좌표</b>이다.
한편 <span class="m">P</span>와 <span class="m">Q</span>는 높이가 같으므로,
<b>가로 변 <span class="m">PQ</span>의 길이는 두 점의
<span class="m">x</span>좌표의 차</b>이다.<br><br>

<b>세로 변이 <span class="m">P</span>를 완전히 정한다.</b>
<span class="m">P</span>의 <span class="m">y</span>좌표가
<span class="m">n</span>이므로
<span class="m">log<sub>2</sub>x = n</span>에서
<span class="m">x = 2<sup>n</sup></span>이 되어
<span class="m">P(2<sup>n</sup>, n)</span>으로 확정된다.<br><br>

<b>가로 변이 <span class="m">k</span>를 두 개로 가른다.</b>
<span class="m">Q</span>의 <span class="m">x</span>좌표는
<span class="m">P</span>보다 <span class="m">n</span>만큼 왼쪽일 수도 있고
오른쪽일 수도 있다.
이 <b>두 가지 위치가 곧 두 값
<span class="m">α<sub>n</sub></span>, <span class="m">β<sub>n</sub></span></b>이다.
<span class="m">f(n)</span>은 그 차이므로,
<span class="m">k</span>를 <span class="m">n</span>과 지수로만 나타내면 바로 계산된다.

## 풀이

<p><span class="step">① P의 좌표를 구한다.</span>
점 <span class="m">P</span>는 곡선
<span class="m">y = log<sub>2</sub>x</span> 위에 있고 제1사분면 위에 있으므로
<span class="m">y</span>좌표가 양수이다.
점 <span class="m">R</span>는 <span class="m">P</span>에서
<span class="m">x</span>축에 내린 수선의 발이므로,
선분 <span class="m">PR</span>의 길이는 <span class="m">P</span>의
<span class="m">y</span>좌표와 같다.
정사각형의 한 변의 길이가 <span class="m">n</span>이므로</p>
<p class="m">(P의 y좌표) = n → log<sub>2</sub>x = n → x = 2<sup>n</sup></p>
<p class="m">P(2<sup>n</sup>, n)</p>

<p><span class="step">② Q의 x좌표를 구한다.</span>
점 <span class="m">Q</span>는 <span class="m">P</span>를 지나고
<span class="m">x</span>축에 평행한 직선 위에 있으므로
<span class="m">y</span>좌표가 <span class="m">n</span>으로 같다.
선분 <span class="m">PQ</span>는 이 정사각형의 가로 변이므로 길이가
<span class="m">n</span>이다.
<span class="m">Q</span>의 <span class="m">x</span>좌표를
<span class="m">s</span>라 하면</p>
<p class="m">|2<sup>n</sup> − s| = n → s = 2<sup>n</sup> − n 또는 s = 2<sup>n</sup> + n</p>
<p><b><span class="m">Q</span>가 <span class="m">P</span>의 왼쪽에 있는 경우와
오른쪽에 있는 경우가 모두 가능하다.</b></p>

<p><span class="step">③ k를 s로 나타낸다.</span>
점 <span class="m">Q(s, n)</span>이 곡선
<span class="m">y = (1/2)<sup>x</sup> + k</span> 위에 있으므로</p>
<p class="m">(1/2)<sup>s</sup> + k = n</p>
<p><span class="m">(1/2)<sup>s</sup> = 2<sup>−s</sup></span>이므로</p>
<p class="m">k = n − 2<sup>−s</sup></p>

<p><span class="step">④ 두 k의 값을 비교한다.</span>
②의 두 경우를 각각 넣는다.</p>
<p class="m">s = 2<sup>n</sup> − n 일 때 : k = n − 2<sup>−(2<sup>n</sup>−n)</sup></p>
<p class="m">s = 2<sup>n</sup> + n 일 때 : k = n − 2<sup>−(2<sup>n</sup>+n)</sup></p>
<p><span class="m">2<sup>n</sup> − n &lt; 2<sup>n</sup> + n</span>이므로
지수 <span class="m">−(2<sup>n</sup> − n)</span>이
<span class="m">−(2<sup>n</sup> + n)</span>보다 크다.
밑 <span class="m">2</span>가 <span class="m">1</span>보다 크므로</p>
<p class="m">2<sup>−(2<sup>n</sup>−n)</sup> &gt; 2<sup>−(2<sup>n</sup>+n)</sup></p>
<p>빼는 값이 클수록 <span class="m">k</span>는 작아지므로,
큰 쪽이 <span class="m">α<sub>n</sub></span>이다.</p>
<p class="m">α<sub>n</sub> = n − 2<sup>−(2<sup>n</sup>+n)</sup>, &nbsp;
β<sub>n</sub> = n − 2<sup>−(2<sup>n</sup>−n)</sup></p>

<p><span class="step">⑤ f(n)을 정리한다.</span>
두 값을 빼면 <span class="m">n</span>이 사라진다.</p>
<p class="m">f(n) = α<sub>n</sub> − β<sub>n</sub>
= 2<sup>−(2<sup>n</sup>−n)</sup> − 2<sup>−(2<sup>n</sup>+n)</sup></p>
<p>두 항에서 공통인 <span class="m">2<sup>−(2<sup>n</sup>+n)</sup></span>으로
묶어 낸다.</p>
<p class="m">f(n) = 2<sup>−(2<sup>n</sup>+n)</sup>(2<sup>2n</sup> − 1)</p>
<p>분수 꼴로 쓰면 다음과 같다.</p>
<p class="m">f(n) = (2<sup>2n</sup> − 1) / 2<sup>2<sup>n</sup>+n</sup></p>

<p><span class="step">⑥ f(1)/f(2)를 구한다.</span>
<span class="m">n = 1</span>이면 지수는
<span class="m">2<sup>1</sup> + 1 = 3</span>,
<span class="m">n = 2</span>이면
<span class="m">2<sup>2</sup> + 2 = 6</span>이다.</p>
<p class="m">f(1) = (2<sup>2</sup> − 1)/2<sup>3</sup> = 3/8, &nbsp;
f(2) = (2<sup>4</sup> − 1)/2<sup>6</sup> = 15/64</p>
<p class="m">f(1)/f(2) = (3/8) × (64/15) = (3 × 8)/15 = 24/15 = 8/5</p>

<p><span class="step">⑦ f(4)/f(3)을 구한다.</span>
<span class="m">n = 3</span>이면 지수는
<span class="m">2<sup>3</sup> + 3 = 11</span>,
<span class="m">n = 4</span>이면
<span class="m">2<sup>4</sup> + 4 = 20</span>이다.</p>
<p class="m">f(3) = (2<sup>6</sup> − 1)/2<sup>11</sup> = 63/2<sup>11</sup>, &nbsp;
f(4) = (2<sup>8</sup> − 1)/2<sup>20</sup> = 255/2<sup>20</sup></p>
<p class="m">f(4)/f(3) = (255/2<sup>20</sup>) × (2<sup>11</sup>/63) = 255/(2<sup>9</sup> × 63)</p>
<p><span class="m">255 = 3 × 85</span>,
<span class="m">63 = 3 × 21</span>이므로 <span class="m">3</span>으로 약분한다.</p>
<p class="m">f(4)/f(3) = 85/(2<sup>9</sup> × 21)</p>

<p><span class="step">⑧ 전체를 곱한다.</span></p>
<p class="m">2<sup>6</sup> × (8/5) × 85/(2<sup>9</sup> × 21)</p>
<p><span class="m">85/5 = 17</span>로 먼저 약분하고,
<span class="m">2<sup>6</sup> × 8 = 2<sup>9</sup></span>이므로
<span class="m">2</span>의 거듭제곱이 통째로 지워진다.</p>
<p class="m">= 2<sup>9</sup> × 17/(2<sup>9</sup> × 21) = 17/21</p>

<p><span class="step">⑨ 답을 만든다.</span>
<span class="m">q/p = 17/21</span>이고
<span class="m">17</span>과 <span class="m">21</span>은 서로소이므로
<span class="m">q = 17</span>, <span class="m">p = 21</span>이다.</p>
<p class="m">p + q = 21 + 17 = 38</p>
<p class="m">답 38</p>

## 함정

<b><span class="m">Q</span>가 <span class="m">P</span>의 한쪽에만 있다고 보면
<span class="m">k</span>가 하나밖에 안 나온다.</b>
정사각형은 <span class="m">P</span>의 왼쪽에도 오른쪽에도 만들어질 수 있다.
<span class="m">k</span>가 두 개라고 문제가 알려 주고 있으므로,
<b>절댓값을 벗길 때 두 경우를 모두 써야 한다.</b><br><br>

<b><span class="m">α<sub>n</sub></span>과 <span class="m">β<sub>n</sub></span>을
뒤집으면 <span class="m">f(n)</span>이 음수가 된다.</b>
<span class="m">k = n − 2<sup>−s</sup></span>에서
<span class="m">2<sup>−s</sup></span>가 <b>작을수록</b>
<span class="m">k</span>가 크다. 그리고
<span class="m">s</span>가 클수록 <span class="m">2<sup>−s</sup></span>가 작다.
따라서 <b><span class="m">s = 2<sup>n</sup> + n</span>인 쪽이
<span class="m">α<sub>n</sub></span></b>이다.
다만 이 문제는 차를 구하므로 순서를 바꿔도 절댓값은 같지만,
부호가 뒤집히면 마지막 약분에서 음수가 나온다.<br><br>

<b>지수를 <span class="m">2n</span>과 <span class="m">2<sup>n</sup></span>으로
혼동하기 쉽다.</b>
<span class="m">P</span>의 <span class="m">x</span>좌표는
<span class="m">2<sup>n</sup></span>이고,
묶어 낸 괄호 안은 <span class="m">2<sup>2n</sup> − 1</span>이다.
<span class="m">n = 3</span>이면 각각
<span class="m">8</span>과 <span class="m">64</span>로 전혀 다르다.

## 노하우

<b>수선의 발이 나오면 그 변의 길이는 좌표 그 자체다.</b>
<span class="m">x</span>축에 내린 수선의 발까지의 거리는
<span class="m">y</span>좌표이고,
<span class="m">y</span>축이면 <span class="m">x</span>좌표이다.
이것이 정사각형의 <b>한 변을 곧바로 방정식으로 바꿔 준다.</b><br><br>

<b>지수가 붙은 값끼리 뺄 때는 작은 쪽으로 묶는다.</b>
<span class="m">2<sup>A</sup> − 2<sup>B</sup> (A &gt; B)</span>는
<span class="m">2<sup>B</sup>(2<sup>A−B</sup> − 1)</span>로 묶으면
<b>괄호 안이 정수</b>가 되어 약분이 쉬워진다.
이 문제에서도 그렇게 묶은 덕분에
<span class="m">2<sup>2n</sup> − 1</span>이라는 깔끔한 꼴이 나왔다.<br><br>

<b>비를 계산할 때는 지수부터 정리한다.</b>
<span class="m">f(4)/f(3)</span>처럼 큰 수가 나오는 나눗셈은
<span class="m">255</span>나 <span class="m">1048576</span>을 직접 쓰지 말고
<span class="m">2</span>의 거듭제곱 꼴로 두어야 한다.
마지막에 <span class="m">2<sup>9</sup></span>이 통째로 약분되는 것이 보인다.
