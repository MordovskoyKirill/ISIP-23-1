# 1
"""
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(5))
"""
# 2
"""
def remove_vowels(string):
    if not string:
        return ""

    vowels = ["a","e", "i","o","u", "y"]
    char = string[0]
    text = string[1:]

    if char not in vowels:
        return char + remove_vowels(text)
    else:
        return remove_vowels(text)

print(remove_vowels('apple'))
print(remove_vowels('orange'))
print(remove_vowels('pear'))
print(remove_vowels('pineapple'))
print(remove_vowels('durian'))
print(remove_vowels('banana'))
"""
#3
"""
def pascal(n):
    if n == 1:
        return [1]

    row = pascal(n - 1)
    current = [1]

    for i in range(len(row) - 1):
        current.append(row[i] + row[i + 1])
    current.append(1)

    return current

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
print(pascal(6))
print(pascal(7))
print(pascal(8))
"""