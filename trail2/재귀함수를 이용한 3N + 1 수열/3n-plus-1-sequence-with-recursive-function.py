n = int(input())
count = 0

# Please write your code here.
def result(n):
    global count
    count += 1
    if n == 1:
        return count
    if n % 2 == 0:
        return result(n//2)
    else:
        return result(n*3+1)

print(result(n)-1)