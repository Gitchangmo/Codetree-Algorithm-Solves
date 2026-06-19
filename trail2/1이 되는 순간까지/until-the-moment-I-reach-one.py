N = int(input())

count = 0
# Please write your code here.
def result(N):
    global count
    count += 1
    if N == 1:
        return count-1
    if N % 2 == 0:
        return result(N//2)
    if N % 2 == 1:
        return result(N//3)
    

print(result(N))