# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    # 문자열을 돌면서 확인하기
    for alpha in s:
        # 공백일 경우 그대로 넣어주기
        if alpha == ' ':
            answer += ' '
        # 소문자일 경우, 옮긴 위치의 알파벳이 몇 번째에 위치하는지 파악한 후 문자로 넣어주기
        elif alpha.islower():
            answer += chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))
        # 대문자일 경우, 마찬가지로 해주기
        else:
            answer += chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))

    return answer