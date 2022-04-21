# 최대값을 이분탐색으로 정해 그 무게를 이동시킬 수 있는지 BFS로 확인
import sys

def BFS(s, e, weight):
    q = [s]
    visited = [0] * (N+1)
    visited[s] = 1
    while q:
        now = q.pop(0)
        if now == e:
            return 1
        for x, w in arr[now]:
            if not visited[x] and w >= weight:
                visited[x] = 1
                q.append(x)
    return 0


N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

fact1, fact2 = map(int, sys.stdin.readline().split())
start = 1
end = 1_000_000_000
answer = 0
while start <= end:
    mid = (start + end) // 2
    boo = BFS(fact1, fact2, mid)

    if boo:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
