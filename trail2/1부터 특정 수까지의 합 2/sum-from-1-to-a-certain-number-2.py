N = int(input())

# Please write your code here.
def Sum(N):
    if N == 1:
        return 1
    
    return Sum(N-1) + N

print(Sum(N))