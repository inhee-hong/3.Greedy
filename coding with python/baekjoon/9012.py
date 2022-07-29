# my code

T = int(input())
for i in range(T):
    lists = []
    word = input()
    
    no = 0
    for j in range(len(word)):
        if word[j] == '(':
            lists.append(word[j])
        else:
            if word[-1] == ')':
                if len(lists) != 0:
                    lists = lists[:-1]
                else:
                    no += 1
            else:
                no += 1
                break
                
    if no == 0 and len(lists) == 0:            
        print('YES')
    else:
        print('NO')
