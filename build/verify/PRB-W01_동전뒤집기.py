# -*- coding: utf-8 -*-
"""PRB-W01 과 유사문항 4개를 완전탐색으로 검증한다."""
from fractions import Fraction as F
from collections import defaultdict

def anyone(n): return [(F(1, n), [j]) for j in range(n)]
def r_photo(k, n): return [(F(1), [k-1, k])] if k % 2 else anyone(n)
def r_v4(k, n):   return anyone(n) if k % 3 == 0 else [(F(1), [k-1])]

def walk(n, start, rule, times):
    d = {(tuple(start), ()): F(1)}
    for _ in range(times):
        out = defaultdict(F)
        for (s, h), p in d.items():
            for k in range(1, 7):
                for q, idx in rule(k, n):
                    t = list(s)
                    for i in idx: t[i] ^= 1
                    out[(tuple(t), h + (k,))] += p * F(1, 6) * q
        d = dict(out)
    return d

def same(d, n, pred=lambda h: True):
    return sum(p for (s, h), p in d.items()
               if s in ((0,)*n, (1,)*n) and pred(h))

N, TT = 6, [1,1,1,0,0,0]
rows = []
d = walk(N, TT, r_photo, 3);  rows.append(("PRB-W01   원본 3회",        same(d, N), F(5,144), "①"))
d1 = walk(N, TT, r_photo, 2); rows.append(("PRB-W01-V1 2회",            same(d1, N), F(1,18),  "③"))
d2 = walk(N, [0]*6, r_photo, 3); rows.append(("PRB-W01-V2 모두앞면 3회", same(d2, N), F(7,144), "③"))
num = same(d, N, lambda h: all(k % 2 == 0 for k in h))
rows.append(("PRB-W01-V3 조건부", num / same(d, N), F(1,5), "②"))
d4 = walk(N, [0]*6, r_v4, 2); rows.append(("PRB-W01-V4 규칙변형 2회",   same(d4, N), F(11,54), "④"))

ok = True
for name, got, want, ch in rows:
    hit = got == want
    ok &= hit
    print("%-26s %-8s (적은 답 %-7s %s)  %s"
          % (name, got, want, ch, "일치" if hit else "★불일치★"))
print()
print("확률 총합 확인 :", sum(d.values()), sum(d4.values()))
print("대칭 확인 (모두앞면 = 모두뒷면) :",
      sum(p for (s,h),p in d.items() if s==(0,)*N), "=",
      sum(p for (s,h),p in d.items() if s==(1,)*N))
print()
print("전체", "통과" if ok else "★실패★")
