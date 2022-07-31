# my code

s = input()

lists = []
for i in range(len(s)):
    for j in range(i, len(s)):
        word = s[i:j+1]
        lists.append(word)
        
print(len(set(lists)))
