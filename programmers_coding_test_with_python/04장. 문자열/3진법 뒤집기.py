# https://school.programmers.co.kr/learn/courses/30/lessons/68935

# divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플로 return해줌
# int(a, b) : b진수로 표현된 문자열 a를 10진수로 바꿔줌

def solution(n):
    answer = ''
    
    while n > 0:
        n, b = divmod(n, 3)
        answer += str(b)
        
    return int(answer, 3)