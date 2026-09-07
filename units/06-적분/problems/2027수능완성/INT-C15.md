---
id: INT-C15
unit: 06-적분
topic: 주기함수의 넓이
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 15번
exam: 2027-수능완성
origin: 기출
core: "주기가 6이므로 15~19를 기본 구간으로 옮겨 놓고 계산한다"
tags: [주기함수,연속,넓이,정적분]
status: seed
added: 2026-09-07
answer: ③
---

## 문제

<p>실수 전체의 집합에서 연속인 함수 <span class="m">f(x)</span>가
다음 조건을 만족시킨다.</p>
<span class="cond">(가) <span class="m">f(x) = 4x + 8 &nbsp; (−2 ≤ x &lt; 0)</span>,
<span class="m">f(x) = x<sup>2</sup> + ax + b &nbsp; (0 ≤ x &lt; 4)</span><br>
(나) 모든 실수 <span class="m">x</span>에 대하여
<span class="m">f(x) = f(x+6)</span>이다.</span>
<p><span class="m">15 ≤ x ≤ 19</span>에서 함수 <span class="m">y = f(x)</span>의 그래프와
직선 <span class="m">x = 15</span> 및 <span class="m">x</span>축으로 둘러싸인 부분의 넓이를
<span class="m">A</span>, 함수 <span class="m">y = f(x)</span>의 그래프와 직선
<span class="m">x = 19</span> 및 <span class="m">x</span>축으로 둘러싸인 부분의 넓이를
<span class="m">B</span>라 할 때, <span class="m">B − A</span>의 값은?
(단, <span class="m">a, b</span>는 상수이다.)</p>
<div class="choices"><span>① 34/3</span><span>② 12</span><span>③ 38/3</span>
<span>④ 40/3</span><span>⑤ 14</span></div>

## 발상

(가)가 정의한 구간은 <span class="m">−2 ≤ x &lt; 4</span>로 <b>길이가 정확히 <span class="m">6</span></b>이다.
그리고 (나)가 주기 <span class="m">6</span>이라고 했으니,
<b>이 한 토막만 알면 함수 전체를 안다.</b><br><br>
그러므로 <span class="m">15 ≤ x ≤ 19</span>를 그대로 계산하지 말고
<b><span class="m">6</span>의 배수만큼 빼서 기본 구간으로 옮긴 뒤</b> 계산한다.
넓이는 옮겨도 변하지 않는다.

## 풀이

<p><span class="step">① 연속 조건으로 a, b를 구한다.</span>
두 조각이 만나는 곳은 <span class="m">x = 0</span>이고,
주기 때문에 <span class="m">x = 4</span>도 이어져야 한다.</p>
<p><b><span class="m">x = 0</span>에서</b> 왼쪽 식의 값과 오른쪽 식의 값이 같아야 한다.</p>
<p class="m">4 × 0 + 8 = 0<sup>2</sup> + a × 0 + b → b = 8</p>
<p><b><span class="m">x = 4</span>에서</b> — 주기가 <span class="m">6</span>이므로
<span class="m">f(4) = f(4 − 6) = f(−2)</span>이다.</p>
<p class="m">f(−2) = 4 × (−2) + 8 = 0</p>
<p>한편 아래쪽 식으로 <span class="m">x → 4</span>일 때의 값은</p>
<p class="m">4<sup>2</sup> + 4a + b = 16 + 4a + 8 = 24 + 4a</p>
<p>두 값이 같아야 하므로</p>
<p class="m">24 + 4a = 0 → a = −6</p>
<p>따라서 기본 구간에서의 <span class="m">f</span>는 다음과 같다.</p>
<p class="m">f(x) = 4x + 8 &nbsp; (−2 ≤ x &lt; 0)</p>
<p class="m">f(x) = x<sup>2</sup> − 6x + 8 = (x − 2)(x − 4) &nbsp; (0 ≤ x &lt; 4)</p>

<p><span class="step">② 15 ≤ x ≤ 19를 기본 구간으로 옮긴다.</span>
주기가 <span class="m">6</span>이므로 <span class="m">6</span>의 배수를 빼서 옮긴다.
구간을 두 토막으로 나눠야 한다.</p>
<p class="m">15 ≤ x &lt; 16 : t = x − 12 ∈ [3, 4) → f = (t−2)(t−4)</p>
<p class="m">16 ≤ x ≤ 19 : t = x − 18 ∈ [−2, 1] → f = 4t+8 또는 (t−2)(t−4)</p>

