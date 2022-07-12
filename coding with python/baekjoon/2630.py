

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def answer(x, y, n):
    global white
    global blue
    
    now = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != paper[i][j]:
                answer(x, y, n//2)
                answer(x, y + n//2, n//2)
                answer(x + n//2, y, n//2)
                answer(x + n//2, y + n//2, n//2)
                return
            
    if now == 0:
        white += 1
    else:
        blue += 1

answer(0, 0, n)
print(white)
print(blue)
