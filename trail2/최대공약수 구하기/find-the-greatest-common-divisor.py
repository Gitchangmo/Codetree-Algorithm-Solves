n, m = map(int, input().split())

# Please write your code here.
def GCD(n, m):
    for i in range(100, 0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break

GCD(n, m)