w1, w2 = input().split()

a1 = ord(w1)
a2 = ord(w2)

sub = 0

if a1>a2:
    sub = a1-a2
else:
    sub = a2-a1
print((a1+a2), (sub))