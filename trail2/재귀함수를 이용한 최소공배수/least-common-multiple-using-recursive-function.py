n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def GCD(a, b):
    if b == 0:
        return a
    
    return GCD(b, a % b)

def LCM(a, b):
    return (a*b) // GCD(a, b)

def result(n):
    if n == 1:
        return arr[0]
    if n == 2:
        return LCM(arr[0], arr[1])

    return LCM(result(n-1), arr[n-1])

print(result(n))
