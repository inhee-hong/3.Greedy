# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = [0, 0, 0]
    
    # 동일한 규칙에 따라 수포자들이 문제를 찍는다.
    first = [1, 2, 3, 4, 5] * (int(len(answers)/5) + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * (int(len(answers)/8) + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(len(answers)/10) + 1)
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            answer[0] += 1
        if answers[i] == second[i]:
            answer[1] += 1
        if answers[i] == third[i]:
            answer[2] += 1
                
    ans = []
    for idx, student in enumerate(answer):
        if student == max(answer):
            ans.append(idx+1)
    
    return ans