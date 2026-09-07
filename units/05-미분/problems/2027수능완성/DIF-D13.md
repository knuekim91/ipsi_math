---
id: DIF-D13
unit: 05-미분
topic: 절댓값 함수의 미분가능성과 사차함수 결정
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 13번
exam: 2027-수능완성
origin: 기출
core: "|g(x)|가 미분가능하지 않은 점은 g의 일차 근이고, 이차 이상의 중근에서는 미분가능하다"
tags: [미분가능성,절댓값함수,사차함수,중근]
status: seed
added: 2026-09-07
answer: ①
---

## 문제

<p>다음 조건을 만족시키는 최고차항의 계수가 <span class="m">1</span>인 모든 사차함수
<span class="m">f(x)</span>에 대하여 모든 <span class="m">f(−1)</span>의 값의 합은?</p>

<div class="cond">
<span class="cond m">(가) f(0) = 0</span>
<span class="cond m">(나) 함수 f(|x − 1|)은 x = 1에서 미분가능하다.</span>
<span class="cond m">(다) 함수 |f(x) − f(1)|이 x = k에서 미분가능하지 않은 실수 k의 개수는 1이다.</span>
</div>

<div class="choices"><span>① 56/3</span><span>② 19</span><span>③ 58/3</span>
<span>④ 59/3</span><span>⑤ 20</span></div>

## 발상

<b>세 조건이 각각 계수 하나씩을 잡아 준다. 순서대로 읽으면 된다.</b><br><br>

조건 (나)는 <span class="m">x = 1</span>을 기준으로 좌우가 <b>대칭으로 접힌</b> 함수를 만든다.
<span class="m">x &gt; 1</span>에서는 <span class="m">f(x − 1)</span>이고
<span class="m">x &lt; 1</span>에서는 <span class="m">f(1 − x)</span>이므로,
접히는 자리에서 두 미분계수가 부호만 반대로 나온다.
그것이 같으려면 <span class="m">f′(0) = 0</span>이어야 한다.<br><br>

조건 (다)가 이 문제의 핵심이다.
<b><span class="m">|g(x)|</span>가 뾰족해지는 곳은
<span class="m">g(x)</span>가 <span class="m">x</span>축을 <b>가로지르며</b>
<span class="m">0</span>이 되는 곳뿐이다.</b>
근의 관점에서 말하면 <b>일차 근(중근이 아닌 근)</b>에서만 미분가능하지 않다.
이차 이상으로 겹친 근에서는 그래프가 <span class="m">x</span>축에 붙었다 떨어지므로
접어도 뾰족해지지 않는다.<br><br>

<span class="m">g(x) = f(x) − f(1)</span>이라 하면
<span class="m">g(1) = 0</span>이므로 <span class="m">1</span>은 항상 근이다.
<span class="m">g</span>는 사차식인데 일차 근이 딱 하나여야 하므로,
남은 차수 <span class="m">3</span>이 통째로 한 근에 몰려야 한다.
곧 <span class="m">g(x) = (x − r<sub>1</sub>)(x − r<sub>2</sub>)<sup>3</sup></span> 꼴이다.

## 풀이

<p><span class="step">① 조건 (나)에서 f′(0) = 0을 얻는다.</span>
<span class="m">h(x) = f(|x − 1|)</span>이라 하자.
<span class="m">x &gt; 1</span>이면 <span class="m">|x − 1| = x − 1</span>이므로
<span class="m">h(x) = f(x − 1)</span>이고,
<span class="m">x &lt; 1</span>이면 <span class="m">|x − 1| = 1 − x</span>이므로
<span class="m">h(x) = f(1 − x)</span>이다.
각각을 미분하여 <span class="m">x = 1</span>에서의 값을 본다.</p>
<p class="m">h′(1+) = f′(0), &nbsp; h′(1−) = −f′(0)</p>
<p><span class="m">h</span>가 <span class="m">x = 1</span>에서 미분가능하므로
두 값이 같아야 한다.</p>
<p class="m">f′(0) = −f′(0) → 2f′(0) = 0 → f′(0) = 0</p>

