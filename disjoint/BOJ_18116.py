# pypy로 제출해야한다..
import sys
sys.setrecursionlimit(10**6)

# root 찾는 함수
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    else:
        parent[a] = b
        cnt[b] += cnt[a]    # 부품수를 저장하기 위해 자식 부품 수를 부모 부품수에 더하고 자식 부품수 0으로 만들어 주기
        cnt[a] = 0


N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
parent = [x for x in range(10**6+1)]
cnt = [1] * (10**6+1)   # 각 부품수를 넣어놓을 리스트 초기화
for sent in arr:
    if sent[0] == 'I':
        a, b = int(sent[1]), int(sent[2])
        union(a, b)
    else:
        root = find(int(sent[1]))
        print(cnt[root])