A = input()

result = A[0]
count = 1
word = A[0]

# Please write your code here.
for i in range(1, len(A)):
    if A[i] != A[i-1]:
        result += str(count)
        result += A[i]
        count = 0
    count += 1

result += str(count)

print(len(result))
print(result)