n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()
count = 0

for s in str:
    if s[:len(t)] == t:
        count += 1
        if count == k:
            print(s)
        