---
id: INT-D15
unit: 06-적분
topic: 절댓값이 있는 정적분으로 정의된 함수
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 15번
exam: 2027-수능완성
origin: 기출
core: "f(x)를 구간별로 정리하면 x ≤ 0과 x ≥ 1에서 직선이 되고, g(x)는 그 바깥에서 상수 ±1/6이 된다"
tags: [정적분으로정의된함수,절댓값적분,구간나누기,부등식]
status: seed
added: 2026-09-07
answer: ⑤
---

## 문제

<p>함수</p>
<p class="m">f(x) = ∫<sub>0</sub><sup>1</sup>|t<sup>3</sup> − xt<sup>2</sup>|dt</p>
<p>에 대하여 함수 <span class="m">g(x)</span>를</p>
<p class="m">g(x) = f(x + 1/2) − f(x)</p>
<p>라 하자. 부등식 <span class="m">|g(x)| &lt; 1/6</span>을 만족시키는 모든 실수
<span class="m">x</span>의 값의 범위가
<span class="m">α &lt; x &lt; β</span>일 때,
<span class="m">f(α) + f(β/2)</span>의 값은?</p>

<div class="choices"><span>① 15/32</span><span>② 23/48</span><span>③ 47/96</span>
<span>④ 1/2</span><span>⑤ 49/96</span></div>

## 발상

<b>적분변수는 <span class="m">t</span>이고 <span class="m">x</span>는 상수 취급한다.</b>
피적분함수를 인수분해하면
<span class="m">t<sup>3</sup> − xt<sup>2</sup> = t<sup>2</sup>(t − x)</span>이다.
적분구간이 <span class="m">0 ≤ t ≤ 1</span>이고 이 구간에서
<span class="m">t<sup>2</sup> ≥ 0</span>이므로,
<b>절댓값의 부호를 결정하는 것은 오직 <span class="m">t − x</span>뿐이다.</b><br><br>

그러므로 <span class="m">x</span>가 적분구간 <span class="m">[0, 1]</span>의
<b>바깥에 있는지 안에 있는지</b>로 경우가 갈린다.
<span class="m">x ≤ 0</span>이면 구간 전체에서
<span class="m">t − x ≥ 0</span>이고,
<span class="m">x ≥ 1</span>이면 구간 전체에서
<span class="m">t − x ≤ 0</span>이다.
이 두 경우에는 절댓값을 통째로 벗길 수 있어 <span class="m">f</span>가
<b><span class="m">x</span>에 대한 일차식</b>이 된다.<br><br>

<b>일차식이면 <span class="m">g(x) = f(x + 1/2) − f(x)</span>가 상수가 된다.</b>
바로 여기가 열쇠다.
<span class="m">x ≤ −1/2</span>이면 <span class="m">x</span>와
<span class="m">x + 1/2</span>이 모두 <span class="m">0</span> 이하이고,
<span class="m">x ≥ 1</span>이면 둘 다 <span class="m">1</span> 이상이다.
이 두 바깥 영역에서 <span class="m">g</span>는 각각
<span class="m">−1/6</span>과 <span class="m">1/6</span>인 상수이므로,
<b>부등호가 <span class="m">&lt;</span>이라서 그 영역이 통째로 제외된다.</b>
따라서 <span class="m">α = −1/2</span>, <span class="m">β = 1</span>이다.

## 풀이

<p><span class="step">① 피적분함수의 부호를 살핀다.</span>
<span class="m">t<sup>3</sup> − xt<sup>2</sup> = t<sup>2</sup>(t − x)</span>이고,
적분구간 <span class="m">0 ≤ t ≤ 1</span>에서
<span class="m">t<sup>2</sup> ≥ 0</span>이다. 따라서</p>
<p class="m">|t<sup>3</sup> − xt<sup>2</sup>| = t<sup>2</sup>|t − x|</p>
<p>이고, 절댓값의 부호는 <span class="m">t − x</span>가 정한다.</p>

<p><span class="step">② x ≤ 0인 경우의 f를 구한다.</span>
<span class="m">x ≤ 0</span>이면 <span class="m">0 ≤ t ≤ 1</span>에서
<span class="m">t − x ≥ 0</span>이므로 절댓값을 그대로 벗긴다.</p>
<p class="m">f(x) = ∫<sub>0</sub><sup>1</sup>t<sup>2</sup>(t − x)dt
= ∫<sub>0</sub><sup>1</sup>(t<sup>3</sup> − xt<sup>2</sup>)dt</p>
<p class="m">= [t<sup>4</sup>/4 − xt<sup>3</sup>/3]<sub>0</sub><sup>1</sup> = 1/4 − x/3</p>

