from collections import deque
html = input()
html = html[6:-7]
html = html.replace('<div ', '!')   # div 태그 !로 바꾸기
html = html.replace('</div>', '')   # 닫는 태그는 없애기
html = html.replace('=', ' : ')     # div안 title에만 있는 '='를 ' : '로 바꾸기
html = html.replace('"', '')        # title에만 있는 "" 없애기
html = html.replace('<p>', '@')     # p태그 @로 바꾸기
html = html.replace('</p>', '')     # p 닫는 태그는 없애기

q = deque(html)
lst = []

# div, p 태그를 제외한 나머지 태그 풀기
while q:
    now = q.popleft()
    # 괄호 열리면 닫힐 때까지 안에 내용 빼기
    if now == '<':
        tmp = q.popleft()
        while tmp != '>':
            tmp = q.popleft()
    else:
        lst.append(now)

# 태그 뺀 리스트 문자열로 변경
ans = ''.join(lst)
ans = ans.replace('>', '')      # div에서 남은 '>' 없애기
ans = ' '.join(ans.split())     # 두번 이상 공백을 하나로 만들기 위해서 단어별로 나눠 join 해줌

ans = ans.replace('!', '\n')    # div 태그 자리에 줄 바꾸기
ans = ans.replace('@', '\n')    # p 태그 자리에 줄 바꾸기

answer = list(ans.strip().split('\n'))      # 줄바꿈을 기준으로 문장 나눠서 리스트로 만듦

for sent in answer:
    print(sent)