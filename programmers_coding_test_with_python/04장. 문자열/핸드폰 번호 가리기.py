# https://school.programmers.co.kr/learn/courses/30/lessons/12948

################# success ########################################
def solution(phone_number):
    answer = ''
    answer += (len(phone_number) - 4) * '*'
    phone_number = phone_number[(len(phone_number) - 4):]
    answer += phone_number
    return answer

############### 정규 표현식을 이용한 풀이 ##########################
import re

def solution(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)
##################################################################