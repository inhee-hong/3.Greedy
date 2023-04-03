# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt = 0
    sum_ = 0
    # s가 1이 될 때까지 반복문 실행
    while s != '1':
        # 조건 1 : x의 모든 0을 제거합니다.
        new_s = ''
        for i in range(len(s)):
            if s[i] == '0':
                sum_ += 1
            else:
                new_s += '1'
        
        # 조건 2 : x의 길이를 c라고 하고, c를 2진법으로 표현한 문자열로 바꿉니다.
        len_s = len(new_s)
        s = bin(len_s)[2:]
        cnt += 1

    return [cnt, sum_]