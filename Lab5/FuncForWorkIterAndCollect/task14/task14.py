import sys
text = sys.stdin.read()
words = text.split()
seen = {}
result = []
for i, word in enumerate(words):
    if word[0].isupper() and word not in seen:
        seen[word] = i
        result.append((word, i))
result.sort()
for word, idx in result:
    print(idx, word)