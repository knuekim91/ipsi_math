---
id: TRI-C14
unit: 02-삼각함수
topic: 이등변삼각형과 코사인법칙
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 14번
exam: 2027-수능완성
origin: 기출
core: "∠CAD는 ∠A이고 ∠CBD는 ∠B다 — D를 새 각으로 착각하지 않는 것이 전부다"
tags: [코사인법칙,이등변삼각형,내분점]
status: seed
added: 2026-09-07
answer: ②
---

## 문제

<p><span class="m">AB = AC</span>인 이등변삼각형 <span class="m">ABC</span>에서
선분 <span class="m">AB</span>를 <span class="m">3 : 1</span>로 내분하는 점을
<span class="m">D</span>라 하자.</p>
<p class="m">BC = 2, &nbsp; cos(∠CAD) : cos(∠CBD) = 7 : 3</p>
<p>일 때, <span class="m">BD<sup>2</sup> + CD<sup>2</sup></span>의 값은?</p>

<div class="fig"><img src="img/TRI-C14.png" width="743" height="478"
  alt="AB=AC인 이등변삼각형 ABC. A는 왼쪽 아래, B는 오른쪽 아래, C는 위쪽에 있고 선분 AB 위의 점 D가 C와 이어져 있다."></div>

<div class="choices"><span>① 31/8</span><span>② 33/8</span><span>③ 35/8</span>
<span>④ 37/8</span><span>⑤ 39/8</span></div>

## 발상

<b>점 <span class="m">D</span>는 선분 <span class="m">AB</span> 위에 있다.</b>
그러므로 반직선 <span class="m">AD</span>는 반직선 <span class="m">AB</span>와 같은 반직선이고,
<span class="m">∠CAD</span>는 <b>삼각형의 각 <span class="m">A</span> 그 자체</b>다.
마찬가지로 <span class="m">∠CBD</span>는 <b>각 <span class="m">B</span> 그 자체</b>다.<br><br>
<span class="m">D</span>는 각의 크기를 바꾸지 않는다. <span class="m">D</span>가 하는 일은
마지막에 길이를 나누는 것뿐이다.
이것만 알면 주어진 비는 <b><span class="m">cos A : cos B = 7 : 3</span></b>이라는
평범한 조건이 된다.

## 풀이

<p><span class="step">① 변의 길이를 문자로 둔다.</span>
<span class="m">AB = AC</span>이므로 이 길이를 <span class="m">c</span>라 하자.
마주 보는 변 <span class="m">BC = 2</span>는 주어져 있다.</p>
<p class="m">AB = AC = c, &nbsp; BC = 2</p>

<p><span class="step">② cos A를 코사인법칙으로 구한다.</span>
각 <span class="m">A</span>가 마주 보는 변은 <span class="m">BC</span>다.</p>
<p class="m">BC<sup>2</sup> = AB<sup>2</sup> + AC<sup>2</sup> − 2 × AB × AC × cos A</p>
<p class="m">4 = c<sup>2</sup> + c<sup>2</sup> − 2c<sup>2</sup>cos A = 2c<sup>2</sup>(1 − cos A)</p>
<p><span class="m">cos A</span>에 대해 정리한다.</p>
<p class="m">1 − cos A = 2/c<sup>2</sup> → cos A = 1 − 2/c<sup>2</sup></p>

<p><span class="step">③ cos B도 구한다.</span>
각 <span class="m">B</span>가 마주 보는 변은 <span class="m">AC = c</span>다.</p>
<p class="m">AC<sup>2</sup> = AB<sup>2</sup> + BC<sup>2</sup> − 2 × AB × BC × cos B</p>
<p class="m">c<sup>2</sup> = c<sup>2</sup> + 4 − 4c cos B</p>
<p><span class="m">c<sup>2</sup></span>이 양변에서 지워진다.</p>
<p class="m">0 = 4 − 4c cos B → cos B = 1/c</p>