<p><span class="step">② f의 꼴을 정한다.</span>
<span class="m">f(x) = x<sup>4</sup> + ax<sup>3</sup> + bx<sup>2</sup> + cx + d</span>라 하자.
조건 (가)에서 <span class="m">f(0) = d = 0</span>이다.
또 <span class="m">f′(x) = 4x<sup>3</sup> + 3ax<sup>2</sup> + 2bx + c</span>이므로
①에서 <span class="m">f′(0) = c = 0</span>이다.</p>
<p class="m">f(x) = x<sup>4</sup> + ax<sup>3</sup> + bx<sup>2</sup></p>
<p><b>여기서 얻은 사실을 다음 단계에서 쓸 형태로 바꿔 둔다.</b>
<span class="m">g(x) = f(x) − f(1)</span>이라 하면
<span class="m">g</span>와 <span class="m">f</span>는 상수만 다르므로
<span class="m">g′(x) = f′(x)</span>이고, 따라서</p>
<p class="m">g′(0) = f′(0) = 0</p>
<p>곧 <b><span class="m">g(x)</span>에는 일차항이 없다.</b></p>

<p><span class="step">③ 조건 (다)를 근의 조건으로 바꾼다.</span>
<span class="m">|g(x)|</span>가 <span class="m">x = k</span>에서 미분가능하지 않으려면
<span class="m">g(k) = 0</span>이면서 <span class="m">g</span>가 그곳에서
부호를 바꾸며 지나가야 한다. 곧 <span class="m">k</span>는
<span class="m">g</span>의 <b>일차 근</b>이어야 한다.
<span class="m">g(x) = (x − k)<sup>2</sup>Q(x)</span>처럼 겹친 근에서는
<span class="m">|g|</span>가 그대로 미분가능하다.<br>
<span class="m">g</span>는 최고차항의 계수가 <span class="m">1</span>인 사차식이고
일차 근이 정확히 하나이므로, 나머지 세 개의 근이 한 곳에 겹쳐야 한다.</p>
<p class="m">g(x) = (x − p)(x − q)<sup>3</sup> &nbsp; (p ≠ q)</p>
<p>한편 <span class="m">g(1) = f(1) − f(1) = 0</span>이므로
<span class="m">1</span>은 <span class="m">g</span>의 근이다.
따라서 <span class="m">p = 1</span>이거나 <span class="m">q = 1</span>이다.</p>

<p><span class="step">④ 경우 1: 1이 일차 근일 때.</span>
<span class="m">g(x) = (x − 1)(x − q)<sup>3</sup></span>이라 하자.
곱의 미분법으로 도함수를 구한다.</p>
<p class="m">g′(x) = (x − q)<sup>3</sup> + 3(x − 1)(x − q)<sup>2</sup></p>
<p>②에서 얻은 <span class="m">g′(0) = 0</span>을 쓴다.</p>
<p class="m">g′(0) = (−q)<sup>3</sup> + 3(−1)(q<sup>2</sup>) = −q<sup>3</sup> − 3q<sup>2</sup> = 0</p>
<p class="m">−q<sup>2</sup>(q + 3) = 0 → q = 0 또는 q = −3</p>

<p><span class="step">⑤ 경우 1의 두 함수를 확정한다.</span>
<span class="m">f(0) = 0</span>에서
<span class="m">g(0) = f(0) − f(1) = −f(1)</span>이므로
<span class="m">f(1) = −g(0)</span>이고
<span class="m">f(x) = g(x) + f(1)</span>이다.<br>
<span class="m">q = 0</span>이면 <span class="m">g(x) = (x − 1)x<sup>3</sup></span>이고
<span class="m">g(0) = 0</span>이므로 <span class="m">f(1) = 0</span>이다.</p>
<p class="m">f(x) = x<sup>4</sup> − x<sup>3</sup> → f(−1) = 1 + 1 = 2</p>
<p><span class="m">q = −3</span>이면
<span class="m">g(x) = (x − 1)(x + 3)<sup>3</sup></span>이고
<span class="m">g(0) = (−1)(27) = −27</span>이므로
<span class="m">f(1) = 27</span>이다.</p>
<p class="m">f(−1) = g(−1) + 27 = (−2)(2)<sup>3</sup> + 27 = −16 + 27 = 11</p>

