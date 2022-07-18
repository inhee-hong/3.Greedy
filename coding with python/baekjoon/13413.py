# my code

from collections import Counter

T = int(input())

for i in range(T):
    n = int(input())
    first = input()
    final = input()
    
    lists = []
    for j in range(n):
        if first[j] != final[j]:
            lists.append(first[j])
    
    lists = Counter(lists)
    #print(lists)
    
    if len(lists) == 1:
        print(lists.most_common()[0][1])
    else:
        print(lists.most_common(2)[0][1])
