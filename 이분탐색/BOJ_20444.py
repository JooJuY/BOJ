# 색종이 한 변 자르는 횟수 mid
N, K = map(int, input().split())

left = 0
right = N//2
flag = 0
while left <= right:
    mid = (left + right) // 2
    paper = (mid + 1) * (N - mid + 1)
    if paper == K:
        flag = 1
        break
    elif paper > K:
        right = mid - 1
    else:
        left = mid + 1
print('YES' if flag else 'NO')