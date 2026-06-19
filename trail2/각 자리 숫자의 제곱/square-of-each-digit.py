N = int(input())

# Please write your code here.
def result(N):
    if N < 10:
        return N*N
    
    return result(N//10) + ((N%10) * (N%10))

print(result(N))