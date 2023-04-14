# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    
    # 오름차순으로 정렬
    participant.sort()
    completion.sort()
    
    # 하나씩 비교해가면서 찾기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
            
    # 완주하지 못한 참가자 이름이 맨 뒤에 존재할 떄
    if answer == "":
        answer = participant[-1]
    
    return answer

################# hash를 이용한 다른 풀이 ################
from collections import Counter

def solution(participant, completion):
    ans = {}
    for name in participant:
        ans[name] = ans.get(name, 0) + 1 

    for people in completion:
        ans[people] -= 1
    
    answer = Counter(ans).most_common()
        
    return answer[0][0]