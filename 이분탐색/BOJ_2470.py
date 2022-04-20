# 두 용액을 left, right로 정해서 더해보며 탐색
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = []
answer = 2e+9
left = 0
right = N-1
while left < right:
    total = arr[left] + arr[right]

    if abs(total) < answer:
        answer = abs(total)
        result = [arr[left], arr[right]]

    if total < 0:
        left += 1
    else:
        right -= 1

print(*result)