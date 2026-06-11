n, m = map(int, input().split())

# Please write your code here.
def LCM(n, m):
    start = max(n, m)
    while True:
        if start % m == 0 and start % n == 0:
            print(start)
            break
        start += 1

LCM(n, m)