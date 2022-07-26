# my code

from collections import Counter

word = input()
word_list = []
word_num = []
p = 13
k = 13
h = 13
t = 13

while len(word) != 0:
    word_list.append(word[:3])
    word_num.append(word[:3][0])
    word = word[3:]
    
word_counter = Counter(word_list)
word_num = Counter(word_num)

if word_counter.most_common(1)[0][1] != 1:
    print('GRESKA')
else:
    for key, value in word_num.items():
        if key == 'P':
            p -= value
        elif key == 'K':
            k -= value
        elif key == 'H':
            h -= value
        elif key == 'T':
            t -= value
    print(p, k, h, t, end = ' ')
