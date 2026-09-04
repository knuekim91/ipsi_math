# -*- coding: utf-8 -*-
from itertools import product

def scan(n, f1, fn, total):
    out=[]
    for f in product(range(1,n+1), repeat=n):
        if f[0]!=f1 or f[-1]!=fn: continue
        if sum(abs(f[k+1]-f[k]) for k in range(n-1))!=total: continue
        out.append(f)
    return out

cands = [
 ("A  X={1..4} f1=1 f4=2 합=5", 4,1,2,5),
 ("B  X={1..4} f1=4 f4=1 합=5", 4,4,1,5),
 ("C  X={1..5} f1=1 f5=4 합=5", 5,1,4,5),
 ("D  X={1..4} f1=2 f4=2 합=4", 4,2,2,4),
 ("E  X={1..5} f1=2 f5=4 합=4", 5,2,4,4),
 ("F  X={1..4} f1=3 f4=2 합=5", 4,3,2,5),
]
for label,n,a,b,t in cands:
    g = scan(n,a,b,t)
    net = abs(b-a); back = (t-net)/2
    print(f"{label}  순변위 {net}, 되돌아간 거리 {back}, 개수 {len(g)}")
    if len(g) <= 14: print("      ", g)
