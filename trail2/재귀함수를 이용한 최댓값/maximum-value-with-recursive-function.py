n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max_val(n):
    if n == 1:
        return arr[0]
    max_num = max_val(n-1)
    if max_num > arr[n-1]:
        return max_num
    else:
        return arr[n-1]
    

print(max_val(n))