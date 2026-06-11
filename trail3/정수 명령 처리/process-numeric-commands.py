N = int(input())
ans = []
Stack = []

for _ in range(N):
    line = input().split()
    
    if line[0] == 'push':
        line[1] = int(line[1])
        Stack.append(line[1])
    elif line[0] == 'pop':
        ans.append(Stack.pop())
    elif line[0] == 'size':
        ans.append(len(Stack))
    elif line[0] == 'empty':
        ans.append(1 if not Stack else 0)
    elif line[0] == 'top':
        ans.append(Stack[-1])

print('\n'.join(map(str, ans)))
