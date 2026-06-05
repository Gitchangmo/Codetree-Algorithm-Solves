nums = list(map(int, input().split()))
temp = []

for num in nums:
    if num == 0:
        break
    temp.append(num)

Avg = sum(temp) / len(temp)

print(sum(temp), round(Avg, 1))