# prim 사용
# 참고 https://hillier.tistory.com/54
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append([c, b])
    arr[b].append([c, a])

heap = [[0, 1]]
answer = cnt = 0
visited = [0] * (V+1)
while heap:
    if cnt == V:
        break
    # heapq.heappop으로 뽑으면 최솟값을 뽑음
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        cnt += 1
        answer += w
        for i in arr[s]:
            # heapq.heappush로 넣으면 항상 최소 힙을 만듦
            heapq.heappush(heap, i)

print(answer)