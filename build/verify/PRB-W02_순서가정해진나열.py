# -*- coding: utf-8 -*-
"""2016학년도 9월 B형 15번과 유사문항 검증. 공은 구별되는 것으로 보고 전수조사한다."""
from fractions import Fraction as F
from itertools import permutations, combinations

def enum(labels, take, ok):
    """labels 에서 take 개를 꺼내 일렬로 나열하는 모든 경우를 센다.
       공은 서로 구별되므로 자리(index)로 다룬다."""
    n = len(labels)
    tot = fav = 0
    for pick in combinations(range(n), take):
        for order in permutations(pick):
            tot += 1
            if ok([labels[i] for i in order]):
                fav += 1
    return F(fav, tot), fav, tot

nondec = lambda s: all(s[i] <= s[i+1] for i in range(len(s)-1))
inc    = lambda s: all(s[i] <  s[i+1] for i in range(len(s)-1))

rows = []
rows.append(("원본  1,1,2,3,4 에서 4개, a<=b<=c<=d",
             enum([1,1,2,3,4], 4, nondec), F(1,15)))
rows.append(("V1    1,1,2,2,3 에서 4개, a<=b<=c<=d",
             enum([1,1,2,2,3], 4, nondec), F(1,10)))
rows.append(("V2    1,1,1,2,3 에서 4개, a<=b<=c<=d",
             enum([1,1,1,2,3], 4, nondec), F(3,20)))
rows.append(("V3    1,1,2,3,4 에서 4개, a<b<c<d",
             enum([1,1,2,3,4], 4, inc), F(1,60)))

for name, (p, fav, tot), want in rows:
    print("%-38s %-7s (%d/%d)  기대 %-6s %s"
          % (name, p, fav, tot, want, "일치" if p == want else "★불일치★"))

# V4 조건부확률: a<=b<=c<=d 일 때 네 수가 모두 다를 확률
L = [1,1,2,3,4]
A = B = 0
for pick in combinations(range(5), 4):
    for order in permutations(pick):
        s = [L[i] for i in order]
        if nondec(s):
            A += 1
            if len(set(s)) == 4:
                B += 1
print()
print("V4    조건부확률 = %d/%d = %s  기대 1/4  %s"
      % (B, A, F(B, A), "일치" if F(B, A) == F(1, 4) else "★불일치★"))
