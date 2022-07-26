# my code

word = input()

while len(word) != 0:
    if word[0] == 'p':
        check = word[:2]
        if check == 'pi':
            word = word[2:]
            continue
        else:
            break
    elif word[0] == 'k':
        check = word[:2]
        if check == 'ka':
            word = word[2:]
            continue
        else:
            break
    elif word[0] == 'c':
        check = word[:3]
        if check == 'chu':
            word = word[3:]
            continue
        else:
            break
    else:
        break
        
if len(word) == 0:
    print('YES')
else:
    print('NO')
