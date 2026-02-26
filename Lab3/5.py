n = int(input())
words = set()
for _ in range(n):
    words.update(input().split())
print(len(words))