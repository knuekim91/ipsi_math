---
id: EXP-W01
unit: 01-지수로그
topic: 역함수인 두 곡선과 그 사이를 지나는 직선
level: 4점
difficulty: 상
source: 2027학년도 10월 모의고사(대성) 22번
exam: 오답노트
origin: 기출
core: "a^x+b 와 log_a(x−b)는 서로 역함수라 교점이 반드시 y=x 위에 있다. 직선은 늘 (1,1)을 지나므로 그 점이 두 곡선 사이에 갇혀 있어야 한다"
tags: [지수함수,로그함수,역함수,그래프개형,부등식,실근]
status: wrong
added: 2026-10-17
answer: 81
---

## 문제

<p>두 상수 <span class="m">a (a &gt; 1)</span>, <span class="m">b</span>에 대하여
<span class="m">x &gt; b</span>에서 <span class="m">a<sup>x</sup> + b</span>와
<span class="m">log<sub>a</sub>(x − b)</span> 중 크지 않은 값을
<span class="m">f(x)</span>라 하자.
<span class="m">x &gt; b</span>에서 정의된 함수 <span class="m">f(x)</span>와
모든 양수 <span class="m">t</span>에 대하여 <span class="m">x</span>에 대한 방정식</p>

<p class="m">f(x) = t(x − 1) + 1</p>

<p>이 서로 다른 두 실근 <span class="m">α(t)</span>,
<span class="m">β(t)</span> <span class="m">(α(t) &lt; β(t))</span>를 갖는다.
양의 실수 전체의 집합에서 정의된 두 함수 <span class="m">α(t)</span>,
<span class="m">β(t)</span>가 다음 조건을 만족시킬 때,
<span class="m">16 × a<sup>3</sup></span>의 값을 구하시오.</p>

<div class="cond">
<span class="cond m">(가) β(1) = 2α(1)</span>
<span class="cond m">(나) 부등식 f(α(t)) × f(β(t)) &gt; 0의 해는 0 &lt; t &lt; 4/3이다.</span>
</div>

## 발상

<b>식이 복잡해 보이지만 열쇠는 세 개뿐이다.</b><br><br>

<b>첫째, 두 함수는 서로 역함수다.</b>
<span class="m">y = a<sup>x</sup> + b</span>를 <span class="m">x</span>에 대하여 풀면
<span class="m">x = log<sub>a</sub>(y − b)</span>다.
곧 두 그래프는 <b>직선 <span class="m">y = x</span>에 대하여 대칭</b>이고,
<span class="m">a &gt; 1</span>이라 둘 다 증가함수이므로
<b>교점은 반드시 <span class="m">y = x</span> 위에 있다.</b>
두 곡선은 눈 모양으로 벌어졌다가 다시 만난다.<br><br>

<b>둘째, 직선은 <span class="m">t</span>가 무엇이든 점
<span class="m">(1, 1)</span>을 지난다.</b>
<span class="m">f(x) = t(x − 1) + 1</span>에 <span class="m">x = 1</span>을 넣으면
<span class="m">y = 1</span>이다.
<b>이 직선은 <span class="m">(1, 1)</span>을 축으로 빙글빙글 도는 막대</b>다.
어떻게 돌려도 그래프를 꼭 두 번 자르려면
<b>그 축이 두 곡선 사이에 갇혀 있어야</b> 한다.<br><br>

<b>셋째, 곱의 부호는 <span class="m">x</span>축을 어디서 넘느냐의 문제다.</b>
<span class="m">f(α(t))</span>와 <span class="m">f(β(t))</span>는
<b>두 교점의 <span class="m">y</span>좌표</b>다.
곱이 양수라는 것은 <b>두 교점이 모두 <span class="m">x</span>축 위에 있거나
모두 아래에 있다</b>는 뜻이다.
그 경계는 <b>직선이 <span class="m">f</span>의
<span class="m">x</span>절편을 지날 때</b>다.

## 풀이

<p><span class="step">① 두 함수가 서로 역함수임을 확인한다.</span></p>
<p class="m">y = a<sup>x</sup> + b → y − b = a<sup>x</sup> → x = log<sub>a</sub>(y − b)</p>
<p>곧 <span class="m">y = log<sub>a</sub>(x − b)</span>는
<span class="m">y = a<sup>x</sup> + b</span>의 역함수이고,
두 그래프는 직선 <span class="m">y = x</span>에 대하여 대칭이다.
<span class="m">a &gt; 1</span>이므로 두 함수는 모두 증가함수이고,
<b>증가함수와 그 역함수의 교점은 반드시 직선
<span class="m">y = x</span> 위에 있다.</b></p>

<p><span class="step">② f의 그래프를 그린다.</span>
<span class="m">x</span>가 <span class="m">b</span>에 가까워지면
<span class="m">log<sub>a</sub>(x − b)</span>는
<span class="m">−∞</span>로 가고,
<span class="m">x</span>가 커지면 <span class="m">a<sup>x</sup> + b</span>가
훨씬 빨리 커진다. 곧 <b>양쪽 끝에서는 로그 쪽이 작고,
두 교점 사이에서만 지수 쪽이 작다.</b></p>

