string = input()

arr = list(string)

word1 = arr[0]
word2 = arr[1]

for idx, w in enumerate(arr):
    if w == word1:
        arr[idx] = word2
    elif w == word2:
        arr[idx] = word1

print(''.join(arr))