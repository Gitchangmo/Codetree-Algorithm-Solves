A = input()

# Please write your code here.
def is_palindrome(A):
    temp = A[::-1]
    if temp == A:
        return 'Yes'
    else:
        return 'No'

print(is_palindrome(A))