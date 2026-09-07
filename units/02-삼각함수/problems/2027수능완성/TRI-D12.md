---
id: TRI-D12
unit: 02-삼각함수
topic: 원에 내접하는 사각형과 사인법칙
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 12번
exam: 2027-수능완성
origin: 기출
core: "AE와 BD가 평행하다는 조건은 ∠AEB = ∠DBC 라는 각의 이동으로 쓰고, 나머지는 모두 사인법칙으로 외접원의 반지름에 묶는다"
tags: [사인법칙,원주각,내접사각형,평행선,동위각]
status: seed
added: 2026-09-07
answer: ②
---

## 문제

<p>그림과 같이 한 원에 내접하고
<span class="m">AB = AC = 2</span>, <span class="m">AD = 1</span>인 사각형
<span class="m">ABCD</span>가 있다.
점 <span class="m">A</span>를 지나고 직선 <span class="m">BD</span>에 평행한 직선이
직선 <span class="m">BC</span>와 만나는 점을 <span class="m">E</span>라 하자.
<span class="m">AE : CD = 2 : 1</span>일 때, 삼각형 <span class="m">AEB</span>의 넓이는?</p>

<div class="fig">
<svg viewBox="0 0 330 235" role="img" aria-label="한 원에 내접하는 사각형 ABCD. 점 A는 원의 위쪽, D는 오른쪽 위, C는 오른쪽 아래, B는 왼쪽 아래에 있다. 직선 BC를 왼쪽으로 늘인 곳에 점 E가 있고, 선분 AE는 선분 BD와 평행하다. 삼각형 AEB가 칠해져 있다.">
  <path class="rg" d="M223 22 L23 200 L157 200 Z"/>
  <circle class="cv" cx="223" cy="124" r="101.5"/>
  <path class="cv" d="M223 22 L307 66 L290 200 L157 200 Z"/>
  <path class="gd" d="M223 22 L290 200"/>
  <path class="gd" d="M157 200 L307 66"/>
  <path class="cv" d="M223 22 L23 200"/>
  <path class="cv" d="M23 200 L290 200"/>
  <path class="gd" d="M186 105 L196 116"/>
  <path class="gd" d="M251 105 L261 116"/>
  <circle class="pt" cx="223" cy="22"  r="3.5"/>
  <circle class="pt" cx="307" cy="66"  r="3.5"/>
  <circle class="pt" cx="290" cy="200" r="3.5"/>
  <circle class="pt" cx="157" cy="200" r="3.5"/>
  <circle class="pt" cx="23"  cy="200" r="3.5"/>
  <text x="223" y="13"  text-anchor="middle">A</text>
  <text x="318" y="60"  text-anchor="middle">D</text>
  <text x="298" y="217" text-anchor="middle">C</text>
  <text x="152" y="217" text-anchor="middle">B</text>
  <text x="16"  y="217" text-anchor="middle">E</text>
</svg>
</div>

<div class="choices"><span>① √6/2</span><span>② √7/2</span><span>③ √2</span>
<span>④ 3/2</span><span>⑤ √10/2</span></div>

## 발상

<b>평행 조건은 길이 조건이 아니라 각의 조건으로 읽는다.</b>
선분 <span class="m">AE</span>와 선분 <span class="m">BD</span>가 평행하고,
세 점 <span class="m">E</span>, <span class="m">B</span>, <span class="m">C</span>가
한 직선 위에 있다. 이 직선을 가로지르는 선으로 보면
<span class="m">∠AEB</span>와 <span class="m">∠DBC</span>는 <b>동위각</b>이므로 서로 같다.
이렇게 하면 그림 바깥에 있던 점 <span class="m">E</span>의 각이
<b>원 안의 각</b>으로 옮겨진다.<br><br>

<b>일단 각이 원 안으로 들어오면 원주각과 사인법칙이 모든 길이를 잇는다.</b>
외접원의 반지름을 <span class="m">R</span>라 하면
한 현의 길이는 <span class="m">(현) = 2R × sin(그 현에 대한 원주각)</span>이다.
<span class="m">AB</span>, <span class="m">AC</span>, <span class="m">AD</span>,
<span class="m">CD</span>가 모두 이 한 식으로 표현되므로,
<b>미지수를 각 두 개로 줄일 수 있다.</b><br><br>

각을 두 개만 남기자. <span class="m">∠DBC = θ</span>,
<span class="m">∠ABC = β</span>라 하면
<span class="m">∠ABD = β − θ</span>가 된다.
주어진 조건 <span class="m">AD = 1</span>과 <span class="m">AE : CD = 2 : 1</span>이
바로 이 두 각에 대한 두 개의 식이 되어, 연립하면 각이 정해진다.

## 풀이

