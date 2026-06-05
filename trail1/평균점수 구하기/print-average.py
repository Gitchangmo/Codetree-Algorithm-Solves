scores = list(map(float, input().split()))

Avg = sum(scores) / len(scores)
print(f"{Avg:.1f}")