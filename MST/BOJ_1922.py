import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append([c, b])
    arr[b].append([c, a])

visited = [0] * (N+1)
heap = [[0, 1]]
cnt = answer = 0

while heap:
    if cnt == N:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        cnt += 1
        answer += w
        for i in arr[s]:
            heapq.heappush(heap, i)

print(answer)