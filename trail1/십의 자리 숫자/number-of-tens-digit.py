nums = list(map(int, input().split()))

arr = [0] * 10

for num in nums:
    if num == 0:
        break
    count_num = num // 10
    if count_num > 0:
        arr[count_num] += 1

for i in range(1, 10):
    print(f"{i} - {arr[i]}")