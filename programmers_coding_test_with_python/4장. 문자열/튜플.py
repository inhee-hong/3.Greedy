def solution(s):
    answer = []
    
    # s는 문자열 형식이므로, list처럼 바꿔주기
    s = s[2:-2].split("},{")
    # 규칙에 따르면, 길이 순서대로 튜플을 놔주면 쉽게 전체 튜플을 구할 수 있음
    s.sort(key=lambda x: len(x))
    
    # 차집합 연산을 통해 새로 더해주어야 할 튜플 원소 찾고 넣어주기
    for lst in s:
        answer += list(set(lst.split(',')) - set(answer))
    
    # 리스트 내부 원소들을 int 형태로 바꾸어주기
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    
    return answer