N = int(input())
nums = list(map(int, input().split()))

count = 0

for idx, num in enumerate(nums):
    if num == 2:
        count += 1
        
    if count == 3:
        print(idx+1)
        break