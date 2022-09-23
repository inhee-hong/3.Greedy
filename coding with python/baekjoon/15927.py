# my code

text = input()

def palindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[-i-1]:
            continue
        else:
            return False
    return True

if len(set(list(text))) == 1:
    print(-1)
elif palindrome(text) == True:
    print(len(text)-1)
elif palindrome(text) == False:
    print(len(text))   
    
