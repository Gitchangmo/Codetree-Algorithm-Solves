S1 = input()
S2 = input()

temp1 = ''
temp2 = ''

for s1 in S1:
    if s1.isdigit():
        temp1 += s1
    
for s2 in S2:
    if s2.isdigit():
        temp2 += s2

print(int(temp1) + int(temp2))