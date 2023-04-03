# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    # 결과로 나올 행렬 만들어주기
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    # 행렬 곱 해주기
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum_ = 0
            for k in range(len(arr1[0])):
                sum_ += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum_
            
    return answer