<p><span class="step">④ 주어진 비로 c를 구한다.</span>
<span class="m">cos A : cos B = 7 : 3</span>이므로
<b>안쪽끼리, 바깥쪽끼리 곱한다.</b></p>
<p class="m">3 cos A = 7 cos B</p>
<p class="m">3(1 − 2/c<sup>2</sup>) = 7 × (1/c)</p>
<p>양변에 <span class="m">c<sup>2</sup></span>을 곱해 분모를 없앤다.</p>
<p class="m">3c<sup>2</sup> − 6 = 7c → 3c<sup>2</sup> − 7c − 6 = 0</p>
<p class="m">(3c + 2)(c − 3) = 0 → c = −2/3 또는 c = 3</p>
<p>길이는 양수이므로 <span class="m">c = 3</span>이다.</p>
<p class="m">AB = AC = 3, &nbsp; BC = 2, &nbsp; cos B = 1/3</p>

<p><span class="step">⑤ BD를 구한다.</span>
<span class="m">D</span>가 <span class="m">AB</span>를 <span class="m">3 : 1</span>로 내분하므로
<span class="m">AD : DB = 3 : 1</span>이고, <span class="m">DB</span>는 전체의
<span class="m">1/4</span>이다.</p>
<p class="m">BD = (1/4) × 3 = 3/4</p>

<p><span class="step">⑥ CD를 구한다.</span>
삼각형 <span class="m">BDC</span>에서 코사인법칙을 쓴다.
각 <span class="m">B</span>를 낀 두 변이 <span class="m">BD</span>와 <span class="m">BC</span>이고,
마주 보는 변이 <span class="m">CD</span>다.
<b><span class="m">cos B</span>는 ③에서 이미 구해 둔 값을 그대로 쓴다.</b></p>
<p class="m">CD<sup>2</sup> = BD<sup>2</sup> + BC<sup>2</sup> − 2 × BD × BC × cos B</p>
<p class="m">= (3/4)<sup>2</sup> + 2<sup>2</sup> − 2 × (3/4) × 2 × (1/3)</p>
<p class="m">= 9/16 + 4 − 1 = 9/16 + 3 = 57/16</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">BD<sup>2</sup> + CD<sup>2</sup> = 9/16 + 57/16 = 66/16 = 33/8</p>
<p class="m">답 ②</p>

## 함정

<b><span class="m">∠CAD</span>를 <span class="m">∠A</span>와 다른 각으로 보면 시작부터 막힌다.</b>
<span class="m">D</span>가 선분 <span class="m">AB</span> 위의 점이므로
<span class="m">∠CAD = ∠CAB = ∠A</span>다. <span class="m">∠CBD</span>도 마찬가지로
<span class="m">∠B</span>다. 그림에 점이 하나 더 있다고 해서 각이 새로 생기는 것이 아니다.<br><br>
그리고 <b><span class="m">3 : 1</span>로 내분하면 <span class="m">DB</span>가
전체의 <span class="m">1/4</span></b>이다. <span class="m">1/3</span>로 잘못 잡으면
<span class="m">BD = 1</span>이 되어 답이 달라진다.

## 노하우

<b>선분 위의 점은 각을 바꾸지 않는다.</b>
<span class="m">∠CAD</span>처럼 글자가 셋인 각을 만나면
<b>가운데 글자가 꼭짓점</b>이고, 나머지 두 점이 어느 반직선 위에 있는지만 확인하면 된다.
같은 반직선 위라면 원래 각과 같은 각이다.<br><br>
그리고 <b>이등변삼각형에서 <span class="m">cos</span>을 두 번 구할 때는
한 번 구한 값을 끝까지 재활용</b>한다.
이 문제에서 <span class="m">cos B = 1/c</span>는 ③에서 구해
⑥의 코사인법칙에서 그대로 쓴다. 다시 구하면 시간을 잃는다.
