temp = []

for i in range(3):
    str = input()
    temp.append(len(str))

print(max(temp) - min(temp))