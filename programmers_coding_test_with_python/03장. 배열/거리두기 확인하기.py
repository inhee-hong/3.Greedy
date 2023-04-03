# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = [1] * 5
    for i in range(5):
        for j in range(5):
            if answer[i] == 0:
                break
            for k in range(5):
                if places[i][j][k] == 'P':
                    if j + 1 <= 4 and places[i][j + 1][k] == 'P':
                        answer[i] = 0
                        break
                    elif k + 1 <= 4 and places[i][j][k + 1] == 'P':
                        answer[i] = 0
                        break
                    
    return answer