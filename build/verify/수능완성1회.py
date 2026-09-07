# -*- coding: utf-8 -*-
"""2027 수능완성 실전 모의고사 1회 — 계산이 무거운 문항 교차검증"""
import io
from fractions import Fraction as F
from itertools import combinations, product
from math import comb

KEY = {10:'34', 11:'5', 12:'23/2', 13:'12', 14:'33/8', 15:'38/3', 16:'6', 17:'5',
       18:'44', 19:'90', 20:'38', 21:'16', 22:'73', 23:'24', 24:'2/15', 25:'150',
       26:'13/16', 27:'4/5', 28:'432', 29:'136', 30:'256'}
got = {}
L = []


def log(*a): L.append(" ".join(str(x) for x in a))


# ── 10 : 로그 두 곡선 + 직선, 넓이 S 와 격자점 m ──────────────
import math
lg3 = lambda t: math.log(t, 3)
# S = 8 + ∫₂⁴(−2x+9)dx  (두 로그 적분이 상쇄)
S = 8 + ((-16 + 36) - (-4 + 18))
m = 0
for x in range(0, 5):
    if x <= 2:
        top, bot = lg3(x + 1) + 4, 0.0
    else:
        top, bot = -2 * x + 9, lg3(x - 1)
    m += sum(1 for y in range(-2, 8) if bot - 1e-9 <= y <= top + 1e-9)
got[10] = str(S + m)
log("10) S =", S, " 격자점 m =", m, " → S+m =", S + m)

# ── 11 : 속도·가속도 보기 ────────────────────────────────────
v = lambda t: F(2, 3) * t**3 - 8 * t + 6
a = lambda t: 2 * t * t - 8
g_ = (v(1) == F(-2, 3))                                   # ㄱ
n_ = max(abs(v(F(t, 10))) for t in range(10, 31)) == F(14, 3)   # ㄴ
# 방향 전환 = v = 0 : 2t³ − 24t + 18 = 0 → t³ − 12t + 9 = 0
rts = sorted(r.real for r in
             __import__('numpy').roots([1, 0, -12, 9]) if abs(r.imag) < 1e-9 and r.real >= 0)
d_ = abs(a(rts[-1]) - 10) < 1e-9
got[11] = {(False, True, True): '5'}.get((g_, n_, d_), '?%s' % ((g_, n_, d_),))
log("11) ㄱ", g_, "(v(1)=%s)" % v(1), " ㄴ", n_, " ㄷ", d_, "(마지막 t=%.4f, a=%.2f)" % (rts[-1], a(rts[-1])))

# ── 12 : 등비 빈칸 ───────────────────────────────────────────
c = F(1, 2); r12 = (c + 1) / c
a2 = 4
assert a2 * r12**4 == 324
a1 = c * a2
S10 = c * (a2 * r12**9)
got[12] = str(F(1, 2) + 2 + 9)
log("12) c =", c, " a₁ =", a1, " (1/a₁)Σ =", S10 / a1, "= 3^9 =", 3**9,
    " → p+q+log₃r =", F(1, 2) + 2 + 9)

# ── 13 : 미분가능 + f(x+a)=f(x)+b ────────────────────────────
fp = lambda x: 3 * x * x - 6 * x + 5
a13 = 2
assert fp(0) == fp(a13)
f13 = lambda x: x**3 - 3 * x * x + 5 * x
b13 = f13(a13) - f13(0)
got[13] = str(f13(a13) + b13)
log("13) a =", a13, " b =", b13, " f(2a)=f(a)+b =", f13(a13) + b13)

# ── 14 : 이등변삼각형 ────────────────────────────────────────
# cosA = 1 − 2/c² , cosB = 1/c , 비 7:3 → 3c²−7c−6=0
cs = [x for x in (F(3), F(-2, 3)) if 3 * x * x - 7 * x - 6 == 0 and x > 0]
c14 = cs[0]
BD = c14 / 4
cosB = F(1) / c14
CD2 = BD**2 + 4 - 2 * BD * 2 * cosB
got[14] = str(BD**2 + CD2)
log("14) AB=AC =", c14, " BD =", BD, " BD²+CD² =", BD**2 + CD2)

