N = int(input())
scores = list(map(float, input().split()))

Avg = sum(scores) / len(scores)
result = round(Avg, 1)


if result < 3.0:
    print(result)
    print("Poor")
elif result < 4.0:
    print(result)
    print("Good")
else:
    print(result)
    print("Perfect")