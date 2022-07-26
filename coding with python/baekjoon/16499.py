# my code

n = int(input())
lists = []
for i in range(n):
    word = list(input())
    
    word.sort()
    
    if word not in lists:
        lists.append(word)

print(len(lists))
