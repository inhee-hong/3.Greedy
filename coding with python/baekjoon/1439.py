# my code

from collections import Counter

n = input()

new = ''
for i in range(1, len(n)):
    if n[i-1] != n[i]:
        new += n[i-1]
if len(new) > 0:
    if n[len(n)-1] != new[-1]:
        new += n[len(n)-1]
    #print(new)
    
    D = Counter(new)
    print(min(D['1'], D['0']))
    
else:
    print(0)
