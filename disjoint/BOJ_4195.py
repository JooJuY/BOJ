import sys
# sys.setrecursionlimit(10**5)

def find(x):
    if friends[x] == x:
        return x
    friends[x] = find(friends[x])
    return friends[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    else:
        friends[b] = a
        num[a] += num[b]    # 친구 수 더해주기


T = int(sys.stdin.readline())
for t in range(T):
    F = int(sys.stdin.readline())
    # 사람 이름이라서 딕셔너리 사용
    friends = {}
    num = {}
    for _ in range(F):
        n1, n2 = sys.stdin.readline().split()
        # 없으면 자기 이름으로 초기화해주고 num에도 1로 만들어주기
        if n1 not in friends:
            friends[n1] = n1
            num[n1] = 1
        if n2 not in friends:
            friends[n2] = n2
            num[n2] = 1
        union(n1, n2)
        print(num[find(n1)])