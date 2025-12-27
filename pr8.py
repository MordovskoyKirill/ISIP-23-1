# 1
def f(n):
    if n[0] > n[1]:
        return f(n[1:])
    if n[1] >= n[2] and n[2] >= n[3]:
        del n[1]
        return f(n)
    elif n[0] >= n[2] and len(n) >= 4:
        del n[2]
        return f(n)
    return n


sp = [6, 2, 5, 4, 2, 5, 6]
print(f(sp))
# 3
'''
k = 1050
count = 0                                                                                                               
for i in range(1, k + 1):
    if i + int(str(i)[::-1]) == k:
        sp.append(str(i))
        count += 1

print(f"Кол-во: {count}")

'''
