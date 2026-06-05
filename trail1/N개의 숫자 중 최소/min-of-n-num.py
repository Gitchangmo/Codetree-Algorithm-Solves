import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = sys.maxsize
count = 0

for num in a:
    if num < min_val:
        min_val = num

for num in a:
    if num == min_val:
        count += 1

print(min_val, count)