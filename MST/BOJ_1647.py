# 크루스칼 알고리즘
# 지역 나누는 거라 유니온파운드가 생각났고
# 유니온파운드를 사용하는 크루스칼을 사용해야겠다는 생각이 들었음

import sys

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
arr.sort(key=lambda x: x[2])

selected = []   # 선택한 간선
parent = [x for x in range(N+1)]
answer = 0
for s, e, w in arr:
    if find(s) != find(e):
        union(s, e)
        answer += w
        selected.append(w)
# 두 마을로 나누기 때문에 가장 마지막에 선택한 간선만큼 빼주기
print(answer-selected[-1])