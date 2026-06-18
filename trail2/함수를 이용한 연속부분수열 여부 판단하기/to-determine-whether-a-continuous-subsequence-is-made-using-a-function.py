n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def result(a, b):
    for i in range(len(a)-len(b)+1):
        temp = a[i:i+len(b)]
        if temp == b:
            return True
    return False

if result(a,b):
    print('Yes')
else:
    print('No')