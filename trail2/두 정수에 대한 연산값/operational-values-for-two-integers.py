a, b = map(int, input().split())

# Please write your code here.
def result(a, b):
    if a < b:
        a = a * 2
        b = b + 25
    else:
        a = a + 25
        b = b * 2
    return a, b

a, b = result(a,b)

print(a, b)