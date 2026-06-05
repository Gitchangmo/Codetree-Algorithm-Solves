N = int(input())

nums = list(map(int, input().split()))

result = [num for num in nums if num % 2 == 0]

print(*result, end='')