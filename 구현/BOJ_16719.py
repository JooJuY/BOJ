def making():
    make_word = ''
    for idx in range(N):
        if selidx[idx]:
            make_word += word[idx]
    return make_word


word = input()
N = len(word)
min_word = ''
selidx = [0] * N
while len(min_word) < N:
    plus = None
    min_word = 'Z' + min_word
    for i in range(N):
        if not selidx[i]:
            selidx[i] = 1
            maded = making()
            if min_word >= maded:
                min_word = maded
                if plus:
                    selidx[plus] = 0
                plus = i
            selidx[i] = 0
    selidx[plus] = 1
    print(min_word)

