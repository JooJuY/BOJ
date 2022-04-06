import sys

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# ㅜ, ㅓ, ㅗ, ㅏ 모양은 DFS로 안돼서 따로 돌려줌
expts = [
    [[0, 0], [0, -1], [0, 1], [1, 0]],   # ㅜ
    [[0, 0], [-1, 0], [0, -1], [1, 0]],  # ㅓ
    [[0, 0], [0, -1], [-1, 0], [0, 1]],  # ㅗ
    [[0, 0], [-1, 0], [1, 0], [0, 1]]    # ㅏ
]

def DFS(x, y, tot):
    global max_tot
    if tot + 999*(4-visited[x][y]) < max_tot:
        return
    if visited[x][y] == 4:
        if max_tot < tot:
            max_tot = tot
        return
    for k in range(4):
        ni, nj = x + di[k], y + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = visited[x][y] + 1
            DFS(ni, nj, tot + arr[ni][nj])
            visited[ni][nj] = 0

def expt(x, y):
    global max_tot
    for e in expts:
        ssum = 0
        for k in range(4):
            ni, nj = x + e[k][0], y + e[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                ssum += arr[ni][nj]
            else:
                break
        else:
            if max_tot < ssum:
                max_tot = ssum


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_tot = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, arr[i][j])
        visited[i][j] = 0
        expt(i, j)
print(max_tot)










# tet = [[[0, 0], [1, 0], [2, 0], [3, 0]],    # 세로4
#        [[0, 0], [0, 1], [0, 2], [0, 3]],    # 가로4
#        [[0, 0], [0, 1], [1, 0], [1, 1]],    # 네모
#        [[0, 0], [1, 0], [2, 0], [2, 1]],    # ㄱ
#        [[0, 0], [0, 1], [0, 2], [1, 0]],
#        [[0, 0], [0, 1], [1, 1], [2, 1]],
#        [[0, 0], [0, 1], [0, 2], [-1, 2]],
#        [[0, 0], [1, 0], [1, 1], [2, 1]],    # ㄹ
#        [[0, 0], [0, 1], [-1, 1], [-1, 2]],
#        [[0, 0], [0, -1], [0, 1], [1, 0]],   # ㅜ
#        [[0, 0], [-1, 0], [0, -1], [1, 0]],  # ㅓ
#        [[0, 0], [0, -1], [-1, 0], [0, 1]],  # ㅗ
#        [[0, 0], [-1, 0], [1, 0], [0, 1]]    # ㅏ
#        ]
# max_sum = 0
# for i in range(N):
#     for j in range(M):
#         for k in range(13):
#             ssum = 0
#             for di, dj in tet[k]:
#                 ni, nj = i + di, j + dj
#                 if ni < 0 or ni >= N or nj < 0 or nj >= M:
#                     break
#                 ssum += arr[ni][nj]
#             else:
#                 if max_sum < ssum:
#                     max_sum = ssum
# print(max_sum)
