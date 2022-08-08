# my code

s = str(input())
one = int(s.count('1') / 2)
zero = int(s.count('0') / 2)

new = ''
for i in range(len(s)):
    if one != 0:
        if s[i] == '1':
            one -= 1
        else:
            new += s[i]
    else:
        new += s[i]

new_word = ''
for j in range(len(new)):
    if zero != 0:
        if new[-1-j] == '0':
            zero -= 1
        else:
            new_word += new[-1-j]
    else:
        new_word += new[-1-j]
            
print(new_word[::-1])



#### 25점

from collections import Counter

s = str(input())

s = Counter(s)
ss = s.most_common()

if ss[0][0] == '0':
    word = ss[0][0] * int(ss[0][1]/2)  + ss[1][0] * int(ss[1][1]/2)
else:
    word = ss[1][0] * int(ss[1][1]/2)  + ss[0][0] * int(ss[0][1]/2)
    

print(word)
