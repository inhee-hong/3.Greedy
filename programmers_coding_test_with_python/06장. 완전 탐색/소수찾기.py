# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

# 소수 구하기 알고리즘
def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    # 구할 수 있는 모든 숫자 list에 담기
    num_list = set()
    for i in range(1, len(numbers)+1):
        num = list(permutations(list(numbers), i))
        num_list.update([int(''.join(x)) for x in num])
        
    for j in num_list:
        if prime(j):
            answer += 1

    return answer