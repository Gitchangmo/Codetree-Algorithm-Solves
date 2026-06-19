a, b, c = map(int, input().split())

# Please write your code here.
mul = a*b*c

def Sum(mul):
    if mul < 10:
        return mul
    
    return Sum(mul//10) + Sum(mul%10)

print(Sum(mul))