<p><span class="step">③ x ≥ 1인 경우의 f를 구한다.</span>
<span class="m">x ≥ 1</span>이면 <span class="m">0 ≤ t ≤ 1</span>에서
<span class="m">t − x ≤ 0</span>이므로 부호를 바꾸어 벗긴다.</p>
<p class="m">f(x) = ∫<sub>0</sub><sup>1</sup>t<sup>2</sup>(x − t)dt = x/3 − 1/4</p>

<p><span class="step">④ 0 &lt; x &lt; 1인 경우의 f를 구한다.</span>
이때는 <span class="m">t = x</span>를 경계로 부호가 바뀌므로 적분을 끊는다.
<span class="m">0 ≤ t ≤ x</span>에서는 <span class="m">t − x ≤ 0</span>,
<span class="m">x ≤ t ≤ 1</span>에서는 <span class="m">t − x ≥ 0</span>이다.</p>
<p class="m">f(x) = ∫<sub>0</sub><sup>x</sup>t<sup>2</sup>(x − t)dt
+ ∫<sub>x</sub><sup>1</sup>t<sup>2</sup>(t − x)dt</p>
<p>앞 조각을 계산한다.</p>
<p class="m">∫<sub>0</sub><sup>x</sup>(xt<sup>2</sup> − t<sup>3</sup>)dt
= x<sup>4</sup>/3 − x<sup>4</sup>/4 = x<sup>4</sup>/12</p>
<p>뒤 조각을 계산한다.</p>
<p class="m">∫<sub>x</sub><sup>1</sup>(t<sup>3</sup> − xt<sup>2</sup>)dt
= (1/4 − x<sup>4</sup>/4) − x(1/3 − x<sup>3</sup>/3)</p>
<p class="m">= 1/4 − x/3 − x<sup>4</sup>/4 + x<sup>4</sup>/3 = 1/4 − x/3 + x<sup>4</sup>/12</p>
<p>두 조각을 더한다.</p>
<p class="m">f(x) = x<sup>4</sup>/6 − x/3 + 1/4 &nbsp; (0 ≤ x ≤ 1)</p>
<p>양 끝에서 ②, ③의 식과 값이 이어지는지 확인한다.
<span class="m">f(0) = 1/4</span>이고
<span class="m">f(1) = 1/6 − 1/3 + 1/4 = 1/12</span>이며,
③의 식에 <span class="m">x = 1</span>을 넣어도
<span class="m">1/3 − 1/4 = 1/12</span>로 같다.</p>

<p><span class="step">⑤ 바깥 영역에서 g가 상수임을 보인다.</span>
<span class="m">x ≤ −1/2</span>이면 <span class="m">x + 1/2 ≤ 0</span>이므로
<span class="m">x</span>와 <span class="m">x + 1/2</span> 모두 ②의 식을 쓴다.</p>
<p class="m">g(x) = (1/4 − (x + 1/2)/3) − (1/4 − x/3) = −(1/2)/3 = −1/6</p>
<p><span class="m">x ≥ 1</span>이면 <span class="m">x + 1/2 ≥ 1</span>이므로
둘 다 ③의 식을 쓴다.</p>
<p class="m">g(x) = ((x + 1/2)/3 − 1/4) − (x/3 − 1/4) = (1/2)/3 = 1/6</p>
<p>두 경우 모두 <span class="m">|g(x)| = 1/6</span>이다.
문제의 부등식은 <b>등호가 없는</b>
<span class="m">|g(x)| &lt; 1/6</span>이므로,
<b>이 두 영역은 통째로 해에서 빠진다.</b></p>

