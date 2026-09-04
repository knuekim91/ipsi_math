# -*- coding: utf-8 -*-
from itertools import product
from math import comb

def scan(n, ends, total):
    c = 0
    for f in product(range(1, n+1), repeat=n):
        if not ends(f[0], f[-1]): continue
        if sum(abs(f[k+1]-f[k]) for k in range(n-1)) != total: continue
        c += 1
    return c

# V1: X={1..7}, f(1)f(7)=7, sum=6  -> 단조만 가능
v1 = scan(7, lambda a,b: a*b == 7, 6)
print("V1 =", v1, " 손계산 2 x 7H5 =", 2*comb(11,5))

# V2: X={1..5}, f(1)f(5)=4, sum=3  -> (2,2)는 홀짝 때문에 불가능
v2 = scan(5, lambda a,b: a*b == 4, 3)
print("V2 =", v2, " 손계산 2 x 4H3 =", 2*comb(6,3))
for (a,b) in [(1,4),(4,1),(2,2)]:
    print("   (%d,%d) ->"%(a,b), scan(5, lambda x,y,a=a,b=b:(x,y)==(a,b), 3))

# V3: X={1..5}, f(1)=2, f(5)=5. sum의 최솟값 m과 그때의 개수 N
best = None; cnt = {}
for f in product(range(1,6), repeat=5):
    if f[0]!=2 or f[4]!=5: continue
    s = sum(abs(f[k+1]-f[k]) for k in range(4))
    cnt[s] = cnt.get(s,0)+1
    if best is None or s < best: best = s
print("V3: 최솟값 m =", best, " 그때 개수 N =", cnt[best], " m+N =", best+cnt[best],
      " 손계산 4H3 =", comb(6,3))
print("   sum별 분포(작은 것부터):", sorted(cnt.items())[:4])
