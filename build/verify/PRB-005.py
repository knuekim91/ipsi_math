# -*- coding: utf-8 -*-
from itertools import product
from fractions import Fraction as F
from collections import Counter

S0 = ('A','A','A','B','B','B')

def step(s, k):
    s = list(s)
    if k <= 5:
        s[k-1], s[k] = s[k], s[k-1]
    return tuple(s)

# ---------- 방법 1: 완전탐색 ----------
tot = num = 0
for seq in product(range(1,7), repeat=4):
    s = S0
    for k in seq: s = step(s, k)
    if s == S0:
        tot += 1
        if seq[2] == 6: num += 1
print("[방법1 완전탐색] 분모 =", tot, " 분자 =", num, " 확률 =", F(num, tot))

# ---------- 방법 2: 상태전이 행렬 ----------
states = {}
def idx(s):
    if s not in states: states[s] = len(states)
    return states[s]
idx(S0)
frontier=[S0]; edges={}
while frontier:                      # 도달 가능한 상태 전개
    cur=frontier.pop()
    if cur in edges: continue
    e=Counter()
    for k in range(1,7): 
        t=step(cur,k); e[t]+=1
        if t not in edges and t not in frontier: frontier.append(t)
    edges[cur]=e
vec = {S0:1}
for r in range(4):
    nxt=Counter()
    for s,c in vec.items():
        for t,w in edges[s].items(): nxt[t]+=c*w
    vec=nxt
print("[방법2 전이행렬] 4회 후 S0 =", vec[S0], " (전체", sum(vec.values()), "= 6^4)")

# ---------- 방법 3: '효과적인 시행' 개수로 분류 ----------
# 상태를 바꾸는 시행만 셈. S0에서는 5개가 제자리, S1에서는 3개가 제자리.
tot_by_eff = Counter(); num_by_eff = Counter()
for seq in product(range(1,7), repeat=4):
    s = S0; eff = 0
    for k in seq:
        t = step(s,k)
        if t != s: eff += 1
        s = t
    if s == S0:
        tot_by_eff[eff] += 1
        if seq[2] == 6: num_by_eff[eff] += 1
print("[방법3 효과적 시행 수별]")
for e in sorted(tot_by_eff):
    print(f"   효과적 {e}회 : 분모 {tot_by_eff[e]:4d}   그중 3번째=6 인 것 {num_by_eff[e]}")
print("   합계:", sum(tot_by_eff.values()), "/", sum(num_by_eff.values()))

# 손으로 센 값과 대조
hand_den = {0: 5**4, 2: 25+15+9+25+15+25, 4: 3}
hand_num = {0: 5**3, 2: 5+3+5, 4: 0}
print("   손계산 분모", hand_den, "합", sum(hand_den.values()))
print("   손계산 분자", hand_num, "합", sum(hand_num.values()))
print("   일치:", dict(tot_by_eff)==hand_den and dict(num_by_eff)=={k:v for k,v in hand_num.items() if True})

# ---------- 선택지 대조 ----------
opts = {'①':F(71,373),'②':F(69,373),'③':F(73,371),'④':F(71,371),'⑤':F(69,371)}
ans = F(num,tot)
print("\n확률 =", ans, "=", [k for k,v in opts.items() if v==ans])
