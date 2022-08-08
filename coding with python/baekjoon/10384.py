# my code

from collections import Counter

n = int(input())

for j in range(n):
    
    dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
          'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
          'y':0, 'z':0}
    
    sen = input()
    sen = sen.lower()
    for i in range(len(sen)):
        if sen[i] in dic:
            dic[sen[i]] += 1
    #print(dic)
    
    dics = Counter(dic).most_common()
    #print(dics)
    if dics[-1][1] == 0:
        print('Case ', j+1, ": ", 'Not a pangram', sep = '')
    elif dics[-1][1] == 1:
        print('Case ', j+1, ": ", 'Pangram!', sep = '')
    elif dics[-1][1] == 2:
        print('Case ', j+1, ": ", 'Double pangram!!', sep = '')
    elif dics[-1][1] == 3:
        print('Case ', j+1, ": ", 'Triple pangram!!!', sep = '')
