str = input()
word = input()

count = 0

for s in str:
    if word == s:
        count += 1

print(count)