# -*- coding: utf-8 -*-
"""STA-W03 (확통 29번 · 표본평균 정규 근사) 검증.

핵심 : 기록값 X 는 0,2,4 세 값 -> 이항분포가 아니다.
       X̄ 의 평균은 E(X), 분산은 V(X)/n. 정규 근사 후 표로 읽는다.
"""
from itertools import permutations
from fractions import Fraction as F
from collections import Counter
from math import sqrt

A = list(permutations([1, 2, 3, 4]))
cnt = Counter(sum(1 for n in range(1, 5) if (n + a[n-1]) % 2 == 1) for a in A)
P = {k: F(v, len(A)) for k, v in cnt.items()}
print("X 의 분포 :", {k: str(v) for k, v in sorted(P.items())}, " (1/6, 2/3, 1/6 ?)")
EX = sum(k*v for k, v in P.items())
EX2 = sum(k*k*v for k, v in P.items())
VX = EX2 - EX*EX
print("E(X) =", EX, "  V(X) =", VX, "  (2, 4/3 ?)")

n = 7500
sd = sqrt(float(VX) / n)
print("sigma(Xbar) =", sd, " (1/75 = %.6f ?)" % (1/75))
z = (59/30 - float(EX)) / sd
print("z =", round(z, 6), "  (-2.5 ?)")

# 표 : P(0<=Z<=z)
table = {0.5: 0.192, 1.0: 0.341, 1.5: 0.433, 2.0: 0.477, 2.5: 0.494}
p = 0.5 + table[round(abs(z), 1)]           # z<0 이므로 P(Z>=z) = 0.5 + P(0<=Z<=|z|)
print("p = %.3f  ->  1000p = %.0f  (994 ?)" % (p, 1000*p))