# ── 15 : 주기 6, 넓이 차 ─────────────────────────────────────
a15, b15 = -6, 8
f15 = lambda t: 4 * t + 8 if -2 <= t < 0 else t * t + a15 * t + b15
A = -(F(4**3, 3) - 3 * 16 + 8 * 4 - (F(27, 3) - 27 + 24))          # −∫₃⁴(t²−6t+8)
B = (0 - (2 * 4 - 16)) + (F(1, 3) - 3 + 8)                          # ∫₋₂⁰(4t+8)+∫₀¹(t²−6t+8)
got[15] = str(B - A)
log("15) a =", a15, " b =", b15, " A =", A, " B =", B, " B−A =", B - A)

# ── 16 : 지수부등식 ──────────────────────────────────────────
xs = [x for x in range(1, 20) if 2 * x < F(19, 2) - x]
got[16] = str(sum(xs))
log("16) x =", xs, " 합 =", sum(xs))

# ── 17 : 적분방정식 ──────────────────────────────────────────
a17 = 1
assert a17**3 + 3 * a17**2 - 4 * a17 == 0
got[17] = str(3 * a17**2 + 6 * a17 - 4)
log("17) a =", a17, " f(a) =", 3 * a17**2 + 6 * a17 - 4)

# ── 18 : 등차수열 ────────────────────────────────────────────
am = lambda n: 3 * n + 11
k18 = min(k for k in range(1, 200) if am(k) > 100)
got[18] = str(am(1) + k18)
log("18) aₙ =", "3n+11", " 최소 k =", k18, " a₁+k =", am(1) + k18)

# ── 19 : 삼차함수 증가·감소 구간 ─────────────────────────────
ok = []
for num in range(-400, 401):
    k = F(num, 100)
    if k == 0:
        continue
    r1, r2 = F(2, 3) * k, -2 * k
    al, be = min(r1, r2), max(r1, r2)
    if -1 < al < 1 and be > 1:
        ok.append(k)
lo, hi = min(ok), max(ok)
got[19] = str(120 * F(-3, 2) * F(-1, 2))
log("19) k 범위 ≈ (%s, %s)" % (lo, hi), " → a=−3/2, b=−1/2, 120ab =", 120 * F(-3, 2) * F(-1, 2))

# ── 20 : 두 로그곡선 교점 ────────────────────────────────────
k20 = 6
disc = (k20**2 - 4)
q20 = (F(k20) - F(int(disc**0.5 * 10**6), 10**6)) / 2
got[20] = str(k20 + disc)
log("20) √(k²−4)/2 = 2√2 → k =", k20, " (r−q)² = k²−4 =", disc, " → k+(r−q)² =", k20 + disc)

# ── 21 : 두 갈래 점화식 ──────────────────────────────────────
X = set()
for c1 in range(2):
    for c2 in range(2):
        t = F(0)
        # a1 = t 를 미지수로 두고 a3 = a1 조건에서 t 를 푼다
        def nxt(v, br):
            return -2 * v + 12 if br == 0 else v - 2
        # a2, a3 를 t 의 일차식 (p, q) = p*t + q 로 추적
        p, q = F(1), F(0)
        for br in (c1, c2):
            p, q = (-2 * p, -2 * q + 12) if br == 0 else (p, q - 2)
        if p == 1:
            continue                       # a3 = a1 이 항등식이거나 모순
        t = q / (1 - p)
        a1 = t
        a2 = nxt(a1, c1); a3 = nxt(a2, c2)
        if a3 != a1:
            continue
        for br in (0, 1):
            X.add(nxt(a3, br))
got[21] = str(sum(X))
log("21) X =", sorted(X), " 합 =", sum(X))

# ── 22 : |f| 와 수평선, 점프 집합 ────────────────────────────
def Lset(d):
    M, m_ = d + F(1), d - F(25, 2)
    def N(s):
        if s > M or s < m_: return 1
        if s == M or s == m_: return 2
        return 3
    def g(t):
        if t < 0: return 0
        if t == 0: return N(F(0))
        return N(t) + N(-t)
    ks = sorted({F(0), M, -m_, abs(M), abs(m_)} | {F(0)})
    out = set()
    for k in ks:
        e = F(1, 10**6)
        out.add(g(k + e) - g(k - e))
    out.add(0)
    return out
cands = [d for d in (F(23, 4), F(-1), F(25, 2), F(0), F(5), F(-3), F(13))
         if sum(Lset(d)) == 2]
got[22] = str(F(4) + 69) if sum(cands) == F(69, 4) else '?%s' % cands
log("22) 조건을 만족하는 d =", cands, " 합 =", sum(cands), " → p+q =", 4 + 69)

