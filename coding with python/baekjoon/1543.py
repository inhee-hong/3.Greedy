# my code

n = input()
word = input()

while word in n:
    n = n.replace(word, '*')

print(n.count('*'))
