# my code

a = input()
b = input()


dic = {'I' : 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


num = 0
while len(a) != 0:
    if a[:2] in dic2:
        num += dic2[a[:2]]
        a = a[2:]
    else:
        num += dic[a[:1]]
        a = a[1:]

while len(b) != 0:
    if b[:2] in dic2:
        num += dic2[b[:2]]
        b = b[2:]
    else:
        num += dic[b[:1]]
        b = b[1:]
        

ans = ''
while num != 0:
    if num >= 1000:
        ans += 'M'
        num -= 1000
        
    elif num >= 900:
        ans += 'CM'
        num -= 900
        del dic2['CM']
        del dic2['CD']
        
    elif num >= 500:
        ans +="D"
        num -=500
        del dic['D']
        
    elif num >= 400 and ("CD" in dic2):
        ans +="CD"
        num -=400
        
    elif num >= 100:
        ans +="C"
        num -=100
        
    elif num >= 90:
        ans +="XC"
        num -=90
        del dic2['XC']
        del dic2['XL']
        
    elif num >= 50:
        ans +="L"
        num -=50
        del dic['L']
        
    elif num >= 40 and ("XL" in dic2):
        ans +="XL"
        num -=40
        
    elif num >= 10:
        ans +="X"
        num -=10
        
    elif num >= 9:
        ans +="IX"
        num -=9
        del dic2['IX']
        del dic2['IV']
        
    elif num >= 5:
        ans +="V"
        num -=5
        del dic['V']
        
    elif num >= 4 and ("IV" in dic2):
        ans +="IV"
        num -=4
        
    elif num >= 1:
        ans +="I"
        num -=1
        
print(ans)
