# my code

from collections import Counter

n = int(input())
book = []
for _ in range(n):
    book.append(input())
    
book = Counter(book)
books = book.most_common()
books.sort(key = lambda x : (-x[1], x[0]))
print(books[0][0])
