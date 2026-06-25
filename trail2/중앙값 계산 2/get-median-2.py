n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, n+1):
    if i % 2 == 1:
        new_arr = sorted(arr[:i])
        print(new_arr[i//2], end=' ')
    