<div class="fig"><img src="img/EXP-W01-1.png" width="992" height="736"
  alt="두 곡선 y=a^x+b 와 y=log_a(x−b) 가 직선 y=x 에 대하여 대칭으로 그려져 있고, 제1사분면에서 눈 모양으로 벌어졌다가 두 점에서 만난다. 두 교점의 x좌표가 각각 알파(1), 베타(1) 로 표시되어 있다."></div>

<div class="fig"><img src="img/EXP-W01-2.png" width="992" height="772"
  alt="y=f(x) 의 그래프. 두 교점 바깥에서는 로그 곡선을 따라가고, 두 교점 사이에서는 지수 곡선을 따라가는 증가함수이다. 쓰이지 않는 쪽은 점선으로 그려져 있다."></div>

<p><span class="step">③ t = 1 을 넣어 본다.</span>
<span class="m">t = 1</span>이면 직선은</p>
<p class="m">y = 1 × (x − 1) + 1 = x</p>
<p>이다. 곧 <b><span class="m">α(1)</span>, <span class="m">β(1)</span>은
두 곡선의 교점의 <span class="m">x</span>좌표</b>다.<br>
조건 (가)에서 <span class="m">β(1) = 2α(1)</span>이고
<span class="m">α(1) &lt; β(1)</span>이므로</p>
<p class="m">0 &lt; α(1) &lt; β(1)</p>
<p>이다. 곧 두 교점은 제1사분면 위에 있다.</p>

<p><span class="step">④ (1, 1)이 두 교점 사이에 있어야 함을 밝힌다.</span>
만약 <span class="m">α(1) ≥ 1</span>이거나
<span class="m">β(1) ≤ 1</span>이면,
직선을 적당히 돌렸을 때 그래프와
<b>한 점에서만 만나거나 아예 만나지 않는</b> 양수
<span class="m">t</span>가 생긴다.</p>

<div class="fig"><img src="img/EXP-W01-3.png" width="1125" height="1176"
  alt="네 가지 경우의 그림. 알파(1)=1 인 경우, 베타(1)=1 인 경우, 알파(1)이 1보다 큰 경우, 베타(1)이 1보다 작은 경우 각각에서 직선 y=t(x−1)+1 이 곡선과 한 점에서만 만나거나 만나지 않는 모습이 그려져 있다."></div>

<p>그러므로 <b>모든 양수 <span class="m">t</span>에 대하여 근이 두 개</b>이려면</p>
<p class="m">α(1) &lt; 1 &lt; β(1)</p>

<p><span class="step">⑤ 조건 (나)로 b를 구한다.</span>
<span class="m">f</span>는 증가함수이므로
<span class="m">f(α(t)) &lt; f(β(t))</span>이고,
곱이 양수라는 것은 <b>두 값의 부호가 같다</b>는 뜻이다.<br>
<span class="m">f</span>의 그래프가 <span class="m">x</span>축과 만나는 점을
<span class="m">A</span>라 하자.
그 자리는 두 교점의 바깥이므로 로그 쪽이다.</p>
<p class="m">log<sub>a</sub>(x − b) = 0 → x − b = 1 → x = b + 1</p>
<p class="m">A(b + 1, 0)</p>
<p>직선이 점 <span class="m">A</span>를 지날 때의
<span class="m">t</span>의 값을 <span class="m">m</span>이라 하자.
<b><span class="m">t</span>가 <span class="m">m</span>보다 작은 동안에는
두 교점이 모두 <span class="m">A</span>의 오른쪽에 있어 부호가 같고,
<span class="m">m</span>을 넘으면 한 점이 <span class="m">A</span>의 왼쪽으로 넘어가
부호가 갈린다.</b>
곧 해가 <span class="m">0 &lt; t &lt; m</span>이므로 조건 (나)에서</p>
<p class="m">m = 4/3</p>
<p>직선 <span class="m">y = (4/3)(x − 1) + 1</span>이
<span class="m">(b + 1, 0)</span>을 지나므로</p>
<p class="m">(4/3)(b + 1 − 1) + 1 = 0</p>
<p class="m">(4/3)b + 1 = 0 → b = −3/4</p>

