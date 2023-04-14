# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

def solution(record):
    answer = []
    tmp = []
    names = defaultdict(str)
    
    # 순서대로 입력 받고, dictionary에 (유저 아이디) : (유저 닉네임) 으로 값을 받아주기
    for text in record:
        token = text.split()
        if token[0] == 'Enter':
            tmp.append((token[1],  '님이 들어왔습니다.'))
            names[token[1]] = token[2]
        elif token[0] == 'Leave':
            tmp.append((token[1], '님이 나갔습니다.'))
        else:
            names[token[1]] = token[2]
    
    # 최종 값들로 result 출력하기
    for text in tmp:
        answer.append(names[text[0]] + text[1])
            
    return answer