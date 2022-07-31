# my code

n = int(input())
pattern = list(input().split('*'))
first = len(pattern[0])
final = len(pattern[1])

for i in range(n):
    
    word = input()
    if first + final - len(word) > 0:
        print('NE')
    elif word[:first] == pattern[0] and word[len(word)-final:] == pattern[1]:
        print('DA')
    else:
        print('NE')
