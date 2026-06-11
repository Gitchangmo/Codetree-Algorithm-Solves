S1, S2 = input().split()

for idx, s1 in enumerate(S1):
    if not s1.isdigit():
        S1 = S1[:idx]
        
for idx, s2 in enumerate(S2):
    if not s2.isdigit():
        S2 = S2[:idx]

print(int(S1) + int(S2))
        