<p><span class="step">⑥ 조건 (가)로 a를 구한다.</span>
<span class="m">α = α(1)</span>이라 하면
<span class="m">β(1) = 2α</span>이고, 둘 다 <span class="m">y = x</span> 위의
교점이므로 <span class="m">a<sup>x</sup> + b = x</span>를 만족시킨다.</p>
<p class="m">a<sup>α</sup> − 3/4 = α → a<sup>α</sup> = α + 3/4</p>
<p class="m">a<sup>2α</sup> − 3/4 = 2α → a<sup>2α</sup> = 2α + 3/4</p>
<p><span class="m">a<sup>2α</sup> = (a<sup>α</sup>)<sup>2</sup></span>이므로</p>
<p class="m">(α + 3/4)<sup>2</sup> = 2α + 3/4</p>
<p class="m">α<sup>2</sup> + (3/2)α + 9/16 = 2α + 3/4</p>
<p class="m">α<sup>2</sup> − (1/2)α − 3/16 = 0</p>
<p>양변에 <span class="m">16</span>을 곱하면</p>
<p class="m">16α<sup>2</sup> − 8α − 3 = 0 → (4α − 3)(4α + 1) = 0</p>
<p class="m">α = 3/4 또는 α = −1/4</p>
<p>④에서 <span class="m">1 &lt; β(1) = 2α</span>이므로
<span class="m">α &gt; 1/2</span>이다. 따라서</p>
<p class="m">α(1) = 3/4, &nbsp; β(1) = 3/2</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">a<sup>3/4</sup> = 3/4 + 3/4 = 3/2</p>
<p>양변을 <span class="m">4</span>제곱하면</p>
<p class="m">a<sup>3</sup> = (3/2)<sup>4</sup> = 81/16</p>
<p class="m">16 × a<sup>3</sup> = 81</p>
<p class="m">답 81</p>

## 함정

<b>&lsquo;크지 않은 값&rsquo;은 작은 쪽이다.</b>
&lsquo;작지 않은 값&rsquo;(큰 쪽)과 바꿔 읽으면 그래프가 위아래로 뒤집혀
처음부터 다른 문제가 된다.
<b>문장을 읽고 작은 쪽인지 큰 쪽인지 먼저 적어 둔다.</b><br><br>

<b><span class="m">t = 1</span>을 넣어 보지 않으면 (가)를 쓸 수 없다.</b>
<span class="m">α(1)</span>, <span class="m">β(1)</span>이 무엇인지 모른 채
식만 보면 막힌다.
<b>조건에 특정한 값이 들어 있으면 그 값을 먼저 대입해 본다.</b>
<span class="m">t = 1</span>일 때 직선이 <span class="m">y = x</span>가 되는 것이
이 문제의 설계다.<br><br>

<b><span class="m">α = −1/4</span>을 버리는 근거를 적어야 한다.</b>
&lsquo;<span class="m">α</span>는 양수니까&rsquo;로는 약하다.
<span class="m">β(1) = 2α &gt; 1</span>이어야 하므로
<span class="m">α &gt; 1/2</span>이다.
<b>④에서 얻은 <span class="m">α(1) &lt; 1 &lt; β(1)</span>이 여기서 쓰인다.</b><br><br>

<b><span class="m">A</span>가 로그 쪽에 있다는 것을 확인한다.</b>
<span class="m">f</span>가 <span class="m">x</span>축을 지나는 자리는
두 교점의 바깥이므로
<span class="m">f = log<sub>a</sub>(x − b)</span>다.
지수 쪽으로 <span class="m">a<sup>x</sup> + b = 0</span>을 풀면 엉뚱한 점이 나온다.

## 노하우

<b><span class="m">a<sup>x</sup> + b</span>와
<span class="m">log<sub>a</sub>(x − b)</span>는 짝이다.</b>
이 둘이 한 문제에 같이 나오면 <b>무조건 역함수</b>이고,
<b>교점은 <span class="m">y = x</span> 위</b>에 있다.
그러면 교점은 <span class="m">a<sup>x</sup> + b = x</span> 한 줄로 구해진다.
<b>두 곡선을 연립할 생각을 하지 않는다.</b><br><br>

<b>직선의 회전축이 어디 있는지 본다.</b>
<span class="m">y = t(x − 1) + 1</span>은 언제나
<span class="m">(1, 1)</span>을 지난다.
<span class="m">y = t(x − p) + q</span> 꼴이면 축은
<span class="m">(p, q)</span>다.
<b>축이 그래프의 어느 쪽에 있는지가 근의 개수를 정한다.</b><br><br>

<b>두 결론은 공식으로 챙겨 둔다.</b></p>
<p class="m">① (1, 1)이 두 곡선 사이에 있을 조건 : a + b &lt; 1</p>
<p class="m">② 부등식의 해가 0 &lt; t &lt; m 일 때 m = −1/b</p>
<p>①은 <span class="m">a<sup>1</sup> + b &lt; 1</span>,
곧 <span class="m">(1, 1)</span>이 지수 곡선보다 위에 있다는 뜻이다.
②는 직선의 <span class="m">x</span>절편
<span class="m">1 − 1/t</span>가 <span class="m">b + 1</span>과 같아지는
<span class="m">t</span>를 구한 것이다.</p>
<p class="m">1 − 1/m = b + 1 → −1/m = b → m = −1/b</p>
<p>이 문제에서는 <span class="m">m = 4/3</span>이므로
<span class="m">b = −3/4</span>이 한 줄에 나온다.
<b>딸림 문항에서 이 두 줄만 쓰는 연습을 한다.</b>
