N = int(input())

arr = [input() for _ in range(N)]

count = 0
temp = ''

for s in arr:
    if s[0] == 'a':
        count += 1
    temp += s

print(len(temp), count)