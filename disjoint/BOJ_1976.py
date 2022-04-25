import sys

def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]


def union(a, b):
    # 각 루트 노드 찾기
    a = find(a)
    b = find(b)

    # 루트가 같으면 동일 집합, 아니면 작은 수를 부모 노드로 사용해서 집합 합치기
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
want = list(map(int, sys.stdin.readline().split()))
parent = [x for x in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            union(i, j)
flag = 0
root = -1
for x in want:
    f = find(x-1)
    if root != -1 and root != f:
        flag = 1
        break
    root = f

print('NO' if flag else 'YES')
