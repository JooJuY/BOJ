N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for students in arr:
    students -= B
    cnt += 1
    if students <= 0:
        continue
    if students % C:
        cnt += (students // C) + 1
    else:
        cnt += (students // C)
print(cnt)
