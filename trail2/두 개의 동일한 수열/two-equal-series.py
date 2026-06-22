n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

is_Same = True
for i in range(n):
    if A[i] != B[i]:
        is_Same = False
        break

if is_Same:
    print('Yes')
else:
    print('No')