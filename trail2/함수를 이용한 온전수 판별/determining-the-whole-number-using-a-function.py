a, b = map(int, input().split())

# Please write your code here.
def is_onjeonsu(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if (n % 3 == 0 and n % 9 != 0):
        return False
    return True

count = 0
for num in range(a, b+1):
    if is_onjeonsu(num):
        count += 1

print(count)