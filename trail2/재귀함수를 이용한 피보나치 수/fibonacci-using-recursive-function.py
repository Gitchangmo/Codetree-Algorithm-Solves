N = int(input())

# Please write your code here.
def result(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    return result(N-1) + result(N-2)

print(result(N))