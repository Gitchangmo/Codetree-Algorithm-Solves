n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
max_num = 0

for i in range(n):
    if max_num < nums[i] + nums[-(i+1)]:
        max_num = nums[i] + nums[-(i+1)]

print(max_num)