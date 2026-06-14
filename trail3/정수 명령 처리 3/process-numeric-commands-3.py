from collections import deque

n = int(input())

Q = deque()

for _ in range(n):
    line = input().split()
    if line[0] in ["push_front", "push_back"]:
        num = int(line[1])
        if line[0] == 'push_front':
            Q.appendleft(num)
        else:
            Q.append(num)
    elif line[0] == 'pop_front':
        print(Q.popleft())
    elif line[0] == 'pop_back':
        print(Q.pop())
    elif line[0] == 'size':
        print(len(Q))
    elif line[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif line[0] == 'front':
        print(Q[0])
    elif line[0] == 'back':
        print(Q[-1])

# Please write your code here.
