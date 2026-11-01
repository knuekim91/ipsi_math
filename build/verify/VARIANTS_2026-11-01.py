# -*- coding: utf-8 -*-
"""2026-11-01 변형문항 검증 : STA-W03-V1~V3 (표본평균), DIF-W06-V1~V3 (극한 삼차함수).

STA : 표준정규분포표(z = 0.5, 1.0, 1.5, 2.0, 2.5) 로 읽히는 값만 쓴다.
DIF : g = f ± x^2 의 근 구조와 극한의 0 아님 조건으로 f 를 정한다.
"""
from itertools import permutations
from fractions import Fraction as F
from collections import Counter
from math import sqrt
from sympy import symbols, limit, expand, factor, solve, Rational

TABLE = {0.5: 0.192, 1.0: 0.341, 1.5: 0.433, 2.0: 0.477, 2.5: 0.494}


def tail_1000(z):
    """P(Z >= z) 를 표로 읽어 1000 배 (z>0)."""
    return round(1000 * (0.5 - TABLE[z]))


def moments(values):
    """값 -> 확률 딕셔너리의 평균, 분산"""
    E = sum(k * v for k, v in values.items())
    V = sum(k * k * v for k, v in values.items()) - E * E
    return E, V


print("=== STA-W03-V1 (쉬움) : X in {1,3} 각 1/2, n=100, P(Xbar >= 2.1) ===")
E, V = moments({1: F(1, 2), 3: F(1, 2)})
n = 100
z = (2.1 - float(E)) / sqrt(float(V) / n)
print("  E=%s V=%s z=%.2f  1000p=%d   (기대 159)" % (E, V, z, tail_1000(round(z, 1))))

print("\n=== STA-W03-V2 (어려움) : 1~5 순열, X = #{n : n+a_n 홀수}, n=400, P(Xbar >= 2.52) ===")
A = list(permutations(range(1, 6)))
cnt = Counter(sum(1 for m in range(1, 6) if (m + a[m-1]) % 2 == 1) for a in A)
P = {k: F(v, len(A)) for k, v in cnt.items()}
E, V = moments(P)
n = 400
z = (2.52 - float(E)) / sqrt(float(V) / n)
print("  분포 %s  E=%s V=%s  z=%.2f  1000p=%d   (기대 23)"
      % ({k: str(v) for k, v in sorted(P.items())}, E, V, z, tail_1000(round(z, 1))))

print("\n=== STA-W03-V3 (역추론) : X in {1,3} 각 1/2, P(Xbar >= 2.3) 의 p 가 0.067 일 때 n ===")
for n in [9, 16, 25, 36]:
    z = (2.3 - 2) / sqrt(1.0 / n)
    print("  n=%-3d z=%.2f  1000p=%d" % (n, z, tail_1000(round(z, 1)) if round(z, 1) in TABLE else -1))
print("  (1000p = 67 이 되는 n 은 25)")

x, c = symbols('x c')
print("\n=== DIF-W06-V1 (쉬움) : f(x)+x^2 의 근이 0(중근), -1 뿐, 최고차항 -1 -> f(2) ===")
f1 = -x**3 - 2*x**2
g1 = f1 + x**2
print("  g =", factor(g1), "  f(2) =", f1.subs(x, 2), "  (-16 ?)")

print("\n=== DIF-W06-V2 (어려움) : 분모 f(x)-x^2, 극한이 모든 실수 t 에서 존재하고 0 아님 -> f(-3) ===")
fc = c*x**3 - c*x**2 + x**2
print("  g = f - x^2 =", factor(fc - x**2), "   f(t)-t =", factor(fc - x))
fv = fc.subs(c, -1)
print("  c = -1 :  f =", expand(fv), "  f(-3) =", fv.subs(x, -3), "  (45 ?)")
for tv in [-2, Rational(-1, 2), 0, Rational(1, 2), 1, 2, 3]:
    L = limit((x + tv) * (x - fv.subs(x, tv)) / (fv - x**2), x, tv)
    print("    t=%-5s 극한 = %s" % (tv, L))

print("\n=== DIF-W06-V3 (구하는 대상 바꾸기) : 원문항과 같은 조건, t=2 에서 극한값 ===")
f0 = -x**3 - 2*x**2
L2 = limit((x + 2) * (x - f0.subs(x, 2)) / (f0 + x**2), x, 2)
print("  f =", expand(f0), "   lim_{x->2} = %s  (-6 ?)" % L2)
