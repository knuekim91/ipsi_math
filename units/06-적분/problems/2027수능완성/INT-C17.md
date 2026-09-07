---
id: INT-C17
unit: 06-적분
topic: 적분방정식과 아래끝
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 1회 17번
exam: 2027-수능완성
origin: 기출
core: "적분의 아래끝을 대입하면 좌변이 0이 되어 a가 결정된다"
tags: [적분방정식,미적분의기본정리]
status: seed
added: 2026-09-07
answer: 5
---

## 문제

<p>양수 <span class="m">a</span>와 다항함수 <span class="m">f(x)</span>가
모든 실수 <span class="m">x</span>에 대하여</p>
<p class="m">∫<sub>a</sub><sup>x</sup>f(t)dt = x<sup>3</sup> + 3x<sup>2</sup> − 4x</p>
<p>를 만족시킬 때, <span class="m">f(a)</span>의 값을 구하시오.</p>

## 발상

적분 기호가 든 등식에서 할 수 있는 일은 두 가지뿐이다.<br><br>
<b>㉠ 아래끝을 대입한다</b> — <span class="m">x = a</span>를 넣으면
<span class="m">∫<sub>a</sub><sup>a</sup> = 0</span>이라 왼쪽이 통째로 사라진다.
이것이 <span class="m">a</span>를 잡는 열쇠다.<br>
<b>㉡ 양변을 미분한다</b> — 적분 기호가 사라지고 <span class="m">f(x)</span>가 나온다.<br><br>
이 문제는 <b>둘 다</b> 쓰고, 순서는 상관없다.

## 풀이

<p><span class="step">① 아래끝을 대입해 a를 구한다.</span>
<span class="m">x = a</span>를 넣으면 적분 구간의 위끝과 아래끝이 같아지므로
왼쪽은 <span class="m">0</span>이다.</p>
<p class="m">0 = a<sup>3</sup> + 3a<sup>2</sup> − 4a</p>
<p>오른쪽을 <span class="m">a</span>로 묶는다.</p>
<p class="m">a(a<sup>2</sup> + 3a − 4) = 0</p>
<p>괄호 안을 인수분해한다. 곱이 <span class="m">−4</span>, 합이 <span class="m">3</span>인 두 수는
<span class="m">4</span>와 <span class="m">−1</span>이다.</p>
<p class="m">a(a + 4)(a − 1) = 0 → a = 0, −4, 1</p>
<p>문제에서 <span class="m">a</span>는 <b>양수</b>라 했으므로</p>
<p class="m">a = 1</p>

<p><span class="step">② 양변을 미분해 f를 구한다.</span>
왼쪽은 미적분의 기본정리에 따라
<span class="m">∫<sub>a</sub><sup>x</sup>f(t)dt</span>를 <span class="m">x</span>로 미분하면
<span class="m">f(x)</span>가 된다. (아래끝 <span class="m">a</span>는 상수라 미분에 영향이 없다.)</p>
<p class="m">f(x) = 3x<sup>2</sup> + 6x − 4</p>

<p><span class="step">③ 구하는 값을 대입한다.</span></p>
<p class="m">f(a) = f(1) = 3 + 6 − 4 = 5</p>
<p class="m">답 5</p>

## 함정

<b><span class="m">a = 0</span>과 <span class="m">a = −4</span>를 버려야 한다.</b>
세 근이 모두 나오지만 문제가 <span class="m">a</span>를 <b>양수</b>라고 못 박아 두었다.
이 조건이 없으면 답이 하나로 정해지지 않는다.
<b>문제에 &lsquo;양수&rsquo;, &lsquo;자연수&rsquo; 같은 말이 붙어 있으면
그것은 근을 거르라는 지시다.</b>

## 노하우

<b>적분방정식은 &lsquo;아래끝 대입&rsquo;과 &lsquo;양변 미분&rsquo; 두 동작이 전부다.</b>
아래끝을 대입하면 <b>적분이 통째로 사라져 상수를 잡을 수 있고</b>,
양변을 미분하면 <b>적분 기호가 벗겨져 함수를 얻는다.</b><br><br>
어느 쪽을 먼저 할지는 <b>무엇을 묻는지</b>가 정한다.
상수가 미지수면 대입부터, 함수를 물으면 미분부터 한다.
이 문제는 <span class="m">f(a)</span>를 물었으니 둘 다 필요하다.
