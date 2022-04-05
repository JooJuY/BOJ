def DFS(n, val):
    global max_val
    if n >= N:
        if max_val < val:
            max_val = val
        return
    # 포함
    if n + arr[n][0] <= N:
        DFS(n + arr[n][0], val + arr[n][1])
    # 미포함
    DFS(n+1, val)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
DFS(0, 0)
print(max_val)