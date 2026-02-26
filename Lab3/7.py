words = input().split()
counter = {}
for w in words:
    counter[w] = counter.get(w,0) + 1
    print(counter[w] - 1, end=" ")