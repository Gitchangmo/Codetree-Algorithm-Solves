a = input()

n = ord(a)

if n == 122:
    n = 97
else:
    n += 1

print(chr(n))