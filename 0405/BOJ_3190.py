from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
seconds = [0] * L   # 시간 배열
turns = [''] * L    # 방향 배열

# 시간과 방향을 각각 배열에 할당
for i in range(L):
    x, c = input().split()
    seconds[i] = int(x)
    turns[i] = c

# time: 총 게임 시간, idx: 방향 전환할 때 사용할 seconds, turns의 인덱스값
# [x, y]: 현재 뱀 머리의 좌표, d: 방향 인덱스, q: 몸 좌표들 넣어줄 queue
time = idx = x = y = 0
d = 1   # 오른쪽 방향으로 시작하기 때문에 1로 초기화
q = deque()
q.append([0, 0])

while True:
    # 방향 전환, 'L' : +3(-1인데 %4 사용하기 위해 +3으로 계산), 'D' : +1
    if idx < L and time == seconds[idx]:
        if turns[idx] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        idx += 1

    # 한칸 이동, 시간 +1
    x, y = x + di[d], y + dj[d]
    time += 1
    
    # 벽이나 몸과 만나면 break
    if x < 0 or x >= N or y < 0 or y >= N or [x, y] in q:
        break

    # q에 넣어주기
    q.append([x, y])

    # 사과 먹으면 사과 없애고 안 먹으면 꼬리 자르기
    for i in range(len(apples)):
        # 사과 좌표가 (1, 1)로 시작이라서 비교할 때 1 더해서 비교해줌
        if [x + 1, y + 1] == apples[i]:
            apples.pop(i)
            break
    else:
        px, py = q.popleft()

print(time)

