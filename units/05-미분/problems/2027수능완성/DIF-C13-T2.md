---
id: DIF-C13-T2
parent: DIF-C13
unit: 05-미분
topic: 평행이동해도 겹치는 그래프의 식
level: 3점
difficulty: 중
source: 사다리 2단 (DIF-C13 조건 (나)가 평행이동인 이유)
origin: 사다리
core: "y = f(x)를 (a, b)만큼 옮긴 곡선은 y = f(x−a) + b 이고, 이것이 처음 곡선과 같다는 말이 f(x+a) = f(x) + b 이다"
tags: [평행이동,그래프,함수방정식]
status: variant
added: 2026-09-08
answer: ①
---

## 문제

<p>곡선 <span class="m">y = f(x)</span>를 <span class="m">x</span>축의 방향으로
<span class="m">3</span>만큼, <span class="m">y</span>축의 방향으로
<span class="m">5</span>만큼 평행이동하였더니
처음의 곡선 <span class="m">y = f(x)</span>와 완전히 겹쳤다.
모든 실수 <span class="m">x</span>에 대하여 반드시 성립하는 식은?</p>

<div class="fig">
<svg viewBox="0 0 360 210" role="img" aria-label="계단처럼 같은 모양이 되풀이되는 곡선. 곡선 위의 점 P를 오른쪽으로 3, 위로 5만큼 옮기면 다시 곡선 위의 점 Q가 된다.">
  <path class="ax" d="M20 175 L345 175"/>
  <path class="ax" d="M40 195 L40 20"/>
  <path class="cv" d="M40 165 C60 150 70 140 90 138 C110 136 118 128 130 110
                      C150 95 160 85 180 83 C200 81 208 73 220 55
                      C240 40 250 30 270 28 C290 26 298 18 310 5"/>
  <path class="gd" d="M130 110 L220 110 L220 55"/>
  <circle class="pt" cx="130" cy="110" r="4"/>
  <circle class="pt" cx="220" cy="55"  r="4"/>
  <text x="122" y="126" text-anchor="end">P</text>
  <text x="230" y="50"  text-anchor="start">Q</text>
  <text x="175" y="124" text-anchor="middle">3</text>
  <text x="228" y="88"  text-anchor="start">5</text>
  <text x="33"  y="17"  text-anchor="end">y</text>
  <text x="343" y="168" text-anchor="end">x</text>
</svg>
</div>

<div class="choices"><span>① f(x+3) = f(x) + 5</span><span>② f(x+3) = f(x) − 5</span>
<span>③ f(x+5) = f(x) + 3</span><span>④ f(x−3) = f(x) + 5</span>
<span>⑤ f(x+3) = 5f(x)</span></div>

## 발상

<b>&lsquo;평행이동해도 겹친다&rsquo;는 말은 두 가지로 읽을 수 있다.
둘 다 같은 식으로 이어진다.</b><br><br>

<b>첫째, 곡선의 식으로 읽는 방법이다.</b>
곡선 <span class="m">y = f(x)</span>를 <span class="m">x</span>축으로
<span class="m">a</span>, <span class="m">y</span>축으로
<span class="m">b</span>만큼 평행이동한 곡선의 방정식은</p>
<p class="m">y = f(x − a) + b</p>
<p>이다. 이것이 처음 곡선과 <b>같은 곡선</b>이라면
두 식이 모든 <span class="m">x</span>에서 같아야 한다.<br><br>

<b>둘째, 점으로 읽는 방법이다.</b>
곡선 위의 점 <span class="m">P(p, f(p))</span>를
오른쪽으로 <span class="m">a</span>, 위로 <span class="m">b</span>만큼 옮기면
점 <span class="m">Q(p + a, f(p) + b)</span>가 된다.
겹친다는 것은 <b>이 <span class="m">Q</span>도 곡선 위에 있다</b>는 뜻이다.
점이 곡선 위에 있으려면 <span class="m">y</span>좌표가
<span class="m">x</span>좌표에 함수를 먹인 값이어야 하므로
<span class="m">f(p + a) = f(p) + b</span>가 된다.
<b>이 두 번째 읽기가 조건을 가장 곧바로 설명해 준다.</b>

## 풀이

<p><span class="step">① 평행이동한 곡선의 식을 쓴다.</span>
곡선을 <span class="m">x</span>축의 방향으로 <span class="m">3</span>,
<span class="m">y</span>축의 방향으로 <span class="m">5</span>만큼 옮기면,
<b><span class="m">x</span> 자리에 <span class="m">x − 3</span>을 넣고
전체에 <span class="m">5</span>를 더한다.</b></p>
<p class="m">y = f(x − 3) + 5</p>

