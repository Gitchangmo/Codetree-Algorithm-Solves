a = input()

n = ord(a)

if n == 97:
    n = 122
else:
    n -= 1

print(chr(n))