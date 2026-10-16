---
id: DIF-W05
unit: 05-미분
topic: 같은 함숫값을 갖는 두 점의 위치 조건
level: 4점
difficulty: 상
source: 2027학년도 10월 모의고사(대성) 15번
exam: 오답노트
origin: 기출
core: "x₁x₂ ≤ 0 은 '두 점이 원점을 사이에 둔다'는 뜻이고, 이것이 성립하려면 극대점이 원점이어야 한다. k의 최댓값은 극소점이다"
tags: [삼차함수,극값,그래프개형,같은함숫값,최댓값]
status: wrong
added: 2026-10-17
answer: ②
---

## 문제

<p>최고차항의 계수가 <span class="m">1</span>인 삼차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키는 양의 실수
<span class="m">k</span>의 최댓값이 <span class="m">M</span>이고
<span class="m">M &gt; 3</span>이다.</p>

<div class="cond">
<span class="cond m">x<sub>1</sub> &lt; x<sub>2</sub> ≤ k이고 f(x<sub>1</sub>) = f(x<sub>2</sub>)인 임의의 두 실수 x<sub>1</sub>, x<sub>2</sub>에 대하여</span>
<span class="cond m">x<sub>1</sub>x<sub>2</sub> ≤ 0, &nbsp; (x<sub>2</sub> − 3) × f(x<sub>1</sub> + 5) ≥ 0</span>
<span class="cond m">이다.</span>
</div>

<p><span class="m">f′(3) = −15</span>일 때,
<span class="m">f(1) × M</span>의 값은?</p>

<div class="choices"><span>① 138</span><span>② 140</span><span>③ 142</span>
<span>④ 144</span><span>⑤ 146</span></div>

## 발상

<b><span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>는
&lsquo;같은 높이의 수평선이 그래프와 만나는 두 점&rsquo;이라는 뜻이다.</b>
수평선을 위아래로 움직이면 그런 쌍이 줄줄이 생기는데,
<b>그 모든 쌍이 조건을 지켜야 한다.</b>
그러므로 &lsquo;어느 한 쌍&rsquo;이 아니라 <b>가장 위험한 쌍</b>을 찾아야 한다.<br><br>

<b>첫 번째 조건을 그림으로 읽는다.</b>
<span class="m">x<sub>1</sub>x<sub>2</sub> ≤ 0</span>은
<b>두 점이 원점을 사이에 둔다</b>는 뜻이다.
그런데 <b>극대점 근처에서는 같은 높이의 두 점을 극대점 바로 양옆에</b>
얼마든지 붙여 잡을 수 있다.
그 두 점은 극대점과 같은 부호가 되어 버리므로,
<b>극대점이 원점이 아니면 조건이 깨진다.</b>
이것이 이 문제의 첫 번째 열쇠다.<br><br>

<b>두 번째 열쇠는 <span class="m">k</span>의 역할이다.</b>
극소점 근처에서도 같은 일이 벌어진다.
극소점 양옆의 두 점은 둘 다 양수라 조건을 깬다.
<b><span class="m">k</span>는 그 위험한 쌍이 범위에 들어오지 못하도록 막는 울타리</b>이고,
울타리를 극소점까지 밀 수 있다. 그래서
<b><span class="m">M</span>은 극소점</b>이 된다.

## 풀이

<p><span class="step">① f′(3) &lt; 0 에서 3의 위치를 읽는다.</span>
최고차항의 계수가 양수인 삼차함수는 극대점을 먼저, 극소점을 나중에 지난다.
미분계수가 음수인 구간은 그 사이뿐이다.
극대점을 <span class="m">a</span>, 극소점을 <span class="m">b</span>라 하면</p>
<p class="m">f′(3) = −15 &lt; 0 → a &lt; 3 &lt; b</p>

