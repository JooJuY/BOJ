# 최대차이를 이분탐색으로 구하기
import sys

N, M, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
start = 1
end = L-2
answer = L-1
while start <= end:
    mid = (start + end) // 2
    current = 0
    cnt = 0
    for i in range(N):
        while arr[i] > current + mid:
            current += mid
            cnt += 1
        current = arr[i]

    while current + mid < L:
        current += mid
        cnt += 1
    # 개수가 적으면 거리가 너무 넓은 것이기 때문에 end를 조정, 최대 거리를 위해 요기에서 answer 업데이트
    if cnt <= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)