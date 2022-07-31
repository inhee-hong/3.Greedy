# my code

from itertools import permutations

def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            return 0
    return 1        
            
            
T = int(input())
for i in range(T):
    cnt = 0
    n = int(input())
    word = [input() for _ in range(n)]
    
    if len(word) == 1:
        pass
    else:
        word_list = list(set(permutations(word, 2)))

        for k in word_list:
            a = ''.join(k)
            
            if isPalindrome(a) == 1:
                cnt += 1
                print(a)
                break 
                
    if cnt == 0:
        print(0)
