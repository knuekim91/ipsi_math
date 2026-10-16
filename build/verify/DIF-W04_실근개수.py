# -*- coding: utf-8 -*-
"""원본과 변형 3문항 검증. g(x)=|x|(ax+b) 의 극대는 b^2/(4a) 다."""
from fractions import Fraction as F
from math import gcd

def N(k, m):
    if k < 0: return 1
    if k == 0: return 2
    if k < m: return 3
    if k == m: return 2
    return 1

def check(tag, A, B, ask, want, want_alpha=None):
    m = F(B*B, 4*A)                       # g 의 극대값
    alpha = F(256, 27) / m**3             # f 의 최고차항 계수
    f = lambda z: alpha*z**3*(z-m) + m
    bad = [z for z in (F(i,2000) for i in range(-int(8*2000), int(8*2000)+1))
           if N(z,m) != N(f(z), m)]
    val = f(ask)
    ok_cnt = (len(bad)==1)
    ok_val = (val == want)
    print("%-26s g=|x|(%dx+%d)  극대 m=%-4s  a=%-7s" % (tag, A, B, m, alpha))
    print("    예외 %d개 %s   f(%s)=%-6s (기대 %s) %s"
          % (len(bad), bad if len(bad)<4 else '...', ask, val, want,
             "일치" if (ok_cnt and ok_val) else "★불일치★"))
    if want_alpha is not None:
        p, q = alpha.denominator, alpha.numerator
        print("    최고차항 계수 %s → p=%d q=%d 서로소=%s  p+q=%d (기대 %d) %s"
              % (alpha, p, q, gcd(p,q)==1, p+q, want_alpha,
                 "일치" if p+q==want_alpha else "★불일치★"))
    print()

check("원본  f(3)",        2, 4, F(3),  F(34), 59)
check("V1    f(-3)",      1, 4, F(-3), F(32))
check("V2    f(-6)",      2, 8, F(-6), F(64))
