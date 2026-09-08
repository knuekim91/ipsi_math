---
id: DIF-C13-T1
parent: DIF-C13
unit: 05-미분
topic: f(x+a)=f(x)+b 를 손으로 써 보기
level: 3점
difficulty: 하
source: 사다리 1단 (DIF-C13 조건 (나))
origin: 사다리
core: "f(x+a) = f(x) + b 는 'a칸 오른쪽으로 가면 b만큼 올라간다'는 뜻이므로, 모르는 값은 아는 구간으로 끌고 온다"
tags: [함수방정식,평행이동,구간]
status: variant
added: 2026-09-08
answer: 27
---

## 문제

<p>함수 <span class="m">f(x)</span>가
<span class="m">0 ≤ x ≤ 2</span>에서
<span class="m">f(x) = 3x<sup>2</sup></span>이고,
모든 실수 <span class="m">x</span>에 대하여</p>
<p class="m">f(x + 2) = f(x) + 12</p>
<p>를 만족시킬 때, <span class="m">f(5)</span>의 값을 구하시오.</p>

## 발상

<b>우리가 아는 것은 <span class="m">0 ≤ x ≤ 2</span>에서의 <span class="m">f</span>뿐이다.</b>
구하려는 <span class="m">f(5)</span>는 그 구간 밖에 있으므로 값을 바로 읽을 수 없다.<br><br>

<b>그래서 주어진 식을 &lsquo;끌고 오는 도구&rsquo;로 쓴다.</b>
<span class="m">f(x + 2) = f(x) + 12</span>를 오른쪽에서 왼쪽으로 읽으면</p>
<p class="m">f(x + 2) − 12 = f(x)</p>
<p>이므로, <b><span class="m">2</span>만큼 왼쪽으로 갈 때마다
<span class="m">12</span>를 빼면 된다.</b>
<span class="m">5</span>에서 <span class="m">2</span>씩 빼 내려가면
<span class="m">3</span>, <span class="m">1</span>이 되고,
<span class="m">1</span>은 우리가 아는 구간 안에 있다.

## 풀이

<p><span class="step">① 아는 구간까지 내려온다.</span>
주어진 식에 <span class="m">x = 3</span>을 넣는다.
<span class="m">3 + 2 = 5</span>이므로 <span class="m">f(5)</span>가 나온다.</p>
<p class="m">f(5) = f(3) + 12</p>
<p>아직 <span class="m">f(3)</span>도 모른다.
같은 식에 <span class="m">x = 1</span>을 넣는다.</p>
<p class="m">f(3) = f(1) + 12</p>
<p><span class="m">1</span>은 <span class="m">0 ≤ x ≤ 2</span> 안에 있으므로
여기서 멈춘다.</p>

<p><span class="step">② 아는 값을 구한다.</span>
<span class="m">0 ≤ x ≤ 2</span>에서
<span class="m">f(x) = 3x<sup>2</sup></span>이므로</p>
<p class="m">f(1) = 3 × 1<sup>2</sup> = 3</p>

<p><span class="step">③ 다시 거슬러 올라간다.</span>
①에서 얻은 두 식에 차례로 대입한다.</p>
<p class="m">f(3) = f(1) + 12 = 3 + 12 = 15</p>
<p class="m">f(5) = f(3) + 12 = 15 + 12 = 27</p>

<p><span class="step">④ 한 번에 쓰면 이렇게 된다.</span>
<span class="m">5 = 1 + 2 × 2</span>이므로
<span class="m">2</span>칸을 두 번 간 것이고,
그때마다 <span class="m">12</span>씩 올라간다.</p>
<p class="m">f(5) = f(1) + 2 × 12 = 3 + 24 = 27</p>
<p class="m">답 27</p>

## 함정

<b><span class="m">f(5) = 3 × 5<sup>2</sup> = 75</span>라고 쓰면 안 된다.</b>
<span class="m">f(x) = 3x<sup>2</sup></span>이라는 식은
<b><span class="m">0 ≤ x ≤ 2</span>에서만</b> 쓸 수 있다.
그 구간 밖에서 <span class="m">f</span>가 어떻게 생겼는지는
조건 <span class="m">f(x + 2) = f(x) + 12</span>가 대신 알려 준다.
<b>구간이 적혀 있으면 그 밖에서는 그 식을 쓰지 않는다.</b><br><br>

<b>더하는 방향을 반대로 하면 안 된다.</b>
오른쪽으로 갈 때 <span class="m">12</span>를 <b>더하고</b>,
왼쪽으로 갈 때 <span class="m">12</span>를 <b>뺀다.</b>
<span class="m">f(5) = f(1) − 24 = −21</span>로 쓰면 방향이 거꾸로다.

## 노하우

<b>모르는 자리는 아는 자리로 끌고 온다.</b>
<span class="m">f(x + a) = f(x) + b</span> 꼴이 주어지면,
구하려는 값에서 <span class="m">a</span>씩 빼 내려가
<b>함수식이 주어진 구간 안으로 들어올 때까지</b> 반복한다.
몇 번 뺐는지 세어 두었다가 그만큼 <span class="m">b</span>를 곱해 더하면 된다.<br><br>

<b>한 줄로 정리하면 이렇다.</b></p>
<p class="m">f(x + na) = f(x) + nb &nbsp; (n은 정수)</p>
<p>이 문제에서는 <span class="m">a = 2</span>,
<span class="m">b = 12</span>, <span class="m">n = 2</span>였다.
<b>이 한 줄이 다음 단계들의 밑바탕이 된다.</b>
