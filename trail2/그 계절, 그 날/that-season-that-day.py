Y, M, D = map(int, input().split())

# Please write your code here.
def is_leap_year(Y):
    if Y % 4 != 0:
        return False
    if Y % 100 != 0:
        return True
    if Y % 400 == 0:
        return True
    return False

def is_valid_date(Y, M, D):
    if M == 2:
        max_day = 29 if is_leap_year(Y) else 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        max_day = 30
    else:
        max_day = 31
    
    return D <= max_day

if not is_valid_date(Y, M, D):
    print(-1)
else:
    if 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    else:
        print("Winter")