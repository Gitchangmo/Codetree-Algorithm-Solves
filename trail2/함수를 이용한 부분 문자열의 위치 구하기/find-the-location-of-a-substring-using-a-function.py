text = input()
pattern = input()

# Please write your code here.
def _find():
    if not pattern in text:
        return -1
    return text.find(pattern)

print(_find())