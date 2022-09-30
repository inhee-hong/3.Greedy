# my code

texts = input()
bomb = input()
stack = []
len_bomb = len(bomb)

for text in texts:
    stack.append(text)
    if stack[-1] == bomb[-1]:
        if ''.join(stack[-len_bomb:]) == bomb:
            del stack[-len_bomb:]

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
