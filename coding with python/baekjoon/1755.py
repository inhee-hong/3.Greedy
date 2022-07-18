# my code

m, n = map(int, input().split())

dic = {'1' : 'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven',
      '8':'eight', '9':'nine', '0':'zero'}

lists = []
for i in range(m, n+1):
    word = str(i)
    
    if len(word) == 1:
        ans = dic[word]
        lists.append([i, ans])
    else:
        ans1 = dic[word[0]]
        ans2 = dic[word[1]]
        ans = ans1 + ans2
        lists.append([i, ans])

lists.sort(key = lambda x: x[1])

for j in range(len(lists)):
    if (j+1) % 10 == 0:
        print(lists[j][0], end = ' ')
        print()
    else:
        print(lists[j][0], end = ' ')
