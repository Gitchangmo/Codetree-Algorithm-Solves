nums = list(map(int, input().split()))

for i in range(3, 11):
    nums.append(((nums[-1])+(nums[-2])) % 10)

print(*nums, end='')