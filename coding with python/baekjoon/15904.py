# my code

word_list = list(map(str, input()))

cnt = 0
for i in range(len(word_list)):
    if cnt == 0:
        if 'U' in word_list[i]:
            cnt += 1
    elif cnt == 1:
        if 'C' in word_list[i]:
            cnt += 1
    elif cnt == 2:
        if 'P' in word_list[i]:
            cnt += 1
    elif cnt == 3:
        if 'C' in word_list[i]:
            cnt += 1
            break

if cnt == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
