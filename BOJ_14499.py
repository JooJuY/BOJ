# 1: 동, 2: 서, 3: 북, 4: 남
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
# 방향에 따라 각 면의 값을 이동
def circles(dire):
    if dire == 1:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif dire == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif dire == 3:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    else:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]


N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direct = list(map(int, input().split()))
dice = [0] * 7  # 주사위

for d in direct:
    # 이동한 칸의 좌표
    tmpx, tmpy = x + di[d], y + dj[d]
    # 바깥으로 나가는 경우
    if tmpx < 0 or tmpx >= N or tmpy < 0 or tmpy >= M:
        continue
    x, y = tmpx, tmpy
    # 주사위 돌리기
    circles(d)
    # 칸에 수가 있는 경우, 칸의 수 -> 주사위의 바닥면으로 복사, 칸은 0
    if arr[x][y]:
        dice[6] = arr[x][y]
        arr[x][y] = 0
    # 칸에 수가 0인 경우, 주사위 바닥면 -> 칸으로 복사
    else:
        arr[x][y] = dice[6]
    # 윗면 출력
    print(dice[1])
