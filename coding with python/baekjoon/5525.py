# my code

n = int(input())
s = int(input())
word = input()

answer, i, count = 0, 0, 0

while i < (s - 1):
    if word[i:i+3] == 'IOI':
        i += 2
        count += 1
        
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