<p><span class="step">③ 부호를 확인한다.</span>
<b>넓이를 구할 때는 부호가 바뀌는 곳을 먼저 찾아야 한다.</b></p>
<p class="m">t ∈ [3, 4) : (t−2) &gt; 0, (t−4) &lt; 0 → f &lt; 0</p>
<p class="m">t = −2 (곧 x = 16) : f = 4(−2)+8 = 0</p>
<p class="m">t ∈ (−2, 0) : f = 4t+8 &gt; 0</p>
<p class="m">t ∈ [0, 1] : (t−2)(t−4) &gt; 0 (음수 × 음수)</p>
<p>즉 <b><span class="m">x = 16</span>에서 <span class="m">f</span>가 <span class="m">0</span>이 되면서
음수에서 양수로 바뀐다.</b> 이 점이 두 넓이를 가르는 경계다.</p>

<p><span class="step">④ A를 구한다.</span>
<span class="m">A</span>는 <b>직선 <span class="m">x = 15</span></b>에 붙어 있는 쪽이므로
<span class="m">15</span>부터 <span class="m">f</span>가 <span class="m">0</span>이 되는
<span class="m">16</span>까지다. <span class="m">f &lt; 0</span>이므로 넓이는 적분값에 음의 부호를 붙인다.</p>
<p class="m">A = −∫<sub>3</sub><sup>4</sup>(t<sup>2</sup> − 6t + 8)dt</p>
<p class="m">∫(t<sup>2</sup>−6t+8)dt = t<sup>3</sup>/3 − 3t<sup>2</sup> + 8t</p>
<p class="m">t = 4 : 64/3 − 48 + 32 = 64/3 − 16</p>
<p class="m">t = 3 : 9 − 27 + 24 = 6</p>
<p class="m">∫<sub>3</sub><sup>4</sup> = (64/3 − 16) − 6 = 64/3 − 22 = −2/3</p>
<p class="m">A = −(−2/3) = 2/3</p>

<p><span class="step">⑤ B를 구한다.</span>
<span class="m">B</span>는 <b>직선 <span class="m">x = 19</span></b>에 붙어 있는 쪽이므로
<span class="m">16</span>부터 <span class="m">19</span>까지다. 여기서는 <span class="m">f &gt; 0</span>이므로
적분값이 곧 넓이다. <span class="m">t = x − 18</span>로 옮기면 구간은
<span class="m">[−2, 1]</span>이고, <span class="m">t = 0</span>에서 식이 바뀐다.</p>
<p class="m">∫<sub>−2</sub><sup>0</sup>(4t+8)dt = [2t<sup>2</sup> + 8t]<sub>−2</sub><sup>0</sup> = 0 − (8 − 16) = 8</p>
<p class="m">∫<sub>0</sub><sup>1</sup>(t<sup>2</sup>−6t+8)dt = [t<sup>3</sup>/3 − 3t<sup>2</sup> + 8t]<sub>0</sub><sup>1</sup> = 1/3 − 3 + 8 = 16/3</p>
<p class="m">B = 8 + 16/3 = 24/3 + 16/3 = 40/3</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">B − A = 40/3 − 2/3 = 38/3</p>
<p class="m">답 ③</p>

## 함정

<b><span class="m">15</span>를 <span class="m">6</span>으로 나눈 나머지로 옮길 때
기본 구간이 <span class="m">[0, 6)</span>이 아니라 <span class="m">[−2, 4)</span>임에 주의한다.</b>
<span class="m">15 − 12 = 3</span>은 구간 안이지만
<span class="m">17 − 12 = 5</span>는 구간 밖이라 <span class="m">6</span>을 더 빼야 한다.
그래서 <span class="m">x = 16</span>에서 옮기는 양이 <span class="m">12</span>에서
<span class="m">18</span>로 바뀐다.<br><br>
그리고 <b>넓이는 음수가 될 수 없다.</b> <span class="m">f &lt; 0</span>인 구간에서
적분값을 그대로 쓰면 <span class="m">A = −2/3</span>이 되어
<span class="m">B − A = 42/3 = 14</span>라는 오답(⑤)이 나온다.

## 노하우

<b>주기함수 문제는 &lsquo;기본 구간으로 옮기기&rsquo;가 첫 수순이다.</b>
주기가 <span class="m">p</span>면 <span class="m">p</span>의 배수를 더하거나 빼서
정의가 주어진 구간 안으로 넣는다. 그래프를 멀리까지 그리려 하면 안 된다.<br><br>
<b>연속 조건은 조각이 만나는 곳마다 하나씩 나온다.</b>
이 문제처럼 주기가 있으면 <b>구간의 오른쪽 끝도 왼쪽 끝과 이어져야</b> 하므로
조건이 두 개가 되어 미지수 두 개를 정확히 결정한다.<br><br>
<b>넓이를 물으면 부호가 바뀌는 점을 먼저 찾는다.</b>
그 점이 두 영역을 가르는 경계이고, 음수 구간에서는 적분값에 음의 부호를 붙인다.
