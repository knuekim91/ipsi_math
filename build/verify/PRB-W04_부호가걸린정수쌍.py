# -*- coding: utf-8 -*-
"""PRB-W04 (2027-10 모평 30번) 과 유사문항 3제의 전수 검증.

핵심
  (가)(나) -> 양수의 합 P, 음수의 절댓값의 합 N 이 P-N=S, P+N=T 로 정해진다.
  (다) |a|+a < |b|+b  <=>  b > 0 이고 a < b        <- 한 줄로 바뀐다
       (|x|+x 는 x>0 이면 2x, x<=0 이면 0 이므로)
"""
from itertools import product

f = lambda x: abs(x) + x

def tuples(S, T, cond=lambda *t: True, allow0=False, W=20):
    R = [x for x in range(-W, W + 1) if allow0 or x != 0]
    return [t for t in product(R, repeat=4)
            if sum(t) == S and sum(abs(x) for x in t) == T and cond(*t)]

da = lambda a, b, c, d: f(a) < f(b)

print("=== (다) 를 한 줄로 바꿀 수 있는가 ===")
all0 = tuples(0, 14)
same = all(((f(a) < f(b)) == (b > 0 and a < b)) for a, b, c, d in all0)
print("  |a|+a<|b|+b  <=>  b>0 이고 a<b  :", same)

print()
print("=== 원문항 PRB-W04 : 합 0, 절댓값의 합 14 ===")
print("  (다) 없이 전체 :", len(all0), "(= 60 + 216 + 60)")
ok = tuples(0, 14, da)
print("  (다) 까지      :", len(ok), "  <- 답")
A = [t for t in ok if t[0] < 0 < t[1]]
B = [t for t in ok if 0 < t[0] < t[1]]
print("    (i)  a<0<b  :", len(A), " = 15 + 72 + 15")
print("    (ii) 0<a<b  :", len(B), " = 12 + 18")
gt = len(tuples(0, 14, lambda a, b, c, d: f(a) > f(b)))
eq = len(tuples(0, 14, lambda a, b, c, d: f(a) == f(b)))
print("  대칭 검산 : %d(<) + %d(>) + %d(=) = %d" % (len(ok), gt, eq, len(ok) + gt + eq))

print()
print("=== V1 : (다) 를 a < b 로 ===")
lt = len(tuples(0, 14, lambda a, b, c, d: a < b))
eq1 = len(tuples(0, 14, lambda a, b, c, d: a == b))
print("  a=b : %d    a<b : %d    (336 - %d)/2 = %d" % (eq1, lt, eq1, (336 - eq1) // 2))

print()
print("=== V2 : 합 4, 절댓값의 합 10  (양수 합 7, 음수 절댓값 합 3) ===")
tot2 = tuples(4, 10)
ok2 = tuples(4, 10, da)
print("  (다) 없이 :", len(tot2), "(= 60 + 72 + 4)")
print("  (다) 까지 :", len(ok2), "  <- 답")
A2 = [t for t in ok2 if t[0] < 0 < t[1]]
B2 = [t for t in ok2 if 0 < t[0] < t[1]]
print("    (i)  a<0<b :", len(A2), " = 15 + 24 + 1")
print("    (ii) 0<a<b :", len(B2), " = 6 + 6 + 6")

print()
print("=== V3 : (다) 와 (라) 를 두 번 ===")
ok3 = tuples(0, 14, lambda a, b, c, d: f(a) < f(b) and f(c) < f(d))
print("  답 :", len(ok3))
for lab, g in (("a<0, c>0", lambda t: t[0] < 0 < t[2]),
               ("a>0, c<0", lambda t: t[2] < 0 < t[0]),
               ("a<0, c<0", lambda t: t[0] < 0 and t[2] < 0),
               ("a>0, c>0", lambda t: t[0] > 0 and t[2] > 0)):
    print("    %s : %d" % (lab, sum(1 for t in ok3 if g(t))))
