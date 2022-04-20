# 걸리는 시간을 mid로 정해 이분탐색

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
left = arr[0]
right = arr[-1] * M
answer = right
while left <= right:
    mid = (left + right) // 2
    total = 0

    for i in range(N):
        total += mid // arr[i]

    if total >= M:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)