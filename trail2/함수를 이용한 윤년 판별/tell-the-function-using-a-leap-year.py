y = int(input())

def result(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True   
    return False

if result(y):
    print('true')
else:
    print('false')