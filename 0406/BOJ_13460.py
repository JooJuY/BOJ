from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def move(x, y, dx, dy):         # 벽이나 구멍을 만날 때까지 좌표 이동
    c = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c


def BFS():
    global min_val
    q = deque()
    q.append((RX, RY, BX, BY, 0))
    visited[RX][RY][BX][BY] = 1
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= min_val:
            continue
        for k in range(4):
            nrx, nry, rc = move(rx, ry, di[k], dj[k])
            nbx, nby, bc = move(bx, by, di[k], dj[k])
            if arr[nbx][nby] == 'O':        # 파란 구슬이 구멍이 들어가면 이전으로 돌아가서 다른방향으로 돌리기
                continue
            if arr[nrx][nry] == 'O':        # 빨간 구슬이 구명에 들어가면 끝내기
                if min_val > cnt + 1:
                    min_val = cnt + 1
                break
            if nrx == nbx and nry == nby:       # 구슬이 겹치면 더 많이 움직인 구슬을 하나 이전 칸으로 이동
                if rc > bc:
                    nrx, nry = nrx - di[k], nry - dj[k]
                else:
                    nbx, nby = nbx - di[k], nby - dj[k]
            if not visited[nrx][nry][nbx][nby]:     # 이동한 좌표가 안 간 좌표면 가기
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited[nrx][nry][nbx][nby] = 1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
RX = RY = BX = BY = 0
min_val = 11
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            RX, RY = i, j
        elif arr[i][j] == 'B':
            BX, BY = i, j

BFS()
print(min_val if min_val != 11 else -1)