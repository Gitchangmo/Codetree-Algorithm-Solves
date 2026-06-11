S = input()
print(S)

for _ in range(len(S)):
    S = S[-1] + S[:-1]
    print(S)

