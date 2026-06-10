string, word = input().split()

result = string.find(word)
if result == -1:
    print('No')
else:
    print(result)