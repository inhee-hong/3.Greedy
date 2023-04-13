# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 이차방정식의 해 구하는 방법으로 풀기
#   x + y = (brown - 4) / 2
#   x * y = yellow

def solution(brown, yellow):
    
    h = ((1 - brown / 4)**2 - yellow)**0.5 - (1 - brown / 4)
    w = -((1 - brown / 4)**2 - yellow)**0.5 - (1 - brown / 4)
    
    return [int(h) + 2, int(w) + 2]