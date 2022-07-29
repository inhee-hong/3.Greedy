# my code

from collections import Counter

n = int(input())

lists = []
for i in range(n):
    word = input()
    word = word.split('.')
    lists.append(word[1])
    
lists = Counter(lists)
new_list = sorted(lists.items())

for j in range(len(new_list)):
    print(new_list[j][0], new_list[j][1])
