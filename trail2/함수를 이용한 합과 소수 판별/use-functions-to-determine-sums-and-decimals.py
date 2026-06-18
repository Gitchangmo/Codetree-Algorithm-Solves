a, b = map(int, input().split())

# Please write your code here.
def sosu(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def result(num):
    if not sosu(num):
        return False
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    if sum % 2 == 0:
        return True
    else:
        return False

count = 0
for num in range(a, b+1):
    if result(num):
        count += 1

print(count)