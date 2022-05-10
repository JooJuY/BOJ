import sys

N, M = map(int, sys.stdin.readline().split())
# 각 폴더 하위 파일/ 폴더 저장할 딕셔너리 사용
folders = {}
for _ in range(N+M):
    p, f, c = sys.stdin.readline().split()
    if p not in folders:
        folders[p] = []
    folders[p].append([f, int(c)])

print(folders)
Q = int(sys.stdin.readline())
for _ in range(Q):
    ques = list(sys.stdin.readline().strip().split('/'))
    # 종류라서 set 사용
    file = set()
    ficnt = 0
    q = [ques[-1]]
    while q:
        now = q.pop()
        if now not in folders:
            continue
        for title, val in folders[now]:
            # val == 1이면 폴더라서 q에 넣음
            # 아니면 파일이라서 file에 add하고 ficnt + 1 해줌
            if val:
                q.append(title)
            else:
                ficnt += 1
                file.add(title)
    print(len(file), ficnt)

