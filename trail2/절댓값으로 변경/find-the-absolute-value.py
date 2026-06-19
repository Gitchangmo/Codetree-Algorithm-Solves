n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def result(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = abs(arr[i])

result(arr)
print(*arr)