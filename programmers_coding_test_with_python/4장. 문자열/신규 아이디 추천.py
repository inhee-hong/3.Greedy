# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''
       
    for text in new_id:
        # 6단계
        if len(answer) == 15:
            break
            
        # 4단계-1
        if len(answer) == 0 and text == '.':
            continue
            
        # 1단계
        if text.isupper():
            answer += text.lower()
            continue
        elif text.isalnum():
            answer += text
        
        # 2단계
        if not text.isalnum():
            txt = re.sub(r'[^-_.]', '', text)
            if len(txt) == 0:
                continue
            # 3단계
            elif txt == '.' and answer[-1] == '.':
                continue
            else:
                answer += txt

    # 4단계-2
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
        
    # 5단계
    if len(answer) == 0:
        answer = 'aaa'
        
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer