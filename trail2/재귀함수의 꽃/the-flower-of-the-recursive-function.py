N = int(input())

# Please write your code here.
def result(N):
    if N == 0:
        return

    print(N, end=' ')
    result(N-1)
    print(N, end=' ')

result(N)