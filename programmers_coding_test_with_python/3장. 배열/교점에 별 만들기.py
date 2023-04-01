# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    # 교점 구하기
    lst = set()
    x_min, y_min = 1e9, 1e9
    x_max, y_max = -1e9, -1e9
    for i in range(len(line)):
        a, b, e = line[i]
        
        for j in range(i+1, len(line)):
            c, d, f = line[j]
            # 평행 또는 일치할 경우 구하지 않고 넘어감
            if a * d == b * c:
                continue
                
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            # 정수인 값들만 저장해주기
            if x == int(x) and y == int(y):
                lst.add((int(x), int(y)))
                # x, y좌표의 최대 최소점 찾기
                if x_min > x:
                    x_min = int(x)
                if x_max < x:
                    x_max = int(x)
                if y_min > y:
                    y_min = int(y)
                if y_max < y:
                    y_max = int(y)
    lst = list(lst)        

    answer = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    return answer