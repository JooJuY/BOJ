H, W = map(int, input().split())
blocks = list(map(int, input().split()))
rain = 0
# 가장 앞에 있는 벽과 가장 뒤에 있는 벽 차이 - 그 사이 벽 개수
maxx = max(blocks)
for h in range(maxx, -1, -1):
    here = []

    for w in range(W):
        if blocks[w] >= h:
            here.append(w)

    if here and here[0] != here[-1]:
        rain += (here[-1]-here[0]-1 -(len(here)-2))
print(rain)

