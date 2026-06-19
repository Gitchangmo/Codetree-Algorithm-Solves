N = int(input())

# Please write your code here.
def result(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    
    return result(N-1) * result(N-2) % 100

print(result(N))