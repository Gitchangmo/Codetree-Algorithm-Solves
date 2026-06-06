w = input()

arr = ["apple", "banana", "grape", "blueberry", "orange"]

count = 0 

for i in range(len(arr)):
    if (arr[i][2] == w or arr[i][3] == w):
        print(arr[i])
        count += 1

print(count)