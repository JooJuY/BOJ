di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
where = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * 101 for _ in range(101)]
# [x, y, d, g(세대)]
for line in arr:
    y, x, d, g = line
    stack = [[x, y]]
    x, y = x + di[d], y + dj[d]
    stack.append([x, y])
    g -= 1
    while g >= 0:
        L = len(stack)
        for i in range(L-1, 0, -1):
            for k in range(8):
                if [stack[i-1][0] - stack[i][0], stack[i-1][1] - stack[i][1]] == where[k]:
                    ni, nj = stack[-1][0] + where[(k+2)%8][0], stack[-1][1] + where[(k+2)%8][1]
                    stack.append([ni, nj])
                    break
        g -= 1
    for nx, ny in stack:
        visited[nx][ny] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and visited[i+1][j+1] and visited[i+1][j]:
            cnt += 1
print(cnt)