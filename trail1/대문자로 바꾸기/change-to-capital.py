alpha = [list(input().split()) for _ in range(5)]

for i in range(5):
    alpha[i] = list(map(str.upper, alpha[i]))
    print(*alpha[i])