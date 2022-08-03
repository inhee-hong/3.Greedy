# my code

s = input()
new = ''
word = ''

i = 0
while True:
    
    if i == len(s):
        break
        
    else:
        if len(word) == 0 and s[i] == '<':
            i += 1
            new += '<'
            while True:
                if s[i] == '>':
                    new += s[i]
                    i += 1
                    break
                else:
                    new += s[i]
                    i += 1
                    
        elif len(word) != 0 and s[i] == '<':
            new += word[::-1]
            i += 1
            new += '<'
            while True:
                if s[i] == '>':
                    new += s[i]
                    i += 1
                    word = ''
                    break
                else:
                    new += s[i]
                    i += 1
                    
        elif i == len(s)-1 and len(word) != 0:
            word += s[i]
            new += word[::-1]
            i += 1
            
        else:
            if s[i] == ' ':
                new += word[::-1]
                new += ' '
                word = ''
                i += 1
            else:
                word += s[i]
                i += 1
        
print(new)
    
