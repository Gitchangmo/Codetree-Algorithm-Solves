N = int(input())

# Please write your code here.
def result(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    return result(N//3) + result(N-1)

print(result(N))