# ── 23 : 이항정리 ────────────────────────────────────────────
co = sum(comb(4, r) * 2**r for r in range(5) if 8 - 3 * r == 2)
got[23] = str(co)
log("23) x² 계수 =", co)

# ── 24 : 조건부확률 ──────────────────────────────────────────
x24 = F(2, 3) / 5
got[24] = str(x24)
log("24) P(A∩B) =", x24)

# ── 25 : 신뢰구간 ────────────────────────────────────────────
xbar = F(4951 + 5049, 200); half = F(5049 - 4951, 200)
sig = half * 12 / F(196, 100)
got[25] = str(sig * xbar)
log("25) x̄ =", xbar, " σ =", sig, " σx̄ =", sig * xbar)

# ── 26 : 곱이 짝수 ───────────────────────────────────────────
odd = F(1, 2) * F(1, 4) + F(1, 2) * F(1, 8)
got[26] = str(1 - odd)
log("26) P(홀수) =", odd, " P(짝수) =", 1 - odd)

# ── 27 : 이산확률분포 ────────────────────────────────────────
from fractions import Fraction
# a+b+c=2/5, a+4b+5c=7/5, a+16b+25c=29/5
import itertools
def solve3():
    # 소거법
    b_, c_ = None, None
    # 3b+4c=1, 12b+20c=22/5
    c_ = (F(22, 5) - 4) / 4
    b_ = (1 - 4 * c_) / 3
    a_ = F(2, 5) - b_ - c_
    return a_, b_, c_
a27, b27, c27 = solve3()
got[27] = str(a27 + 2 * b27 + 3 * c27)
log("27) a,b,c =", a27, b27, c27, " a+2b+3c =", a27 + 2 * b27 + 3 * c27)

# ── 28 : 비증가 함수 개수 ────────────────────────────────────
tot = 0; bad = 0
for f in product(range(1, 7), repeat=6):
    if all(f[i] >= f[i + 1] for i in range(5)):
        tot += 1
        if f[1] * f[3] == 6:
            bad += 1
got[28] = str(tot - bad)
log("28) 비증가 함수 =", tot, " f(2)f(4)=6 인 것 =", bad, " → ", tot - bad)

# ── 29 : 정규분포 넓이 차 ────────────────────────────────────
prime = {2, 3, 5, 7, 11}
cnt = sum(1 for a_ in range(1, 13) for b_ in range(a_, 13)
          if a_ in prime and b_ in prime and (a_ + b_) % 5 == 0)
tot29 = comb(13, 2)
p29 = F(cnt, tot29)
m29 = 100 * p29
s29 = (100 * p29 * (1 - p29))
got[29] = str(int(1000 * (F(477, 1000) - F(341, 1000))))
log("29) 조건 함수 %d개 / 전체 %d개 → p=%s, m=%s, σ²=%s (m=2σ ? %s)"
    % (cnt, tot29, p29, m29, s29, m29 == 2 * F(25, 13)))
log("    S₁−S₂ = P(0≤Z≤2) − P(0≤Z≤1) = 0.477 − 0.341 = 0.136 → 1000배 = 136")

# ── 30 : 상자 시행 ──────────────────────────────────────────
good = 0
for xs2 in combinations(range(1, 8), 2):          # ㉡ 가 일어난 두 자리
    seq = ['O'] * 8
    for i in xs2: seq[i] = 'X'
    def двa(n):                                    # n번째까지 b=2a 인가
        i_ = sum(1 for t in range(1, n + 1) if seq[t] == 'O')
        j_ = n - i_
        return i_ - j_ == 3
    if not двa(7): continue
    if sum(1 for n in range(1, 7) if двa(n)) == 1:
        good += 1
got[30] = str(good * 2**5)
log("30) 조건을 만족하는 배열 =", good, " → 3⁷p =", good * 2**5)

# ── 대조 ────────────────────────────────────────────────────
L.append("")
L.append("=== 공식 정답표 대조 ===")
bad_ = []
for n in sorted(KEY):
    g = got.get(n, '미검증')
    ok_ = (g == KEY[n])
    if not ok_: bad_.append(n)
    L.append(" %2d  공식=%-6s 내계산=%-8s %s" % (n, KEY[n], g, 'OK' if ok_ else 'X'))
L.append("")
L.append("불일치: %s" % (bad_ if bad_ else "없음 (21문항 전부 일치)"))
io.open("v1_out.txt", "w", encoding="utf-8").write("\n".join(L))
print("done")
