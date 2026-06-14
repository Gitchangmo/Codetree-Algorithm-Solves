from collections import deque

n = int(input())

# Please write your code here.
Q = deque()

for i in range(1, n+1):
    Q.append(i)

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])