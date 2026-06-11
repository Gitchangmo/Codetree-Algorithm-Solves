S = input()

for w in S:
    if w >= 'a' and w <= 'z':
        print(w.upper(), end='')
    elif w >= 'A' and w <= 'Z':
        print(w.lower(), end='')