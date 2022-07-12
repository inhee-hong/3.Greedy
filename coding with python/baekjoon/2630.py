

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
                #print(0, '-', i, j, n, '/', x, y)
                answer(x, y, n//2)
                #print(1, '=',i, j, n, '/', x, y)
                answer(x, y + n//2, n//2)
                #print(2, '=',i, j, n, '/', x, y)
                answer(x + n//2, y, n//2)
                #print(3, '=',i, j, n, '/', x, y)
                answer(x + n//2, y + n//2, n//2)
                #print(4,'=',i, j, n, '/', x, y)
                return
            
    if now == 0:
        white += 1
        #print('white =', 1)
    else:
        blue += 1
        #print('blue =', 1)

answer(0, 0, n)
print(white)
print(blue)


#  0 - 0 2 8 / 0 0
#  0 - 0 2 4 / 0 0
#  blue = 1
#  1 = 0 2 4 / 0 0
#  white = 1
#  2 = 0 2 4 / 0 0
#  white = 1
#  3 = 0 2 4 / 0 0
#  white = 1
#  4 = 0 2 4 / 0 0
#  1 = 0 2 8 / 0 0
#  0 - 0 6 4 / 0 4
#  white = 1
#  1 = 0 6 4 / 0 4
#  blue = 1
#  2 = 0 6 4 / 0 4
#  blue = 1
#  3 = 0 6 4 / 0 4
#  white = 1
#  4 = 0 6 4 / 0 4
#  2 = 0 2 8 / 0 0
#  0 - 4 1 4 / 4 0
#  0 - 4 1 2 / 4 0
#  blue = 1
#  1 = 4 1 2 / 4 0
#  white = 1
#  2 = 4 1 2 / 4 0
#  white = 1
#  3 = 4 1 2 / 4 0
#  blue = 1
#  4 = 4 1 2 / 4 0
#  1 = 4 1 4 / 4 0
#  white = 1
#  2 = 4 1 4 / 4 0
#  white = 1
#  3 = 4 1 4 / 4 0
#  blue = 1
#  4 = 4 1 4 / 4 0
#  3 = 0 2 8 / 0 0
#  blue = 1
#  4 = 0 2 8 / 0 0
#  9
#  7
