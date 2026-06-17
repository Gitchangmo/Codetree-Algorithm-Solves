a, b = map(int, input().split())

# Please write your code here.

def num(a,b):
    count = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            count += 1
            continue
        i = str(i)
        if '3' in i or '6' in i or '9' in i:
            count += 1
    return count

print(num(a,b))