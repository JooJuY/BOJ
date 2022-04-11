'''
추가할 수 있는 가로선 다 추가해보는 방법 (브루트포스, 백트래킹)
계속 시간초과나서 검색해보니 pypy3으로만 통과된다고 해서 pypy3으로 했슴미다..
'''

# i번 세로줄의 결과가 i번인지 확인
def check():
    for i in range(N):
        tmp = i     # 마지막에 i와 같은지 비교하기 위해 tmp에 저장
        for j in range(H):
            if ladder[j][tmp]:      # 오른쪽으로 갈 수 있는 경우
                tmp += 1
            elif tmp > 0 and ladder[j][tmp-1]:      # 왼쪽으로 갈 수 있는 경우
                tmp -= 1
        if tmp != i:        # 만약에 다르면 false 반환
            return False
    return True     # 같으면 true 반환


def dfs(x, y, cnt):
    global ans
    # 가지치기(최솟값보다 크면 return)
    if cnt >= ans:
        return
    # i번 세로줄의 결과가 i가 나오는지 확인
    if check():
        ans = min(ans, cnt)
        return
    # cnt가 3 이면 다음엔 4니끼 3보다 큰 값이면 값을 구하지 않기 때문에 return
    if cnt == 3:
        return
    for i in range(x, H):
        k = y if i == x else 0      # 시작한 세로줄과 같은 세로줄이면 가로줄을 y부터 시작, 아니면 0부터 시작
        for j in range(k, N-1):
            if not ladder[i][j]:
                ladder[i][j] = 1
                dfs(i, j+2, cnt + 1)    # 연속된 가로선은 못그리기 때문에 j+2해줌
                ladder[i][j] = 0


# N: 세로선 갯수 M: 현재 사다리 연결부분 갯수 H: 가로선 갯수
N, M, H = map(int, input().split())
ladder = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

ans = 4
dfs(0, 0, 0)
print(ans if ans <= 3 else -1)