---
id: INT-J15
unit: 06-적분
topic: 절댓값 정적분과 부호 변화
level: 4점
difficulty: 상
source: 2027-06모평 15번
exam: 2027-06모평
origin: 기출
core: "∫|f| ≠ |∫f| 는 그 구간에서 f가 부호를 바꾼다는 뜻이다"
tags: [절댓값적분,부호변화,삼차함수]
status: seed
added: 2026-09-06
answer: ④
---

## 문제

<p>상수항이 0인 삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킨다.</p><span class="cond">(가) <span class="m">∫<sub>p</sub><sup>p+3</sup>|f(x)|dx ≠ |∫<sub>p</sub><sup>p+3</sup>f(x)dx|</span>를 만족시키는 모든 실수 <span class="m">p</span>의 값의 범위는 <span class="m">0 &lt; p &lt; 3</span>이다.<br><br>(나) <span class="m">∫<sub>0</sub><sup>3</sup>|f(x) + q|dx ≠ |∫<sub>0</sub><sup>3</sup>(f(x) + q)dx|</span>를 만족시키는 모든 실수 <span class="m">q</span>의 값의 범위는 <span class="m">0 &lt; q &lt; 1</span>이다.</span><p><span class="m">f(6)</span>의 값은?</p><div class="choices"><span>① 21</span><span>② 23</span><span>③ 25</span><span>④ 27</span><span>⑤ 29</span></div>

## 발상

<b><span class='m'>∫|g| = |∫g|</span>가 성립하는 것은 g가 그 구간에서 부호를 바꾸지 않을 때뿐이다.</b> 그러니 &lsquo;≠&rsquo;라는 조건은 전부 <b>&lsquo;부호가 바뀐다&rsquo;</b>로 번역된다. 이 번역 하나로 문제가 그래프 문제로 바뀐다.

## 풀이

<p><span class="step">① 두 조건의 &lsquo;≠&rsquo;가 무슨 뜻인지 번역한다.</span>
<span class="m">∫|F| = |∫F|</span>가 성립하는 것은
<b><span class="m">F</span>가 그 구간에서 부호를 바꾸지 않을 때뿐</b>이다.
그러므로 <span class="m">≠</span>라는 조건은 모두
<b>&lsquo;그 구간에서 부호가 바뀐다&rsquo;</b>로 읽으면 된다.
이 번역 하나로 적분 문제가 그래프 문제가 된다.</p>

<p><span class="step">② (가)를 번역한다.</span>
길이가 <span class="m">3</span>인 구간 <span class="m">[p, p+3]</span> 안에서
<span class="m">f</span>가 부호를 바꾼다는 뜻이다.
<span class="m">f</span>의 부호가 바뀌는 점이 <span class="m">c</span> 하나뿐이라면
그 점이 구간 안에 들어와야 하므로</p>
<p class="m">p &lt; c &lt; p + 3 ⟺ c − 3 &lt; p &lt; c</p>
<p>주어진 범위가 <span class="m">0 &lt; p &lt; 3</span>이므로 양쪽을 비교하면</p>
<p class="m">c = 3</p>
<p>즉 <b>부호가 바뀌는 점은 <span class="m">x = 3</span> 하나뿐</b>이다.</p>

<p><span class="step">③ f의 꼴을 정한다.</span>
&lsquo;상수항이 0&rsquo;이므로 <span class="m">f(0) = 0</span>, 즉 <span class="m">x = 0</span>은 근이다.
그런데 ②에서 <b>부호가 바뀌는 점은 <span class="m">3</span>뿐</b>이라고 했으므로
<span class="m">x = 0</span>에서는 근이면서도 부호가 바뀌지 않아야 한다.
<b>근이지만 부호가 안 바뀌는 것은 중근</b>이다.</p>
<p class="m">f(x) = k x<sup>2</sup>(x − 3) &nbsp; (k ≠ 0)</p>

<p><span class="step">④ (나)를 위해 [0, 3]에서 f의 값 범위를 구한다.</span>
<span class="m">k &gt; 0</span>이라 하자.
<span class="m">[0, 3]</span>에서는 <span class="m">x<sup>2</sup> ≥ 0</span>이고 <span class="m">x − 3 ≤ 0</span>이므로
<span class="m">f ≤ 0</span>이다. 최솟값을 찾기 위해 미분한다.</p>
<p class="m">f(x) = k(x<sup>3</sup> − 3x<sup>2</sup>) → f′(x) = k(3x<sup>2</sup> − 6x) = 3kx(x − 2)</p>
<p class="m">f′(x) = 0 → x = 0 또는 x = 2</p>
<p class="m">f(2) = k(8 − 12) = −4k &nbsp; (최솟값)</p>
<p>양 끝에서는 <span class="m">f(0) = f(3) = 0</span>이므로
<span class="m">[0,3]</span>에서 <span class="m">f</span>의 값은 <span class="m">−4k</span>부터 <span class="m">0</span>까지다.</p>

<p><span class="step">⑤ f + q가 부호를 바꿀 조건을 쓴다.</span>
<span class="m">f</span>에 <span class="m">q</span>를 더하면 그래프가 <span class="m">q</span>만큼 위로 올라간다.
값의 범위는 <span class="m">q − 4k</span>부터 <span class="m">q</span>까지가 된다.
<b>부호가 바뀌려면 최댓값은 양수, 최솟값은 음수</b>여야 한다.</p>
<p class="m">q &gt; 0 &nbsp;이고&nbsp; q − 4k &lt; 0</p>
<p class="m">0 &lt; q &lt; 4k</p>

<p><span class="step">⑥ k를 구한다.</span>
문제가 준 범위가 <span class="m">0 &lt; q &lt; 1</span>이므로</p>
<p class="m">4k = 1 → k = 1/4</p>
<p class="m">f(x) = (1/4)x<sup>2</sup>(x − 3)</p>

<p><span class="step">⑦ 답을 계산한다.</span></p>
<p class="m">f(6) = (1/4) × 6<sup>2</sup> × (6 − 3) = (1/4) × 36 × 3 = 27</p>
<p class="m">답 ④</p>

## 함정

<span class='m'>x = 0</span>이 근이라는 것만 보고 <span class='m'>f = kx(x−3)(x−r)</span>처럼 단순근으로 두면 부호 변화점이 늘어나 (가)의 범위가 <span class='m'>0&lt;p&lt;3</span>이 되지 않는다. <b>&lsquo;근이지만 부호는 안 바뀐다&rsquo; = 중근</b>이 이 문제의 핵심 한 줄이다.

## 노하우

<b><span class='m'>∫|g| = |∫g|</span> ⟺ g가 부호를 바꾸지 않는다.</b> 9월 확통 7번의 <span class='m'>Σ|a| = |Σa|</span>와 정확히 같은 구조다 — 절댓값을 밖으로 뺄 수 있는 것은 <b>부호가 한쪽으로 통일될 때뿐</b>이라는 하나의 원리. 그리고 <b>&lsquo;근이지만 부호가 안 바뀐다 = 중근(짝수 개로 겹친 근)&rsquo;</b>은 다항함수 문제의 상비 도구다.