<p><span class="step">① 각을 두 개로 잡는다.</span>
삼각형 <span class="m">ABC</span>는 <span class="m">AB = AC</span>인 이등변삼각형이므로
두 밑각이 같다. 이 밑각을 <span class="m">β</span>라 하자.</p>
<p class="m">∠ABC = ∠ACB = β</p>
<p>점 <span class="m">D</span>가 호 <span class="m">AC</span> 위에 있으므로
반직선 <span class="m">BD</span>는 <span class="m">∠ABC</span>를 둘로 나눈다.
그중 <span class="m">∠DBC</span>를 <span class="m">θ</span>라 하자.</p>
<p class="m">∠DBC = θ, &nbsp; ∠ABD = β − θ</p>

<p><span class="step">② 외접원의 반지름을 구한다.</span>
삼각형 <span class="m">ABC</span>의 외접원의 반지름을
<span class="m">R</span>라 하면, 변 <span class="m">AB</span>가 마주 보는 각은
<span class="m">∠ACB = β</span>이므로 사인법칙에서</p>
<p class="m">AB = 2R sin β → 2 = 2R sin β → R = 1/sin β</p>

<p><span class="step">③ 평행 조건으로 각을 옮긴다.</span>
<span class="m">AE</span>와 <span class="m">BD</span>가 평행하고,
직선 <span class="m">EC</span>가 이 두 직선을 가로지른다.
<span class="m">∠AEB</span>와 <span class="m">∠DBC</span>는 동위각이므로 같다.</p>
<p class="m">∠AEB = ∠DBC = θ</p>
<p>또 세 점 <span class="m">E</span>, <span class="m">B</span>,
<span class="m">C</span>가 이 순서로 한 직선 위에 있으므로
<span class="m">∠ABE</span>와 <span class="m">∠ABC</span>는 서로 보각이다.</p>
<p class="m">∠ABE = 180° − ∠ABC = 180° − β</p>

<p><span class="step">④ 삼각형 AEB에서 AE를 구한다.</span>
삼각형 <span class="m">AEB</span>에 사인법칙을 쓴다.
변 <span class="m">AB</span>가 마주 보는 각은 <span class="m">∠AEB = θ</span>이고,
변 <span class="m">AE</span>가 마주 보는 각은
<span class="m">∠ABE = 180° − β</span>이다.</p>
<p class="m">AB / sin θ = AE / sin(180° − β)</p>
<p><span class="m">sin(180° − β) = sin β</span>이므로</p>
<p class="m">AE = AB × sin β / sin θ = 2 sin β / sin θ</p>

<p><span class="step">⑤ CD를 구한다.</span>
현 <span class="m">CD</span>에 대한 원주각은 <span class="m">∠DBC = θ</span>이므로
사인법칙에서</p>
<p class="m">CD = 2R sin θ = 2 sin θ / sin β</p>

<p><span class="step">⑥ AE : CD = 2 : 1을 식으로 쓴다.</span>
비례식에서 <span class="m">AE = 2 CD</span>이다.</p>
<p class="m">2 sin β / sin θ = 2 × (2 sin θ / sin β)</p>
<p>양변에 <span class="m">sin β sin θ</span>를 곱해 분모를 없앤다.</p>
<p class="m">2 sin<sup>2</sup>β = 4 sin<sup>2</sup>θ → sin<sup>2</sup>β = 2 sin<sup>2</sup>θ</p>
<p><span class="m">β</span>와 <span class="m">θ</span>는 삼각형의 내각이므로
<span class="m">sin β &gt; 0</span>, <span class="m">sin θ &gt; 0</span>이다.</p>
<p class="m">sin β = √2 sin θ &nbsp; … ㉠</p>

<p><span class="step">⑦ AD = 1을 식으로 쓴다.</span>
현 <span class="m">AD</span>에 대한 원주각은
<span class="m">∠ABD = β − θ</span>이므로</p>
<p class="m">AD = 2R sin(β − θ) = 2 sin(β − θ) / sin β = 1</p>
<p class="m">2 sin(β − θ) = sin β &nbsp; … ㉡</p>

<p><span class="step">⑧ 두 식을 연립한다.</span>
㉡의 좌변을 사인의 뺄셈 공식으로 편다.</p>
<p class="m">2(sin β cos θ − cos β sin θ) = sin β</p>
<p>양변을 <span class="m">sin θ</span>로 나눈 뒤, ㉠에서 얻은
<span class="m">sin β / sin θ = √2</span>를 대입한다.</p>
<p class="m">2(√2 cos θ − cos β) = √2</p>
<p class="m">cos β = √2 cos θ − √2/2 &nbsp; … ㉢</p>
<p>한편 ㉠의 양변을 제곱하면
<span class="m">sin<sup>2</sup>β = 2 sin<sup>2</sup>θ</span>이므로</p>
<p class="m">1 − cos<sup>2</sup>β = 2(1 − cos<sup>2</sup>θ) → cos<sup>2</sup>β = 2cos<sup>2</sup>θ − 1 &nbsp; … ㉣</p>

