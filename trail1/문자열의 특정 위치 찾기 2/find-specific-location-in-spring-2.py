w = input()

arr = ["apple", "banana", "grape", "blueberry", "orange"]

count = 0 

for s in arr:
    for i in range(len(s)):
        if (s[2] == w or s[3] == w):
            print(s)
            count += 1
            break

print(count)