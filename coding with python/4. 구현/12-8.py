# my code

n = input()

a = ''
num = 0

for i in range(len(n)):
    if n[i].isalpha():
        a += n[i]
    else:
        num += int(n[i])

print(''.join(sorted(a)) + str(num))
