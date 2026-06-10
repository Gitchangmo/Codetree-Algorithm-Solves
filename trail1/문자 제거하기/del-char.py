S = input()
arr = list(S)

while len(arr) > 1:
    N = int(input())
    if N > len(arr)-1:
        arr.pop()
    else:
        arr.pop(N)
    print(''.join(arr))