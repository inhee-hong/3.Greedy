# my code

n = int(input())

ans = n
for i in range(n):
    words = input()
    for j in range(1, len(words)):
        if words[j] == words[j-1]:
            continue
        else:
            if words[j-1] in words[j:]:
                ans -= 1
                break
        
print(ans)
