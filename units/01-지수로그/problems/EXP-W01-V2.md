---
id: EXP-W01-V2
parent: EXP-W01
unit: 01-지수로그
topic: 모든 양수 t에 대하여 두 실근을 가질 조건
level: 4점
difficulty: 상
source: 자체 개발 (EXP-W01 변형 · 조건의 뜻을 정면으로 묻기)
origin: 유사문항
core: "회전축 (1,1)이 두 곡선 사이에 있어야 한다는 것이 조건의 전부이고, 그것은 a + b < 1 한 줄로 바뀐다"
tags: [지수함수,로그함수,역함수,실근의개수,부등식,자연수]
status: variant
added: 2026-10-17
answer: 20
---

## 문제

<p>상수 <span class="m">a (a &gt; 1)</span>에 대하여
<span class="m">x &gt; −6</span>에서
<span class="m">a<sup>x</sup> − 6</span>과
<span class="m">log<sub>a</sub>(x + 6)</span> 중 크지 않은 값을
<span class="m">f(x)</span>라 하자.
모든 양수 <span class="m">t</span>에 대하여
<span class="m">x</span>에 대한 방정식</p>

<p class="m">f(x) = t(x − 1) + 1</p>

<p>이 서로 다른 두 실근을 갖도록 하는 모든 자연수
<span class="m">a</span>의 값의 합을 구하시오.</p>

## 발상

<b>모문항에서 가장 모호했던 문장이 이 문항의 전부다.</b>
&lsquo;모든 양수 <span class="m">t</span>에 대하여 서로 다른 두 실근&rsquo;이
<b>그림으로 무슨 뜻인지</b>를 묻는다.<br><br>

<b>직선 <span class="m">y = t(x − 1) + 1</span>은
<span class="m">t</span>가 무엇이든 점 <span class="m">(1, 1)</span>을 지난다.</b>
곧 <span class="m">(1, 1)</span>을 축으로 도는 막대다.
<b>막대를 어떻게 돌려도 그래프를 꼭 두 번 자르려면,
축이 두 곡선이 만드는 눈 모양 안에 갇혀 있어야 한다.</b><br><br>

<b>그리고 <span class="m">(1, 1)</span>은 직선
<span class="m">y = x</span> 위의 점</b>이다.
교점도 <span class="m">y = x</span> 위에 있으므로,
<b>&lsquo;눈 모양 안&rsquo;인지 아닌지는
<span class="m">x = 1</span>에서 지수 곡선이
<span class="m">1</span>보다 아래인지만 보면 된다.</b></p>
<p class="m">a<sup>1</sup> + b &lt; 1</p>
<p><b>조건이 부등식 한 줄로 줄어든다.</b>
여기서는 <span class="m">b = −6</span>이다.

## 풀이

<p><span class="step">① f의 모양을 본다.</span>
<span class="m">b = −6</span>이다.
<span class="m">y = a<sup>x</sup> − 6</span>과
<span class="m">y = log<sub>a</sub>(x + 6)</span>은 서로 역함수이고
<span class="m">a &gt; 1</span>이므로 둘 다 증가함수다.
따라서 <b>두 그래프의 교점은 직선 <span class="m">y = x</span> 위에 있다.</b><br>
<span class="m">x</span>가 <span class="m">−6</span>에 가까우면 로그 쪽이
<span class="m">−∞</span>로 가고 <span class="m">x</span>가 크면
지수 쪽이 훨씬 커지므로,
<span class="m">f</span>는 <b>두 교점 사이에서만 지수 곡선</b>을 따라간다.</p>

<p><span class="step">② 직선의 회전축을 찾는다.</span>
<span class="m">x = 1</span>을 넣으면
<span class="m">y = t × 0 + 1 = 1</span>이므로
<b>직선은 <span class="m">t</span>에 관계없이
<span class="m">(1, 1)</span>을 지난다.</b></p>

<p><span class="step">③ 축이 두 교점 사이에 있어야 함을 밝힌다.</span>
두 교점의 <span class="m">x</span>좌표를
<span class="m">p</span>, <span class="m">q</span>
<span class="m">(p &lt; q)</span>라 하자.<br>
<b><span class="m">p &lt; 1 &lt; q</span>이면</b>
<span class="m">(1, 1)</span>이 눈 모양 안에 있어 막대를 어떻게 돌려도
왼쪽에서 한 번, 오른쪽에서 한 번 자른다.<br>
<b><span class="m">1 ≤ p</span>이거나 <span class="m">q ≤ 1</span>이면</b>
축이 눈 모양 밖(또는 경계)에 있어,
직선을 적당히 돌리면 한 점에서만 만나거나 아예 만나지 않는
양수 <span class="m">t</span>가 생긴다.</p>
<p class="m">∴ p &lt; 1 &lt; q</p>

