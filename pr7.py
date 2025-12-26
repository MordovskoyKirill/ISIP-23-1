# 1
'''
for x in '0123456789ABCDE':
    n1 = '123' + x + '5'
    n2 = '1' + x + '233'
    summa = int(n1, 15) + int(n2, 15)
    if summa % 14 == 0:
        otv = summa // 14
        print(otv)
        break

ost = []

while otv > 0:
    a = otv % 15
    ost.append(a)
    otv //= 15

sp = []
for i in ost:
    if i <= 9:
        sp.append(str(i))
    elif i == 10:
        sp.append('A')
    elif i == 11:
        sp.append('B')
    elif i == 12:
        sp.append('C')
    elif i == 13:
        sp.append('D')
    elif i == 14:
        sp.append('E')

print("".join(sp))
'''
#2
'''
for p in range(16, 100):
    n1 = int('A', 16) + int('B', 16) + 2 + 6 + 7 + int('D', 16) + 1
    n2 = int('F', 16) + 0 + 2 + 4 + int('A', 16) + 8 + 9
    summa = n1 + n2
    if summa % (p - 1) == 0:
        print(p)
        break
'''
#3
'''
for x in '0123456789':
    n1 = x + 'B09'
    n2 = x + '8E8'
    summa = int(n1, 17) + int(n2, 15)
    if summa % 155 == 0:
        otv = summa // 155
        print(otv)
        break
'''

#4
'''
for x in '01234567':
    for y in '01234567':
        n1 = y + '04' + x + '5'
        n2 = '253' + x + y
        summa = int(n1, 11) + int(n2, 8)
        if summa % 117 == 0:
            otv = summa // 117
            print(otv)
            break
'''
#5
'''
summa = 7 * (512**1912) + 6 * (64**1954) - 5 * (8**1991) - 4 * (8**1980) - 2022
count = 0
n = []

while summa > 0:
    n.append(summa % 8)
    summa //= 8
    
for i in n:
    if i == 7:
        count += 1
        
print(count)
'''