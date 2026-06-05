nums = list(map(int, input().split()))
temp = []

for num in nums:
    if num == 0:
        break
    temp.append(num)


print(*temp[::-1])