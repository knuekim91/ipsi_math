# -*- coding: utf-8 -*-
"""수능완성 2회 23~30번 검증 (확률과 통계)"""
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
OK = []
def chk(n, got, want): OK.append((n, got, want, got == want))

# 23  X ~ B(64,p), E(X)=16
p = F(16, 64); chk("23", 64*p*(1-p), F(12))

# 24  배반, 4P(A)=P(B^c), P(A∪B)=1/2
from sympy import symbols, solve, Eq, Rational
xA, yB = symbols('xA yB')
s = solve([Eq(xA + yB, Rational(1,2)), Eq(4*xA, 1 - yB)], [xA, yB], dict=True)[0]
chk("24", s[xA], Rational(1,6))

# 25  1,2,3 중복허락 5개 나열 -> 12100 보다 큰 다섯 자리 수
c = sum(1 for d in product("123", repeat=5) if int("".join(d)) > 12100)
chk("25", c, 216)

# 26  n=196, 표본평균 6.3, 95% 신뢰구간이 4a <= m <= 5a
sg, aa = symbols('sg aa', positive=True)
s = solve([Eq(Rational(63,10) - Rational(196,100)*sg/14, 4*aa),
           Eq(Rational(63,10) + Rational(196,100)*sg/14, 5*aa)], [sg, aa], dict=True)[0]
chk("26", s[aa]*s[sg], Integer := 7)

# 27  a,b,c 중복허락 6개, (가) a,b 홀수 개씩·c 1개 이상 (나) 모든 a 는 b 와 이웃
def ok27(w):
    na, nb, nc = w.count('a'), w.count('b'), w.count('c')
    if na % 2 == 0 or nb % 2 == 0 or nc < 1: return False
    for i, ch in enumerate(w):
        if ch != 'a': continue
        if not ((i > 0 and w[i-1] == 'b') or (i < 5 and w[i+1] == 'b')): return False
    return True
chk("27", sum(1 for w in product("abc", repeat=6) if ok27("".join(w))), 58)

# 28  X={1..5}, |f(n+1)-f(n)|<=1, f(2)f(4) 가 3의 배수 -> f(4) 홀수일 확률
tot = fav = 0
for f in product(range(1, 6), repeat=5):
    if any(abs(f[i+1] - f[i]) > 1 for i in range(4)): continue
    if (f[1]*f[3]) % 3: continue
    tot += 1
    if f[3] % 2: fav += 1
chk("28", F(fav, tot), F(29, 41))

# 29  사과4·배6·빵6 을 같은 종류의 접시 3개에 남김없이
#     (가) 빵 1개만 담는 접시가 정확히 1개 (나) 각 접시에 과일 1개 이상
#     (다) 사과를 빵보다 많이 담는 접시가 있다
def parts(n, k):
    """n 을 순서 있는 k 개의 음이 아닌 정수로 쪼갠다"""
    if k == 1: yield (n,); return
    for i in range(n + 1):
        for rest in parts(n - i, k - 1): yield (i,) + rest
seen = set()
for A_ in parts(4, 3):
    for B_ in parts(6, 3):
        for C_ in parts(6, 3):
            pl = tuple(sorted(zip(A_, B_, C_)))       # 접시가 같은 종류 -> 정렬해 중복 제거
            if pl in seen: continue
            if sum(1 for a_, b_, c_ in pl if c_ == 1) != 1: continue
            if any(a_ + b_ == 0 for a_, b_, c_ in pl): continue
            if not any(a_ > c_ for a_, b_, c_ in pl): continue
            seen.add(pl)
n29 = len(seen)

# 접시를 서로 다른 것으로 볼 때의 개수도 같이 본다
cnt_lab = 0
for A_ in parts(4, 3):
    for B_ in parts(6, 3):
        for C_ in parts(6, 3):
            pl = list(zip(A_, B_, C_))
            if sum(1 for a_, b_, c_ in pl if c_ == 1) != 1: continue
            if any(a_ + b_ == 0 for a_, b_, c_ in pl): continue
            if not any(a_ > c_ for a_, b_, c_ in pl): continue
            cnt_lab += 1
print("29 참고: 같은 종류 접시 %d개 / 서로 다른 접시 %d개" % (n29, cnt_lab))
chk("29", n29, 481)

# 30  P(X>=x) = P(Y<=-x+10)  ->  sigma1=sigma2, m1+m2=10
#     a0=1, m1=3, m2=7, sigma=2  ->  k = P(-1<=Z<=2) = 0.341+0.477
chk("30", int(1000*(0.341 + 0.477) + 0.5), 818)

for n, got, want, o in OK:
    print("%3s  %-10s %-10s %s" % (n, got, want, "일치" if o else "★불일치★"))
print("맞은 개수", sum(1 for *_, o in OK if o), "/", len(OK))
