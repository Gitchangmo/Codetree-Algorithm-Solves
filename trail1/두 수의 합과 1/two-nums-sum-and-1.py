num1, num2 = map(int, input().split())

Sum = str(num1 + num2)
count = 0

for num in Sum:
    if num == '1':
        count += 1

print(count)