<p><span class="step">② x₁x₂ ≤ 0 에서 극대점이 원점임을 밝힌다.</span>
극대점 <span class="m">a</span>를 사이에 두고 같은 높이의 두 점을
<b>원하는 만큼 가깝게</b> 잡을 수 있다.
그 두 점을 <span class="m">p</span>, <span class="m">q</span>라 하자.<br>
<b><span class="m">a &gt; 0</span>인 경우</b>:
<span class="m">0 &lt; p &lt; a &lt; q</span>가 되도록 잡으면
<span class="m">pq &gt; 0</span>이다.
<span class="m">a &lt; 3 &lt; M</span>이므로 <span class="m">q</span>를
<span class="m">a</span>에 충분히 가깝게 잡으면
<span class="m">q ≤ k</span>도 된다. 조건에 어긋난다.<br>
<b><span class="m">a &lt; 0</span>인 경우</b>:
<span class="m">p &lt; a &lt; q &lt; 0</span>으로 잡으면
<span class="m">pq &gt; 0</span>이고 <span class="m">q &lt; 0 &lt; k</span>이므로
역시 어긋난다.</p>
<p class="m">∴ a = 0</p>

<p><span class="step">③ f′을 세워 극소점을 구한다.</span>
<span class="m">f′</span>은 최고차항의 계수가 <span class="m">3</span>인 이차함수이고
두 근이 <span class="m">0</span>과 <span class="m">b</span>이므로</p>
<p class="m">f′(x) = 3x(x − b)</p>
<p class="m">f′(3) = 3 × 3 × (3 − b) = 9(3 − b) = −15</p>
<p class="m">3 − b = −5/3 → b = 14/3</p>

<p><span class="step">④ f를 적분으로 복원한다.</span></p>
<p class="m">f′(x) = 3x<sup>2</sup> − 14x</p>
<p class="m">f(x) = x<sup>3</sup> − 7x<sup>2</sup> + C &nbsp; (C는 상수)</p>

<p><span class="step">⑤ 두 번째 조건으로 C를 정한다.</span>
<span class="m">(x<sub>2</sub> − 3) × f(x<sub>1</sub> + 5) ≥ 0</span>은
<span class="m">x<sub>2</sub></span>가 <span class="m">3</span>보다 작으면
<span class="m">f(x<sub>1</sub> + 5) ≤ 0</span>, 크면
<span class="m">f(x<sub>1</sub> + 5) ≥ 0</span>을 요구한다.
<b><span class="m">x<sub>2</sub> = 3</span>인 경계에서는 양쪽이 만나므로
<span class="m">f(x<sub>1</sub> + 5) = 0</span></b>이어야 한다.<br>
<span class="m">x<sub>2</sub> = 3</span>일 때의 짝
<span class="m">x<sub>1</sub></span>을 찾는다.
<span class="m">f(x<sub>1</sub>) = f(3)</span>에서</p>
<p class="m">x<sub>1</sub><sup>3</sup> − 7x<sub>1</sub><sup>2</sup> + C = 27 − 63 + C</p>
<p class="m">x<sub>1</sub><sup>3</sup> − 7x<sub>1</sub><sup>2</sup> + 36 = 0</p>
<p class="m">(x<sub>1</sub> + 2)(x<sub>1</sub> − 3)(x<sub>1</sub> − 6) = 0</p>
<p><span class="m">x<sub>1</sub> &lt; x<sub>2</sub> = 3</span>이고
<span class="m">x<sub>1</sub>x<sub>2</sub> ≤ 0</span>에서
<span class="m">x<sub>1</sub> ≤ 0</span>이므로
<span class="m">x<sub>1</sub> = −2</span>이다.</p>
<p class="m">f(x<sub>1</sub> + 5) = f(3) = 0 → −36 + C = 0 → C = 36</p>
<p class="m">f(x) = x<sup>3</sup> − 7x<sup>2</sup> + 36</p>

<p><span class="step">⑥ M을 구한다.</span>
이제 위험한 쌍은 <b>극소점 양옆</b>뿐이다.
수평선의 높이를 극솟값보다 조금만 높이면,
<span class="m">x = 14/3</span>의 좌우에 양수인 두 점이 생겨
<span class="m">x<sub>1</sub>x<sub>2</sub> &gt; 0</span>이 된다.
<b>그 두 점 중 오른쪽 점은 언제나 <span class="m">14/3</span>보다 크므로</b>,
<span class="m">k ≤ 14/3</span>이면 그 쌍이 범위 밖으로 밀려난다.</p>
<p class="m">M = 14/3 &nbsp; (M &gt; 3 을 만족한다)</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">f(1) = 1 − 7 + 36 = 30</p>
<p class="m">f(1) × M = 30 × 14/3 = 140</p>
<p class="m">답 ②</p>

