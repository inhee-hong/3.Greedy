# my code

n = int(input())
word = list(input())
word.sort()

ans = 0
for i in range(n-1):
    word2 = list(input())
    word2.sort()
    
    if word == word2:
        ans += 1
    else:
        cnt = 0
        word_copy = word.copy()
        
        if len(word) == len(word2):
            for j in range(len(word)):
                if word2[j] in word_copy:
                    word_copy.remove(word2[j])
                else:
                    cnt += 1
            if cnt == 1:
                ans += 1
        
        elif (len(word) + 1) == len(word2):
            for j in range(len(word)):
                if word[j] in word2:
                    word2.remove(word[j])
                else:
                    cnt += 1
            if cnt == 0:
                ans += 1
                
        elif (len(word2) + 1) == len(word):
            for j in range(len(word2)):
                if word2[j] in word_copy:
                    word_copy.remove(word2[j])
                else:
                    cnt += 1
            if cnt == 0:
                ans += 1
print(ans)
