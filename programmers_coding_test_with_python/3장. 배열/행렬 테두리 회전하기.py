# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def rotation(x1, y1, x2, y2, rows, columns, graph):
    # graph와 동일한 형태를 가진 배열 생성, min_value를 위해 초기값 정해주기
    new_graph = [[0 for j in range(columns)] for i in range(rows)]
    min_value = 1e5
    
    # 아래로 내려가는 경우
    for x in range(x1, x2):
        new_graph[x][y2-1] = graph[x-1][y2-1]
        min_value = min(new_graph[x][y2-1], min_value)
    # 오른쪽으로 가는 경우
    for y in range(y1, y2):
        new_graph[x1-1][y] = graph[x1-1][y-1]
        min_value = min(new_graph[x1-1][y], min_value)
    # 위로 올라가는 경우
    for x in range(x2, x1, -1):
        new_graph[x-2][y1-1] = graph[x-1][y1-1]
        min_value = min(new_graph[x-2][y1-1], min_value) 
    # 왼쪽으로 가는 경우
    for y in range(y2, y1, -1):
        new_graph[x2-1][y-2] = graph[x2-1][y-1]
        min_value = min(new_graph[x2-1][y-2], min_value)    
        
    # 위의 과정으로 인해 입력된 값이 아닌 다른 값들은 원래 graph 값으로 채워주기
    for i in range(rows):
        for j in range(columns):
            if new_graph[i][j] == 0:
                new_graph[i][j] = graph[i][j]
    
    return new_graph, min_value


def solution(rows, columns, queries):
    answer = []
    # graph 생성해주기
    graph = [[(i-1) * columns + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    for x1, y1, x2, y2 in queries:
        graph, value = rotation(x1, y1, x2, y2, rows, columns, graph)
        answer.append(value)
    
    return answer