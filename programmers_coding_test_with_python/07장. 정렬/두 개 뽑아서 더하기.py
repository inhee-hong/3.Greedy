# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    answer = set()
    
    lst = list(combinations(numbers, 2))
    for n in lst:
        answer.add(sum(n))
    
    return sorted(list(answer))

##################### 한 줄 코드 ##########################
from itertools import combinations

def solutions(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))