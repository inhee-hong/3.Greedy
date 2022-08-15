# my code

r, c = map(int, input().split())
puzzle = []
puzzle_ss = ['' for _ in range(c)]
for _ in range(r):
    aa = input()
    puzzle.append(aa)
    for k in range(c):
        puzzle_ss[k] += aa[k]

words = []

# 가로
for i in range(r):
    word = puzzle[i].split('#')
    
    for j in range(len(word)):
        if len(word[j]) > 1:
            words.append(word[j])
    
# 세로
for a in range(c):
    word = puzzle_ss[a].split('#')
    
    for b in range(len(word)):
        if len(word[b]) > 1:
            words.append(word[b])

words.sort()
print(words[0])