<p><span class="step">④ 이것을 a에 대한 부등식으로 바꾼다.</span>
<span class="m">p</span>, <span class="m">q</span>는
<span class="m">a<sup>x</sup> − 6 = x</span>의 두 근이다.
<span class="m">g(x) = a<sup>x</sup> − 6 − x</span>라 하면
<span class="m">g</span>는 아래로 볼록하고,
<span class="m">x</span>가 <span class="m">−∞</span>, <span class="m">∞</span>로 갈 때
모두 <span class="m">∞</span>로 간다.
따라서 <b><span class="m">p &lt; 1 &lt; q</span>일 필요충분조건은
<span class="m">g(1) &lt; 0</span></b>이다.</p>
<p class="m">g(1) = a − 6 − 1 = a − 7 &lt; 0</p>
<p class="m">a &lt; 7</p>
<p><b>이것은 <span class="m">(1, 1)</span>이 지수 곡선보다 위에 있다는 말과 같다.</b></p>

<p><span class="step">⑤ 답을 만든다.</span>
<span class="m">a &gt; 1</span>이고 <span class="m">a &lt; 7</span>이므로</p>
<p class="m">1 &lt; a &lt; 7</p>
<p>자연수 <span class="m">a</span>는
<span class="m">2, 3, 4, 5, 6</span>이고</p>
<p class="m">2 + 3 + 4 + 5 + 6 = 20</p>
<p class="m">답 20</p>

<p><span class="step">⑥ 경계를 확인한다.</span>
<span class="m">a = 7</span>이면 <span class="m">g(1) = 0</span>이므로
<span class="m">(1, 1)</span>이 <b>교점 그 자체</b>가 된다.
그러면 큰 쪽 교점이 <span class="m">q = 1</span>이 되어
막대를 가파르게 세웠을 때 한 점에서만 만난다.
<b><span class="m">a = 7</span>은 답에 들어가지 않는다.</b></p>

## 함정

<b><span class="m">a</span>의 범위를 구하고 끝내지 않는다.</b>
묻는 것은 <b>자연수 <span class="m">a</span>의 값의 합</b>이다.
<span class="m">1 &lt; a &lt; 7</span>에서
<span class="m">1</span>과 <span class="m">7</span>은 포함되지 않으므로
<span class="m">2</span>부터 <span class="m">6</span>까지 다섯 개다.
<b><span class="m">a = 1</span>을 넣으면
<span class="m">log<sub>1</sub></span>이 정의되지 않는다.</b><br><br>

<b>교점이 존재하는지 따로 걱정하지 않아도 된다.</b>
<span class="m">g(1) &lt; 0</span>이면 <span class="m">g</span>가
아래로 볼록하고 양쪽 끝에서 <span class="m">∞</span>로 가므로
<b>교점은 저절로 두 개</b>가 된다.
<span class="m">g(1) &lt; 0</span> 한 줄이
&lsquo;교점이 두 개&rsquo;와 &lsquo;그 사이에 1이 있다&rsquo;를
한꺼번에 보장한다.<br><br>

<b>&lsquo;두 실근&rsquo;을 &lsquo;교점이 두 개&rsquo;와 혼동하지 않는다.</b>
문제가 말하는 두 실근은 <b>직선과
<span class="m">y = f(x)</span>의 교점</b>이고,
두 곡선의 교점은 그것을 판정하는 도구일 뿐이다.
<b>그림에 둘을 따로 표시해 둔다.</b>

## 노하우

<b>&lsquo;모든 <span class="m">t</span>에 대하여&rsquo;가 보이면
<span class="m">t</span>가 없는 조건으로 바꾼다.</b>
<span class="m">t</span>마다 따져서는 끝이 없다.
<b><span class="m">t</span>가 만드는 도형이 무엇인지</b>를 먼저 본다.
여기서는 <b><span class="m">(1, 1)</span>을 지나는 모든 직선</b>이었고,
그래서 조건이 <b>점 하나의 위치</b>로 줄었다.<br><br>

<b>점이 곡선의 위냐 아래냐는 대입 한 번이다.</b>
<span class="m">(1, 1)</span>이
<span class="m">y = a<sup>x</sup> + b</span>보다 위에 있다
<span class="m">⟺ a<sup>1</sup> + b &lt; 1</span>
<span class="m">⟺ a + b &lt; 1</span>.
<b>모문항의 <span class="m">a + b = (3/2)<sup>4/3</sup> − 3/4 ≈ 0.97 &lt; 1</span>도
이 조건을 만족시킨다.</b> 검산에 쓸 수 있다.<br><br>

<b>볼록한 함수의 근 두 개 사이에 어떤 수가 있을 조건은
그 수에서의 함숫값이 음수인 것이다.</b></p>
<p class="m">g 가 아래로 볼록, g(±∞) = ∞ 일 때</p>
<p class="m">p &lt; k &lt; q &nbsp; ⟺ &nbsp; g(k) &lt; 0</p>
<p><b>판별식이나 근의 분리를 꺼낼 필요가 없다.</b>
이차함수에서 배운 근의 분리가
지수함수에서도 그대로 통한다는 것을 기억해 둔다.
