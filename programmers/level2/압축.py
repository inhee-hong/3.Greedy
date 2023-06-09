def solution(msg):
    answer = []
    
    index = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
            'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
            'X':24, 'Y':25, 'Z':26}
    
    now_index = 27

    num = 0
    flag = True
    while True:
        if not flag:
            break
        now_text = msg[num]
        idx = 1
        while True:
            try:
                next_text = msg[num + idx]
                # index에 다음 글자를 합한 것이 존재하는지 확인
                total_text = now_text + next_text
                check = index[total_text] # try구문 실행될 부분
                now_text = total_text
                num += 1
            except:
                if num == len(msg)-1:
                    answer.append(index[now_text])
                    flag = False
                    break
                # index에 다음 글자를 합한 것이 존재하지 않는다면, index에 추가해주기
                index[total_text] = now_index
                now_index += 1
                # 현재 입력을 answer에 넣기
                answer.append(index[now_text])
                num += 1
                break
    
    return answer
