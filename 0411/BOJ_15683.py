dirt = [[-1, 0], [0, 1], [1, 0], [0, -1]]
case = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]]
        ]
def see(idx, cnt):
    global max_cnt
    # 종료
    if idx == L:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    for didxs in case[cctvs[idx][2]]:
        tmp = []
        t = 0
        for didx in didxs:
            ni, nj = cctvs[idx][0] + dirt[didx][0], cctvs[idx][1] + dirt[didx][1]
            while 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 6:
                if not arr[ni][nj]:
                    arr[ni][nj] = '#'
                    tmp.append([ni, nj])
                    t += 1
                ni, nj = ni + dirt[didx][0], nj + dirt[didx][1]
        see(idx+1, cnt+t)
        for x, y in tmp:
            arr[x][y] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
max_cnt = 0
six = 0
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctvs.append([i, j, arr[i][j]])
        if arr[i][j] == 6:
            six += 1
L = len(cctvs)
see(0, 0)
print(N*M - L - six - max_cnt)