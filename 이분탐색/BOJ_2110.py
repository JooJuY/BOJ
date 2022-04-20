# 길이를 mid로 정해 이분탐색으로 구하기, input으로 쓰면 시간초과
import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

wifi = 0
left = 1
right = houses[-1] - houses[0]
while left <= right:
    mid = (right + left) // 2
    current = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= current + mid:
            cnt += 1
            current = houses[i]

    if cnt >= C:
        left = mid + 1
        wifi = mid
    else:
        right = mid - 1

print(wifi)