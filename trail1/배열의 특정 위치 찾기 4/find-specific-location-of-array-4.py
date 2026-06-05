nums = list(map(int, input().split()))
temp = []

for num in nums:
    if num == 0:
        break
    if num % 2 == 0:
        temp.append(num)

print(len(temp), sum(temp))