n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def result(A):
    global m
    sum = 0
    while m > 0:
        sum += A[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        
    return sum

print(result(A))