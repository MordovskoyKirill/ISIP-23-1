#1
"""
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
if (1 <= x1 <= 8) and (1 <= y1 <= 8) and (1 <= x2 <= 8) and (1 <= y2 <= 8):
    if (x1 != x2) and (y1 != y2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if (dx + dy) == 3:
            print("Конь может ходить")
        else:
            print("Конь не можеит ходить")
    else:
        print("Конь неходит на одну и ту же клетку")
else:
    print("Ошибка!")
"""

#2
"""
k = int(input("K:"))
n = int(input("N:")) + 1
sum = 0
for i in range(k, n):
    if (i % 2) == 0:
        sum += i
print(sum)
"""

#3
"""
sum = 0
while (True):
    x = int(input())
    if (x != 0):
       sum += x
    else:
        break
print(sum)
"""

#4
"""
n = int(input()) + 1
sum = 1
for i in range(1, n):
    sum *= i
print(sum)
"""