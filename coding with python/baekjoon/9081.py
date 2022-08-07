# study (https://hillier.tistory.com/102)
# my code

n = int(input())

for i in range(n):
    new_word = ''
    word = list(input())
    
    for j in range(len(word)-1, 0, -1):
        if word[j] > word[j-1]:
            a = word[j-1]
            a_index = j-1
            break
        else:
            if j-1 == 0:
                new_word += ''.join(word)
                print(new_word)
                
    if len(new_word) != 0:
        continue
            
    for k in range(len(word)-1, 0, -1):
        if word[k] > a:
            b = word[k]
            b_index = k   
            break
            
    word[b_index], word[a_index] = word[a_index], word[b_index]
            
    word1, word2 = word[:a_index+1], word[a_index+1:]
    
    new_word += ''.join(word1) + ''.join(word2[::-1])
    print(''.join(new_word))





### fail code _ time over

from itertools import permutations

n = int(input())
for i in range(n):
    word = input()
    
    new = list(set(map(''.join, permutations(word, len(word)))))
    new.sort()
    
    index = new.index(word)
    
    if index == len(new)-1:
        print(word)
    else:
        print(new[index+1])
