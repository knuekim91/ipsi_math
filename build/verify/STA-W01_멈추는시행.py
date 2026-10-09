# -*- coding: utf-8 -*-
"""최종 4종 + 원본. 풀이에 쓸 중간 수치까지 전부 뽑는다."""
from fractions import Fraction as F
from collections import defaultdict

def detail(cards, stop, name):
    n=len(cards); P=defaultdict(F)
    for c in cards: P[c]+=F(1,n)
    P=dict(sorted(P.items()))
    print("=== %s ===" % name)
    print("  카드 %s  →  %s" % (cards, "  ".join("P(%d)=%s"%(v,p) for v,p in P.items())))
    out=defaultdict(F); cur={0:F(1)}; k=0
    while cur and k<14:
        k+=1; nxt=defaultdict(F); line=[]
        for s,q in sorted(cur.items()):
            for v,pv in sorted(P.items()):
                t=s+v
                if t>=stop:
                    out[k]+=q*pv; line.append("합%d+%d=%d 멈춤 %s"%(s,v,t,q*pv))
                else: nxt[t]+=q*pv
        if line: print("   %d번째 멈춤: %s" % (k, " / ".join(line)))
        if nxt: print("      -> 계속되는 상태 %s" % {a:str(b) for a,b in sorted(nxt.items())})
        cur=nxt
    E=sum(k*v for k,v in out.items())
    print("  분포 %s" % "  ".join("P(X=%d)=%s"%(k,out[k]) for k in sorted(out)))
    print("  합 %s   E(X) = %s" % (sum(out.values()), E))
    print("  → E(%dX) = %s" % (E.denominator, E*E.denominator))
    print()
    return out, E

detail([1,1,1,2,2,3], 4, "원본 PRB? (설맞이 57)")
detail([1,1,2,2,3,3], 4, "V1  각 2장씩")
detail([1,1,1,1,2,3], 4, "V2  1이 4장")
detail([1,1,1,2,2,3], 5, "V3  멈춤 기준 5")
