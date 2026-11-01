# -*- coding: utf-8 -*-
"""STA-W02 (확통 29번) 과 유사문항 3제의 검증.

챙겨 둘 두 줄
  ① B(n,p) 를 따르는 확률변수가 가질 수 있는 값은 0,1,...,n 뿐이다.
     곧 n 은 그 확률변수의 "최댓값"이고, 0 부터 빠짐없이 나와야 한다.
  ② 변환이 일대일이 아니면 겹친 칸에서 확률이 합쳐져 미지수가 남는다.
     남는 미지수의 개수만큼 추가 조건(평균 등)이 필요하다.
"""
from fractions import Fraction as F
from math import comb

def binom(n, p):
    return {y: F(comb(n, y)) * p**y * (1-p)**(n-y) for y in range(n+1)}

def values(xs, g):
    """변환 g 로 생기는 값들과, 값마다 몇 개의 x 가 겹치는지"""
    d = {}
    for x in xs:
        d.setdefault(g(x), []).append(x)
    return d

XS = [-2, -1, 0, 1, 2]

print("=== 원문항 : Y=|X+1|, 평균 2, E(X)=5/6  ->  108 x P(|X-1|=1) ===")
d = values(XS, lambda x: abs(x+1))
print("  Y 의 값 ->", sorted(d), "  n =", max(d), "  겹치는 칸 :",
      {v: k for v, k in d.items() if len(k) > 1})
n = 3; p = F(2, 3)                      # np = 2
B = binom(n, p)
a = F(1, 12)                            # P(X=-2) : 아래에서 E(X) 로 확인
dist = {-2: a, -1: B[0], 0: B[1]-a, 1: B[2], 2: B[3]}
print("  X 의 분포 :", {k: str(v) for k, v in dist.items()})
print("  합 =", sum(dist.values()), "  E(X) =", sum(k*v for k, v in dist.items()), "(=5/6?)")
ans = dist[2] + dist[0]                 # |X-1|=1 -> X=2 또는 X=0
print("  108 x P(|X-1|=1) =", 108*ans, "  (=47?)")
print("  오답 재현 : n=4 로 보면 p=1/2 -> 값이 4 까지 필요해 불가")
print("            겹침을 못 보고 P(X=0)=6/27 로 두면 108x(8/27+6/27) = %d" % (108*(B[3]+B[1])))

print()
print("=== V1 : 이항분포를 따를 수 있는 변환 고르기 ===")
for name, g in [("ㄱ. |X|", lambda x: abs(x)),
                ("ㄴ. |X|+1", lambda x: abs(x)+1),
                ("ㄷ. |X+1|", lambda x: abs(x+1))]:
    vs = sorted(values(XS, g))
    ok = vs == list(range(0, max(vs)+1))
    print("  %-10s 값 %-12s 0 부터 빠짐없이? %-5s  %s"
          % (name, vs, ok, ("가능 n=%d" % max(vs)) if ok else "불가"))

print()
print("=== V2 : Y=|X-1|, P(X=1)=8/27, P(X=2)=1/9  ->  108 x E(X) ===")
d = values(XS, lambda x: abs(x-1))
print("  Y 의 값 ->", sorted(d), "  n =", max(d), "  겹치는 칸 :",
      {v: k for v, k in d.items() if len(k) > 1})
# P(X=1)=P(Y=0)=(1-p)^3 = 8/27  ->  p = 1/3
p2 = F(1, 3); B2 = binom(3, p2)
assert B2[0] == F(8, 27)
d2 = {-2: B2[3], -1: B2[2], 0: B2[1]-F(1, 9), 1: B2[0], 2: F(1, 9)}
print("  X 의 분포 :", {k: str(v) for k, v in d2.items()}, " 합 =", sum(d2.values()))
E2 = sum(k*v for k, v in d2.items())
print("  E(X) =", E2, "  108 x E(X) =", 108*E2, "  (=24?)")

print()
print("=== V3 : Y=|X|, 평균 4/3, E(X)=2/3, P(X=-1)=1/9  ->  9 x V(X) ===")
d = values(XS, lambda x: abs(x))
print("  Y 의 값 ->", sorted(d), "  n =", max(d), "  겹치는 칸 :",
      {v: k for v, k in d.items() if len(k) > 1}, " <- 두 군데")
p3 = F(2, 3); B3 = binom(2, p3)         # 2p = 4/3
print("  Y 의 분포 :", {k: str(v) for k, v in B3.items()})
s = F(1, 3)                             # P(X=2) : E(X)=2/3 에서
d3 = {-2: B3[2]-s, -1: F(1, 9), 0: B3[0], 1: B3[1]-F(1, 9), 2: s}
E3 = sum(k*v for k, v in d3.items())
E3sq = sum(k*k*v for k, v in d3.items())
print("  X 의 분포 :", {k: str(v) for k, v in d3.items()}, " 합 =", sum(d3.values()))
print("  E(X) =", E3, "(=2/3?)   E(X^2) =", E3sq, "   V(X) =", E3sq - E3**2)
print("  9 x V(X) =", 9*(E3sq - E3**2), "  (=16?)")
