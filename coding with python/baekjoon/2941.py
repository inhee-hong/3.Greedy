# my code

word = input()

word_lists = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in word_lists:
    if i in word:
        word = word.replace(i, '1')

print(len(word))
