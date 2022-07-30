# my code

T = int(input())

for _ in range(T):
    recode = list(map(str, input().split()))
    remove = []
    ans = []

    while True:
        word = input()

        if word == 'what does the fox say?':
            break
        else:
            word = word.split(' goes ')
            remove.append(word[1])

    for i in recode:
        if i not in remove:
            ans.append(i)

    print(' '.join(ans))
