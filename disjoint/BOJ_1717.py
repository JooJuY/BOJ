import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
parent = [x for x in range(N + 1)]  # 부모리스트 생성. 각 자기 번호로 초기화


# 루트 노드 찾는 함수
def find(a):
    # 루트 노드일 때
    if a == parent[a]:
        return a
    p = find(parent[a])  # a의 루트 노드 찾기
    parent[a] = p  # 부모 리스트 갱신
    return parent[a]  # a의 루트 노드 반환


# a가 있는 집합과 b가 있는 집합을 합치는 연산 함수
def union(a, b):
    # 각 루트 노드 찾기
    a = find(a)
    b = find(b)

    # 루트가 같으면 동일 집합, 아니면 작은 수를 부모 노드로 사용해서 집합 합치기
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    q, a, b = map(int, sys.stdin.readline().split())
    if q:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)