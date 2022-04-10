def slide(a, visited):
    global cnt
    for i in range(N):
        flag = 0
        j = 0
        while j < N - 1:
            # 높이가 같을때
            if a[i][j + 1] - a[i][j] == 0:
                j += 1
            # 앞 칸이 1 작을 때
            elif a[i][j + 1] - a[i][j] == -1:
                tmp = a[i][j + 1]  # 낮은 높이 저장
                # L길이의 경사로를 놓을 수 있고 경사로 안 썼던 곳이고 L길이동안 높이가 똑같으면,
                if j + L < N and 1 not in visited[i][j + 1:j + L + 1]:
                    for k in range(j + 1, j + L + 1):
                        if tmp != a[i][k]:
                            flag = 1
                            break
                    else:
                        visited[i][j + 1:j + L + 1] = [1] * L
                        j += L  # j를 경사로 끝 인덱스로 보내기
                else:
                    flag = 1
            # 앞칸이 1 클 때
            elif a[i][j + 1] - a[i][j] == 1:
                tmp = a[i][j]  # 낮은 높이 저장
                # L길이의 경사로를 놓을 수 있고 경사로 안 썼던 곳이고 L길이동안 높이가 똑같으면,
                if j + 1 - L >= 0 and 1 not in visited[i][j + 1 - L:j + 1]:
                    for k in range(j + 1 - L, j + 1):
                        if tmp != a[i][k]:
                            flag = 1
                            break
                    else:
                        visited[i][j + 1 - L:j + 1] = [1] * L
                        j += 1  # j를 경사로 끝 인덱스로 보내기
                else:
                    flag = 1
            else:
                break
            if flag:
                break
        else:
            cnt += 1


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# 가로
slide(arr, [[0]*N for _ in range(N)])
# 세로
slide(list(map(list, zip(*arr))), [[0]*N for _ in range(N)])

print(cnt)