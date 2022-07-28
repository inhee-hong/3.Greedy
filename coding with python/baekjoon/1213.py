# my code

from collections import Counter

word = list(input())

# 한 글자 일때
if len(word) == 1:
    print(''.join(word))

# 두 글자 일때
elif len(word) == 2:
    if word[0] != word[1]:
        print("I'm Sorry Hansoo")
    else:
        print(''.join(word))

# 세 글자 이상, 홀수 개수 일 때        
elif len(word) % 2 != 0:
    word.sort()
    word = Counter(word)
    words = word.most_common()
    words.sort(key = lambda x : x[0])
    
    ans = ''
    ones = 0
    odd = 0
    for i in range(len(words)):
        if words[i][1] == 1:
            ones += 1
        if words[i][1] % 2 == 1:
            odd += 1
        if words[i][1] % 2 != 0:
            cnt = words[i][0]
        ans += words[i][0] * (words[i][1] // 2)

    if ones > 1 or ones == len(word):
        print("I'm Sorry Hansoo")
    elif odd > 2:
        print("I'm Sorry Hansoo")
    else:
        ans_reverse = ans[::-1]
        ans += cnt
        ans += ans_reverse
        print(ans)
        
# 세 글자 이상, 짝수 개수 일 때            
elif len(word) % 2 == 0:
    word.sort()
    word = Counter(word)
    words = word.most_common()
    words.sort(key = lambda x : x[0])
   
    ans = ''
    cnt = 0
    for i in range(len(words)):
        if words[i][1] % 2 != 0:
            cnt += 1
            break

        ans += words[i][0] * (words[i][1] // 2)

    ans_reverse = ans[::-1]
    ans += ans_reverse
    
    if cnt == 0:
        print(ans)
    else:
        print("I'm Sorry Hansoo")
