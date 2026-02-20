text = input().split()

indices = list(map(int,input().split()))

res = []
for idx in indices:
    res.append(text[idx-1]) # -1, т.к нумерация с 1

res[0] = res[0].capitalize()
for i in range(1,len(res)):
    res[i] = res[i].lower()

output = ' '.join(res)
print(output)