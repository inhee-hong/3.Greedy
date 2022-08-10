# my code

from collections import Counter
import sys
work =[]
work = sum([line.split() for line in sys.stdin.readlines()],[])
lens = len(work)

work = Counter(work)

print('Re', work['Re'], format(work['Re'] / lens, ".2f"))
print('Pt', work['Pt'], format(work['Pt'] / lens, ".2f"))
print('Cc', work['Cc'], format(work['Cc'] / lens, ".2f"))
print('Ea', work['Ea'], format(work['Ea'] / lens, ".2f"))
print('Tb', work['Tb'], format(work['Tb'] / lens, ".2f"))
print('Cm', work['Cm'], format(work['Cm'] / lens, ".2f"))
print('Ex', work['Ex'], format(work['Ex'] / lens, ".2f"))
print('Total', lens, '1.00')

#### 입력 주의하자
