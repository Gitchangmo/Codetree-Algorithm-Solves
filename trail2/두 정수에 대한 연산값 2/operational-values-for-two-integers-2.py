a, b = map(int, input().split())

# Please write your code here.
def result(a, b):
    if a < b:
        a = a+10
        b = b*2
    else:
        a = a*2
        b = b+10
    
    return a, b

a, b = result(a, b)
print(a, b)