## 다른 풀이

<b>그래프를 그리지 않고 대수로만 가는 길이 있다.</b>
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>를 직접 전개하면
<b>두 점의 합과 곱 사이의 관계식</b>이 나온다.<br><br>

<span class="m">f(x) = x<sup>3</sup> + ax<sup>2</sup> + bx + c</span>라 하고
<span class="m">f(x<sub>1</sub>) − f(x<sub>2</sub>) = 0</span>을 인수분해한다.</p>
<p class="m">(x<sub>1</sub> − x<sub>2</sub>)(x<sub>1</sub><sup>2</sup> + x<sub>1</sub>x<sub>2</sub> + x<sub>2</sub><sup>2</sup> + a(x<sub>1</sub> + x<sub>2</sub>) + b) = 0</p>
<p><span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>이므로 괄호 안이
<span class="m">0</span>이다.
<span class="m">s = x<sub>1</sub> + x<sub>2</sub></span>,
<span class="m">p = x<sub>1</sub>x<sub>2</sub></span>라 하면
<span class="m">x<sub>1</sub><sup>2</sup> + x<sub>1</sub>x<sub>2</sub> + x<sub>2</sub><sup>2</sup> = s<sup>2</sup> − p</span>이므로</p>
<p class="m">s<sup>2</sup> − p + as + b = 0 → p = s<sup>2</sup> + as + b</p>
<p><b>곱이 합의 이차식으로 나온다.</b> 이것이 숨은 관계식이다.<br><br>

②에서 극대점이 <span class="m">0</span>이므로
<span class="m">f′(0) = b = 0</span>이고</p>
<p class="m">p = s<sup>2</sup> + as = s(s + a)</p>
<p>한편 <span class="m">x<sub>1</sub></span>,
<span class="m">x<sub>2</sub></span>는
<span class="m">T<sup>2</sup> − sT + p = 0</span>의 두 실근이므로
판별식이 <span class="m">0</span> 이상이다.</p>
<p class="m">s<sup>2</sup> − 4p = s<sup>2</sup> − 4s(s + a) = −3s<sup>2</sup> − 4as ≥ 0</p>
<p class="m">3s<sup>2</sup> + 4as ≤ 0 → 0 ≤ s ≤ −4a/3 &nbsp; (a &lt; 0)</p>
<p>그런데 조건 <span class="m">p ≤ 0</span>은
<span class="m">s(s + a) ≤ 0</span>, 곧
<span class="m">0 ≤ s ≤ −a</span>를 요구한다.
<span class="m">−4a/3 &gt; −a</span>이므로
<b><span class="m">−a &lt; s ≤ −4a/3</span>인 쌍은 조건을 어긴다.</b><br>
그 쌍들 중 <span class="m">x<sub>2</sub></span>가 가장 작아지는 것은
판별식이 <span class="m">0</span>이 되는
<span class="m">s = −4a/3</span>일 때이고, 그때</p>
<p class="m">x<sub>1</sub> = x<sub>2</sub> = s/2 = −2a/3 &nbsp; (= 극소점)</p>
<p>이다. 곧 <b>조건을 어기는 쌍의 <span class="m">x<sub>2</sub></span>는
모두 극소점보다 크다.</b></p>
<p class="m">M = −2a/3</p>
<p><span class="m">a = −7</span>이므로
<span class="m">M = 14/3</span>으로 ⑥과 같다.<br><br>

