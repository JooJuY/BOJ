from itertools import combinations

def oddcnt(x):
    odd = 0
    for i in x:
        if int(i) % 2:
            odd += 1
    return odd

def cal(x, cnt):
    global max_cnt, min_cnt
    odd = oddcnt(x)
    length = len(x)
    if length == 1:
        if max_cnt < cnt+odd:
            max_cnt = cnt+odd
        if min_cnt > cnt+odd:
            min_cnt = cnt+odd
        return

    if length >= 3:
        slicing = list(combinations(range(1, length), 2))
        for s in slicing:
            a = x[:s[0]]
            b = x[s[0]:s[1]]
            c = x[s[1]:]
            cal(str(int(a) + int(b) + int(c)), cnt + odd)
    else:
        x = str((int(x)//10) + (int(x) % 10))
        cal(x, cnt+odd)


N = input()
max_cnt = 0
min_cnt = 10 ** 9
cal(N, 0)
print(min_cnt, max_cnt)