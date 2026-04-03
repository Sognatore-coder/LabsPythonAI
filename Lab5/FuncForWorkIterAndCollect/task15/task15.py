from functools import reduce
import sys
words = [line.strip() for line in sys.stdin if line.strip()]
if words:
    min_word = reduce(lambda a, b: a if a < b else b, words)
    print(min_word)