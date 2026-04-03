words = input().split()
sorted_words = sorted(words, key=str.lower)
print(' '.join(sorted_words))