<p><span class="step">⑥ 경우 2: 1이 삼중근일 때.</span>
<span class="m">g(x) = (x − p)(x − 1)<sup>3</sup></span>이라 하자.</p>
<p class="m">g′(x) = (x − 1)<sup>3</sup> + 3(x − p)(x − 1)<sup>2</sup></p>
<p class="m">g′(0) = (−1)<sup>3</sup> + 3(−p)(1) = −1 − 3p = 0 → p = −1/3</p>
<p><span class="m">g(x) = (x + 1/3)(x − 1)<sup>3</sup></span>이고
<span class="m">g(0) = (1/3)(−1) = −1/3</span>이므로
<span class="m">f(1) = 1/3</span>이다.</p>
<p class="m">f(−1) = g(−1) + 1/3 = (−1 + 1/3)(−2)<sup>3</sup> + 1/3</p>
<p class="m">= (−2/3)(−8) + 1/3 = 16/3 + 1/3 = 17/3</p>

<p><span class="step">⑦ 답을 만든다.</span>
조건을 만족시키는 사차함수는 모두 세 개이고,
각각의 <span class="m">f(−1)</span>의 값을 더한다.</p>
<p class="m">2 + 11 + 17/3 = 13 + 17/3 = 39/3 + 17/3 = 56/3</p>
<p class="m">답 ①</p>

## 함정

<b>가장 큰 함정은 &lsquo;근이 하나&rsquo;와 &lsquo;일차 근이 하나&rsquo;를 헷갈리는 것이다.</b>
조건 (다)는 <span class="m">g(x) = 0</span>의 근이 하나라는 말이 아니라,
<span class="m">|g|</span>가 뾰족한 점이 하나라는 말이다.
<b>겹친 근에서는 <span class="m">|g|</span>가 미분가능하다.</b>
그래서 <span class="m">g</span>는 서로 다른 두 개의 실근을 가질 수 있고,
그중 하나가 삼중근이면 된다.<br><br>

<b>삼중근에서 <span class="m">|g|</span>가 미분가능하다는 것을 놓치기 쉽다.</b>
<span class="m">y = |x|</span>는 원점에서 뾰족하지만
<span class="m">y = |x<sup>3</sup>|</span>은 원점에서 접선이
<span class="m">x</span>축인 매끄러운 곡선이다.
차수가 <span class="m">2</span> 이상이면 접어도 뾰족해지지 않는다.<br><br>

<b><span class="m">g′(0) = 0</span>을 쓰는 것을 잊으면 <span class="m">q</span>가 정해지지 않는다.</b>
<span class="m">f</span>에 일차항이 없다는 사실은
<span class="m">g</span>에도 그대로 옮겨진다.
<span class="m">g</span>와 <span class="m">f</span>는 상수만 다르므로
도함수가 완전히 같기 때문이다.<br><br>

<b>세 함수를 모두 찾아야 한다.</b>
경우 1에서 <span class="m">q = 0</span>과 <span class="m">q = −3</span> 두 개,
경우 2에서 하나. 하나라도 빠뜨리면 합이 달라진다.

## 노하우

<b><span class="m">|g(x)|</span>의 미분가능성은 근의 차수로 판정한다.</b>
<span class="m">g</span>의 근 <span class="m">k</span>에서
<span class="m">|g|</span>가 미분가능하지 않을 필요충분조건은
<span class="m">k</span>가 <b>일차 근</b>인 것이다.
근의 차수가 <span class="m">2</span> 이상이면 미분가능하다.
이 한 줄을 알고 있으면 조건 (다) 같은 문장이 곧바로
&lsquo;일차 근의 개수&rsquo;로 번역된다.<br><br>

<b><span class="m">f(|x − a|)</span>가 <span class="m">x = a</span>에서
미분가능할 조건은 <span class="m">f′(0) = 0</span>이다.</b>
안쪽 절댓값은 <span class="m">x = a</span>를 기준으로 그래프를 접는다.
접힌 자리에서 두 미분계수는 부호만 반대이므로,
둘이 같으려면 <span class="m">0</span>이어야 한다.
이것은 자주 나오는 정형화된 결론이므로 외워 두면 좋다.<br><br>

<b>차수를 나누어 배분하는 방식으로 근의 꼴을 정한다.</b>
사차식에서 일차 근이 하나면 남은 차수는 <span class="m">3</span>이고,
겹친 근에 몰아야 하므로 <span class="m">1 + 3</span>밖에 없다.
<span class="m">1 + 2 + 1</span>이나 <span class="m">1 + 1 + 2</span>는
일차 근이 두 개가 되어 조건에 어긋난다.
