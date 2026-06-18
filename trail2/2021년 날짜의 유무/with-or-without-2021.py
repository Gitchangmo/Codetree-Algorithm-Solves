M, D = map(int, input().split())

# Please write your code here.

def result(M, D):
    if M == 2:
        if D > 28:
            return False
    if M > 12:
        return False
    if M == 4 or M == 6 or M == 9 or M == 11:
        if D > 30:
            return False
    else:
        if D > 31:
            return False
    
    return True

if result(M, D):
    print('Yes')
else:
    print('No')