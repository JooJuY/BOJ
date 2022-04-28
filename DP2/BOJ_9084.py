import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)
    dp[0] = 1
    for cost in costs:
        for j in range(cost, M+1):
            dp[j] += dp[j-cost]
    print(dp[M])
