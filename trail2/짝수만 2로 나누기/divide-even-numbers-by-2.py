n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def result(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

result(arr)
print(*arr)