<b>시험장에서는 그래프 쪽이 빠르다.</b> 개형만 그리면 ②가 몇 초 만에 보인다.
다만 <b>이 관계식은 &lsquo;<span class="m">x<sub>1</sub>x<sub>2</sub></span>의 최솟값&rsquo;이나
&lsquo;<span class="m">x<sub>1</sub> + x<sub>2</sub></span>의 범위&rsquo;를 묻는 문제에서는
그래프로 손도 못 대는 것을 한 줄에 끝낸다.</b>

## 함정

<b>&lsquo;임의의 두 실수&rsquo;를 &lsquo;어떤 두 실수&rsquo;로 읽으면 안 된다.</b>
조건을 만족시키는 쌍이 하나라도 있으면 되는 것이 아니라
<b>모든 쌍이 지켜야</b> 한다.
그래서 <b>가장 위험한 쌍</b>, 곧 극점 바로 양옆의 쌍을 찾는 것이 핵심이다.<br><br>

<b><span class="m">M &gt; 3</span>이라는 단서를 흘리면 ②단계가 막힌다.</b>
<span class="m">a &gt; 0</span>인 경우를 버릴 때
&lsquo;<span class="m">q ≤ k</span>도 된다&rsquo;고 말할 수 있는 이유가
<span class="m">k</span>가 <span class="m">3</span>보다 크다는 데 있다.
<b>조건에 있는 모든 단서는 어딘가에서 쓰인다.</b><br><br>

<b><span class="m">x<sub>1</sub> = 6</span>을 고르면 안 된다.</b>
⑤에서 근이 <span class="m">−2, 3, 6</span>으로 셋인데,
<span class="m">x<sub>1</sub> &lt; x<sub>2</sub> = 3</span>이어야 하므로
<span class="m">6</span>은 애초에 탈락이고,
<span class="m">3</span>은 <span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>라 탈락이다.
<b>범위 조건으로 근을 걸러 내는 한 줄</b>을 빠뜨리지 않는다.<br><br>

<b><span class="m">M</span>을 <span class="m">3</span>이라고 답하지 않는다.</b>
<span class="m">f′(3) = −15</span>가 주어졌다고 해서
<span class="m">3</span>이 경계인 것이 아니다.
<span class="m">3</span>은 극대와 극소 <b>사이의 한 점</b>일 뿐이고,
울타리는 극소점까지 밀 수 있다.

## 노하우

<b>&lsquo;같은 함숫값을 갖는 두 점&rsquo;은 수평선으로 생각한다.</b>
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>가 보이면
<b>곧바로 개형을 그리고 수평선을 위아래로 움직인다.</b>
그러면 쌍이 어디서 생기고 어디서 사라지는지가 눈에 보인다.<br><br>

<b>극점 바로 양옆이 가장 위험하다.</b>
극점 근처에서는 같은 높이의 두 점을 <b>원하는 만큼 가깝게</b> 붙일 수 있으므로,
그 두 점은 극점과 사실상 같은 위치로 볼 수 있다.
<b>&lsquo;모든 쌍이 ~이다&rsquo; 꼴의 조건은 거의 언제나 극점에서 판가름난다.</b><br><br>

<b>부등식의 곱이 <span class="m">0</span> 이상이면 경계에서 등호를 본다.</b>
<span class="m">(x<sub>2</sub> − 3) × f(x<sub>1</sub> + 5) ≥ 0</span>에서
<span class="m">x<sub>2</sub> = 3</span>을 넣으면
<span class="m">f(x<sub>1</sub> + 5) = 0</span>이 나와 상수를 정해 준다.
<b>부호가 바뀌는 자리에 값이 숨어 있다.</b><br><br>

<b>삼차함수에는 합과 곱의 관계식이 있다.</b></p>
<p class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>), x<sub>1</sub> ≠ x<sub>2</sub> → x<sub>1</sub>x<sub>2</sub> = (x<sub>1</sub> + x<sub>2</sub>)<sup>2</sup> + a(x<sub>1</sub> + x<sub>2</sub>) + b</p>
<p><b>곱을 합의 이차식으로 바꿔 주는 식</b>이다.
그래프로 보이지 않는 것을 묻는 문제에서는 이쪽이 유일한 길이 된다.
딸림 문항에서 이 식만 쓰는 연습을 해 둔다.
