# -*- coding: utf-8 -*-
from itertools import product
from math import comb

def scan(n, f1, fn, total, listing=False):
    got=[]
    for f in product(range(1,n+1), repeat=n):
        if f[0]!=f1 or f[-1]!=fn: continue
        if sum(abs(f[k+1]-f[k]) for k in range(n-1))!=total: continue
        got.append(f)
    return got

print("=== S2: X={1,2,3,4}, f(1)=1, f(4)=4, 합=3 (증가 방향) ===")
g = scan(4,1,4,3); print("  개수 =", len(g), " 손계산 4H2 =", comb(5,2))
print("  전부:", g)

print("\n=== S3: X={1,2,3,4}, f(1)=4, f(4)=1, 합=3 (감소 방향, 형광펜 지점) ===")
g = scan(4,4,1,3); print("  개수 =", len(g), " 손계산 4H2 =", comb(5,2))
print("  전부:", g)

print("\n=== S4: X={1,2,3,4}, f(1)=1, f(4)=4, 합=5 (등호가 깨질 때) ===")
g = scan(4,1,4,5); print("  개수 =", len(g))
print("  전부:", g)
print("  (되돌아간 거리 = (5-3)/2 = 1 이어야 함 -> 정확히 한 번 1만큼 후퇴)")

print("\n=== 홀짝 확인: f(1)=1, f(4)=4 에서 가능한 합의 값 ===")
from collections import Counter
c=Counter()
for f in product(range(1,5),repeat=4):
    if f[0]!=1 or f[3]!=4: continue
    c[sum(abs(f[k+1]-f[k]) for k in range(3))]+=1
print(" ", sorted(c.items()), "  -> 모두 홀수 (순변위 3과 같은 홀짝)")
