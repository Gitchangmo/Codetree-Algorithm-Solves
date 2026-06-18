a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def result(a, o, c):
    if o == '+':
        return f"{a} + {c} = {a + c}"
    elif o == '-':
        return f"{a} - {c} = {a - c}"
    elif o == '/':
        return f"{a} / {c} = {a // c}"
    elif o == '*':
        return f"{a} * {c} = {a * c}"
    else:
        return 'False'
    
print(result(a,o,c))