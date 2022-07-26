# my code

word = input()

ans = []
for i in range(len(word)):
    a = word[i:]
    ans.append(a)

ans.sort()
for j in range(len(ans)):
    print(ans[j])
