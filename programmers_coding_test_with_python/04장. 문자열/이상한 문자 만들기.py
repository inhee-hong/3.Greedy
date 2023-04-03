# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    # 단어는 하나 이상의 공백문자로 구분되어 있기 때문에, split 사용하지 않기!
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0
            answer += ' '
            continue
        
        if cnt % 2 == 0:
            answer += s[i].upper()
            cnt += 1
        else:
            answer += s[i].lower()
            cnt += 1
    
    return answer