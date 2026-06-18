Y, M, D = map(int, input().split())

# Please write your code here.
def year(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    return False

def leaf(M, D):
    if M == 2:
        if D > 29:
            return -1
    if M == 4 or M == 6 or M == 9 or M == 11:
        if D > 30:
            return -1
    else:
        if D > 31:
            return -1

    if M >= 3 and M <= 5:
        return 'Spring'
    elif M >= 6 and M <= 8:
        return 'Summer'
    elif M >= 9 and M <= 11:
        return 'Fall'
    else:
        return 'Winter'

def common(M, D):
    if M == 2:
        if D > 28:
            return -1
    if M == 4 or M == 6 or M == 9 or M == 11:
        if D > 30:
            return -1
    else:
        if D > 31:
            return -1

    if M >= 3 and M <= 5:
        return 'Spring'
    elif M >= 6 and M <= 8:
        return 'Summer'
    elif M >= 9 and M <= 11:
        return 'Fall'
    else:
        return 'Winter'

if year(Y):
    print(leaf(M, D))
else:
    print(common(M, D))