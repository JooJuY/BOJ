'''
2
1 2 -1
2 -1 -1
--> 2
'''

import sys
sys.setrecursionlimit(10**6)

def likeinorder(x):
    global cnt
    if left[x] != -1:
        likeinorder(left[x])
        cnt += 1
    # 마지막 노드에 도착하면 출력하고 종료
    if x == last:
        print(cnt)
        exit()
    cnt += 1

    if right[x] != -1:
        likeinorder(right[x])
        cnt += 1

# 중위 순회 마지막 노드 구하기 위해
def inorder(x):
    global last
    if left[x] != -1:
        inorder(left[x])
    last = x
    if right[x] != -1:
        inorder(right[x])


N = int(sys.stdin.readline())
left = [0] * (N+1)
right = [0] * (N+1)
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    left[a] = b
    right[a] = c
cnt = 0
last = 0
inorder(1)
likeinorder(1)



