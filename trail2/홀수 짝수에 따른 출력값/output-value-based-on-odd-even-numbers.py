N = int(input())

# Please write your code here.
def result(N):
    if N % 2 == 0:
        if N == 2:
            return 2
        return result(N-2) + N
    else:
        if N == 1:
            return 1
        return result(N-2) + N

print(result(N))