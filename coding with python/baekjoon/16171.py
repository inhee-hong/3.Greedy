# my code

import re

first = input()
word = re.sub('[^a-zA-Z]','',first)
second = input()

if second in word:
    print(1)
else:
    print(0)
