import sys
sys.setrecursionlimit(10**4)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    elif arr[a] > arr[b]:   # 값이 작은 것을 root도 삼기
        parent[a] = b
    else:
        parent[b] = a


N, M, k = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
parent = [x for x in range(N+1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    union(v, w)
ans = 0
for i, root in enumerate(parent):
    if i == root:
        ans += arr[i]

if ans <= k:
    print(ans)
else:
    print('Oh no')