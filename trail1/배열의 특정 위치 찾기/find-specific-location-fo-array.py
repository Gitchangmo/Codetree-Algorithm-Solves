nums = list(map(int, input().split()))
N = len(nums)

Sum = []
Avg = []

for i in range(1, N, 2):
    Sum.append(nums[i])

for i in range(2, N, 3):
    Avg.append(nums[i])
    
print(sum(Sum), round((sum(Avg)/len(Avg)), 1))