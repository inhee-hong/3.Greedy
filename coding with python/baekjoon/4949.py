# my code

while True:
    word = list(input())
    
    if (''.join(word)) == '.':
        break
    else:
    
        lists = []
        no = 0
        for i in range(len(word)):
            if '(' == word[i]:
                lists.append(word[i])

            elif '[' == word[i]:
                lists.append(word[i])

            elif ')' == word[i]:
                if len(lists) == 0:
                    no += 1
                    continue

                if lists[-1] == '(':
                    lists = lists[:-1]
                else:
                    no += 1

            elif ']' == word[i]:
                if len(lists) == 0:
                    no += 1
                    continue

                if lists[-1] == '[':
                    lists = lists[:-1]
                else:
                    no += 1

        if len(lists) == 0 and no == 0:
            print('yes')
        else:
            print('no')
