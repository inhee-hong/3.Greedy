# my code

n = input()

num = len(str(n)) // 2

left = 0
right = 0

for i in range(len(n)):
    if i < num:
        left += int(n[i])
    else:
        right += int(n[i])
        
if left == right:
    print('LUCKY')
else:
    print('READY')