<p><span class="step">⑨ cos θ를 구한다.</span>
㉢을 ㉣에 대입한다.</p>
<p class="m">(√2 cos θ − √2/2)<sup>2</sup> = 2cos<sup>2</sup>θ − 1</p>
<p class="m">2cos<sup>2</sup>θ − 2 cos θ + 1/2 = 2cos<sup>2</sup>θ − 1</p>
<p><span class="m">2cos<sup>2</sup>θ</span>가 양변에서 지워진다.</p>
<p class="m">−2 cos θ + 1/2 = −1 → cos θ = 3/4</p>
<p>따라서 각 삼각비의 값이 차례로 정해진다.</p>
<p class="m">sin θ = √7/4, &nbsp; sin β = √2 × √7/4 = √14/4</p>

<p><span class="step">⑩ 넓이를 구한다.</span>
삼각형 <span class="m">AEB</span>의 세 내각의 합이
<span class="m">180°</span>이므로</p>
<p class="m">∠EAB = 180° − θ − (180° − β) = β − θ</p>
<p>④에서 구한 <span class="m">AE</span>의 값을 계산한다.</p>
<p class="m">AE = 2 sin β / sin θ = 2 × (√14/4) / (√7/4) = 2√2</p>
<p>㉡에서 <span class="m">sin(β − θ) = sin β / 2 = √14/8</span>이다.
두 변과 그 끼인각으로 넓이를 구한다.</p>
<p class="m">(넓이) = (1/2) × AB × AE × sin(∠EAB)</p>
<p class="m">= (1/2) × 2 × 2√2 × (√14/8) = 2√28/8 = 4√7/8 = √7/2</p>
<p class="m">답 ②</p>

## 함정

<b><span class="m">∠ABE</span>를 <span class="m">∠ABC</span>와 같다고 놓으면 안 된다.</b>
점 <span class="m">E</span>는 선분 <span class="m">BC</span> 위가 아니라
그 <b>연장선 위</b>, 곧 <span class="m">B</span>의 바깥쪽에 있다.
그래서 <span class="m">∠ABE</span>는 <span class="m">∠ABC</span>의
<b>보각</b>인 <span class="m">180° − β</span>이다.
다행히 <span class="m">sin(180° − β) = sin β</span>이므로 사인법칙에서는
같은 값이 되지만, 코사인법칙을 쓰려 했다면 부호에서 바로 틀린다.<br><br>

<b><span class="m">AE : CD = 2 : 1</span>에서 어느 쪽이 큰지 헷갈리면 안 된다.</b>
앞이 <span class="m">AE</span>이고 뒤가 <span class="m">CD</span>이므로
<span class="m">AE = 2 CD</span>이다. 반대로 놓으면
㉠이 <span class="m">√2 sin β = sin θ</span>가 되어 답이 달라진다.<br><br>

<b>원주각을 잘못 짝지으면 사인법칙이 무너진다.</b>
현 <span class="m">CD</span>에 대한 원주각은 <span class="m">∠DBC</span>이고
현 <span class="m">AD</span>에 대한 원주각은 <span class="m">∠ABD</span>이다.
<b>현의 양 끝점을 보는 각</b>인지 매번 확인한다.

## 노하우

<b>평행선이 나오면 각을 옮긴다.</b>
도형 문제에서 &lsquo;평행&rsquo;은 거의 언제나 <b>동위각 또는 엇각으로 각을 옮기라</b>는 신호다.
특히 이 문제처럼 <b>원 바깥의 점</b>이 등장하면,
평행 조건이 그 점의 각을 원 안의 원주각으로 데려오는 유일한 통로다.<br><br>

<b>원 문제는 각을 최소한으로 잡는다.</b>
현이 여러 개 나와도 <span class="m">(현) = 2R sin(원주각)</span> 하나로 모두 표현되므로,
<b>독립인 각을 두 개만</b> 정해 두면 나머지는 그 두 각의 식이 된다.
그 뒤에는 주어진 조건의 개수만큼 방정식이 생겨 저절로 풀린다.<br><br>

<b><span class="m">sin</span>만 나오는 식은 제곱해서 <span class="m">cos</span>으로 바꾼다.</b>
<span class="m">sin β = √2 sin θ</span>처럼 사인끼리 묶인 관계식은
제곱한 뒤 <span class="m">sin<sup>2</sup> = 1 − cos<sup>2</sup></span>을 써서
코사인의 관계식으로 바꾸면, 덧셈정리에서 나온 다른 식과 바로 연립된다.
