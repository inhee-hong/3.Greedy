# my code

max = 0
index = 0
for i in range(5):
    a, b, c, d = map(int, input().split())
    if max < a + b + c + d:
        max = a+b+c+d
        index = i+1
    
print(index, max)