<p><span class="step">② 겹친다는 조건을 식으로 쓴다.</span>
이 곡선이 처음 곡선 <span class="m">y = f(x)</span>와 완전히 겹치므로,
모든 실수 <span class="m">x</span>에 대하여 두 <span class="m">y</span>값이 같다.</p>
<p class="m">f(x − 3) + 5 = f(x)</p>

<p><span class="step">③ 보기와 같은 모양으로 고친다.</span>
②의 식은 모든 실수 <span class="m">x</span>에서 성립하므로,
<span class="m">x</span> 자리에 <span class="m">x + 3</span>을 넣어도 된다.
<b>이렇게 바꾸어 넣는 것이 허용되는 이유는 &lsquo;모든 실수&rsquo;이기 때문이다.</b></p>
<p class="m">f((x + 3) − 3) + 5 = f(x + 3)</p>
<p>왼쪽 괄호 안을 정리한다.</p>
<p class="m">f(x) + 5 = f(x + 3)</p>
<p>좌우를 바꾸어 쓴다.</p>
<p class="m">f(x + 3) = f(x) + 5</p>
<p class="m">답 ①</p>

<p><span class="step">④ 점으로도 확인해 본다.</span>
그림에서 곡선 위의 점 <span class="m">P</span>를 오른쪽으로
<span class="m">3</span>, 위로 <span class="m">5</span>만큼 옮긴 점이
<span class="m">Q</span>이고, <span class="m">Q</span>도 곡선 위에 있다.
<span class="m">P</span>의 좌표를 <span class="m">(p, f(p))</span>라 하면
<span class="m">Q</span>의 좌표는
<span class="m">(p + 3, f(p) + 5)</span>이다.
<span class="m">Q</span>가 곡선 위에 있으므로</p>
<p class="m">f(p + 3) = f(p) + 5</p>
<p><span class="m">p</span>는 아무 점이나 될 수 있으므로,
이는 모든 실수에서 성립하는 식이다. ③과 같은 결론이다.</p>

## 함정

<b>④번 <span class="m">f(x − 3) = f(x) + 5</span>와 헷갈리기 쉽다.</b>
이 식은 <b>왼쪽으로</b> <span class="m">3</span>만큼 갔을 때
<span class="m">5</span>가 <b>올라간다</b>는 뜻이므로 방향이 반대다.
그림에서 <span class="m">P</span>에서 <span class="m">Q</span>로 갈 때
<span class="m">x</span>도 커지고 <span class="m">y</span>도 커진다는 것을
확인하면 헷갈리지 않는다.<br><br>

<b>평행이동에서 부호가 뒤집히는 것은 <span class="m">x</span>쪽뿐이다.</b>
오른쪽으로 <span class="m">a</span>만큼 옮기면 식에는
<span class="m">x − a</span>가 들어가고,
위로 <span class="m">b</span>만큼 옮기면 그냥
<span class="m">+ b</span>가 붙는다.
<b><span class="m">x</span>는 반대, <span class="m">y</span>는 그대로</b>라고 외워 둔다.<br><br>

<b>⑤번처럼 곱으로 착각하면 안 된다.</b>
<span class="m">y</span>축 방향의 평행이동은 <b>더하기</b>이지 곱하기가 아니다.
곱하기는 확대·축소다.

## 노하우

<b>&lsquo;평행이동해도 겹친다&rsquo;는 조건은 두 가지 모습으로 나온다.</b>
하나는 이 문제처럼 말로 주는 것이고,
다른 하나는 <span class="m">f(x + a) = f(x) + b</span>라는 <b>식으로</b> 주는 것이다.
<b>둘은 완전히 같은 말</b>이므로, 식이 나오면 곧바로 그림을 떠올리고
그림이 나오면 곧바로 식으로 옮길 수 있어야 한다.<br><br>

<b><span class="m">b = 0</span>이면 그것이 바로 주기함수다.</b>
<span class="m">f(x + a) = f(x)</span>는 위아래로는 움직이지 않고
옆으로만 <span class="m">a</span>만큼 옮겨도 겹친다는 뜻이므로,
주기가 <span class="m">a</span>인 함수다.
<b><span class="m">f(x + a) = f(x) + b</span>는 주기함수를 비스듬히 기울여 놓은 것</b>이라고
생각하면 그림이 잘 그려진다.<br><br>

<b>&lsquo;모든 실수 <span class="m">x</span>에 대하여&rsquo;가 있어야
<span class="m">x</span> 자리에 다른 것을 넣을 수 있다.</b>
③에서 <span class="m">x</span>에 <span class="m">x + 3</span>을 넣은 것은
그 문구 덕분이다. 특정한 몇 개의 <span class="m">x</span>에서만 성립하는 식에는
이렇게 바꿔 넣을 수 없다.