<p><span class="step">⑥ 가운데 영역에서는 부등식이 성립함을 확인한다.</span>
<span class="m">−1/2 &lt; x &lt; 1</span>에서는
<span class="m">x</span>와 <span class="m">x + 1/2</span> 중
적어도 하나가 구간 <span class="m">(0, 1)</span> 안에 들어와
<span class="m">f</span>의 사차항이 살아난다.
예를 들어 <span class="m">−1/2 &lt; x ≤ 0</span>이면</p>
<p class="m">g(x) = (x + 1/2)<sup>4</sup>/6 − 1/6</p>
<p>이고, <span class="m">0 &lt; x + 1/2 ≤ 1/2</span>이므로
<span class="m">0 &lt; (x + 1/2)<sup>4</sup> ≤ 1/16</span>이 되어</p>
<p class="m">−1/6 &lt; g(x) ≤ 1/96 − 1/6 &lt; 1/6</p>
<p>이다. 나머지 구간에서도 같은 방식으로
<span class="m">|g(x)| &lt; 1/6</span>임이 확인된다.
따라서 부등식의 해는 다음과 같다.</p>
<p class="m">−1/2 &lt; x &lt; 1 → α = −1/2, β = 1</p>

<p><span class="step">⑦ f(α)를 구한다.</span>
<span class="m">α = −1/2 ≤ 0</span>이므로 ②의 식을 쓴다.</p>
<p class="m">f(−1/2) = 1/4 − (−1/2)/3 = 1/4 + 1/6 = 3/12 + 2/12 = 5/12</p>

<p><span class="step">⑧ f(β/2)를 구한다.</span>
<span class="m">β/2 = 1/2</span>이고
<span class="m">0 ≤ 1/2 ≤ 1</span>이므로 ④의 식을 쓴다.</p>
<p class="m">f(1/2) = (1/2)<sup>4</sup>/6 − (1/2)/3 + 1/4</p>
<p class="m">= (1/16)/6 − 1/6 + 1/4 = 1/96 − 16/96 + 24/96 = 9/96 = 3/32</p>

<p><span class="step">⑨ 답을 만든다.</span></p>
<p class="m">f(α) + f(β/2) = 5/12 + 3/32 = 40/96 + 9/96 = 49/96</p>
<p class="m">답 ⑤</p>

## 함정

<b>적분변수와 상수를 바꿔 보면 안 된다.</b>
적분은 <span class="m">t</span>에 대한 것이므로
<span class="m">x</span>는 적분 밖으로 빠져나올 수 있는 상수다.
<span class="m">∫<sub>0</sub><sup>1</sup>xt<sup>2</sup>dt = x/3</span>이지
<span class="m">x<sup>3</sup>/3</span>이 아니다.<br><br>

<b>부등호에 등호가 없다는 것이 답을 결정한다.</b>
바깥 영역에서 <span class="m">|g(x)|</span>는 정확히
<span class="m">1/6</span>이다.
만약 부등식이 <span class="m">≤</span>였다면 해는 실수 전체가 되어
<span class="m">α</span>, <span class="m">β</span>가 존재하지 않는다.
<b>등호가 빠져 있기 때문에</b> 경계가
<span class="m">−1/2</span>과 <span class="m">1</span>로 딱 잡힌다.<br><br>

<b><span class="m">f(β/2)</span>를 <span class="m">f(β)/2</span>로 읽으면 안 된다.</b>
<span class="m">β = 1</span>이므로 <span class="m">β/2 = 1/2</span>이고,
이 값은 <span class="m">0</span>과 <span class="m">1</span> 사이이므로
<b>사차식이 들어 있는 가운데 구간의 식</b>을 써야 한다.
바깥 구간의 일차식을 쓰면 틀린다.

## 노하우

<b>절댓값 적분은 부호를 결정하는 인수만 본다.</b>
<span class="m">|t<sup>3</sup> − xt<sup>2</sup>| = t<sup>2</sup>|t − x|</span>처럼
<b>항상 <span class="m">0</span> 이상인 인수를 절댓값 밖으로 빼내면</b>
경우를 나누는 기준이 하나로 줄어든다.<br><br>

<b>적분구간의 양 끝을 기준으로 경우를 나눈다.</b>
<span class="m">x</span>가 <span class="m">[0, 1]</span>의 왼쪽인지, 안인지,
오른쪽인지 세 가지다.
바깥 두 경우는 절댓값을 통째로 벗기므로 계산이 짧고,
가운데 한 경우만 적분을 끊는다.<br><br>

<b>일차식의 차는 상수다.</b>
<span class="m">f</span>가 어떤 구간에서 <span class="m">x</span>에 대한 일차식이면
<span class="m">f(x + c) − f(x)</span>는 그 구간에서 <b>상수</b>가 된다.
이 성질을 알면 계산하지 않고도 바깥 영역의
<span class="m">g</span> 값을 예상할 수 있고,
경계가 어디인지 먼저 눈에 들어온다.
