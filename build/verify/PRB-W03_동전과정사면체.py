# -*- coding: utf-8 -*-
"""PRB-W03 과 유사문항 4개 최종 검증. 풀이에 적은 중간값까지 함께 확인한다."""
from fractions import Fraction as F
from collections import defaultdict
from math import comb

def chain(N, die, times):
    D = defaultdict(F)
    for f in die: D[f] += F(1, len(die))
    d, hist = {N: F(1)}, []
    for _ in range(times):
        out = defaultdict(F)
        for a, p in d.items():
            for k, pk in D.items():
                tot = comb(N, k)
                for j in range(k + 1):
                    if j > a or (k - j) > (N - a): continue
                    out[a - j + (k - j)] += p * pk * F(comb(a, j)*comb(N-a, k-j), tot)
        d = dict(out); hist.append(d)
    return hist

ok = True
def case(tag, N, die, target, want_pq, mid_den, mid_want):
    global ok
    h = chain(N, die, 3)
    d = h[2]
    par = target % 2
    base = sum(v for a, v in d.items() if a % 2 == par)
    c = d[target] / base
    pq = c.numerator + c.denominator
    mid = {a: v * mid_den for a, v in sorted(h[1].items())}
    mid_ok = all(mid.get(a) == b for a, b in mid_want.items()) and len(mid) == len(mid_want)
    good = (pq == want_pq) and mid_ok
    ok &= good
    print("%-28s P(%d|%s)=%-7s p+q=%-4d %s" %
          (tag, target, "홀" if par else "짝", c, pq, "일치" if pq == want_pq else "★불일치★"))
    print("      2회 중간값(분모%d) %s  %s" %
          (mid_den, {a: str(b) for a, b in mid.items()}, "일치" if mid_ok else "★불일치★"))

case("PRB-W03   원본",        4, [1,1,1,2], 1, 45, 192, {0:2,1:36,2:89,3:36,4:29})
case("PRB-W03-V1 3개를 묻기", 4, [1,1,1,2], 3, 51, 192, {0:2,1:36,2:89,3:36,4:29})
case("PRB-W03-V2 1122",      4, [1,1,2,2], 1, 47,  48, {0:2,1:12,2:17,3:12,4:5})
case("PRB-W03-V3 동전 3개",   3, [1,1,1,2], 1, 16,  48, {0:6,1:20,2:12,3:10})
case("PRB-W03-V4 1222·짝수", 4, [1,2,2,2], 2, 85,  64, {0:6,1:12,2:27,3:12,4:7})
print()
print("전체", "통과" if ok else "★검토 필요★")
