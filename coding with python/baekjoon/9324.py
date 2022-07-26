# my code

n = int(input())

for i in range(n):
    word = input()
    cnt = 0
    
    dic = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0,
      'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0,
      'Y':0, 'Z':0}
    
    for j in range(len(word)):
        if dic[word[j]] < 2:
            dic[word[j]] += 1
            cnt += 1
            
        elif dic[word[j]] == 2:
            if len(word) - 1 == j:
                break
            else:
                if word[j] != word[j+1]:
                    break
                else:
                    dic[word[j]] += 1
                    cnt += 1
                    
        elif dic[word[j]] == 3:
            dic[word[j]] = 0
            cnt += 1


    if cnt == len(word):
        print('OK')
    else:
        print('FAKE')
