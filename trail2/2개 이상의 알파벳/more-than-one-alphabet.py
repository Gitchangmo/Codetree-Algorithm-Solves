A = input()

# Please write your code here.
def result(A):
    a = A[0]
    count = 0
    for i in range(1, len(A)):
        if a != A[i]:
            count += 1

    if count:
        return 'Yes'
    else:
        return 'No'
    

print(result(A))
        