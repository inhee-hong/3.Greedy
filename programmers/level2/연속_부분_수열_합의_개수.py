from collections import deque

def solution(elements):
    answer = []
    
    # 원형 수열처럼 보이게 만들기
    new_elements = elements * 2
    
    # 1개씩, 모든 개수 
    answer += elements
    answer.append(sum(elements))
    
    tmp = deque()
    for i in range(2, len(elements)):
        for j in range(len(new_elements)):
            if j == 0:
                tmp.append(new_elements[0])
            else:
                tmp.append(new_elements[j])
                if len(tmp) == i:
                    answer.append(sum(tmp))
                    tmp.popleft()
    
    return len(set(answer))