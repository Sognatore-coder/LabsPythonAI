n = int(input())
surnames = []
for _ in range(n):
    surnames.append(input().strip())

count = 0
seen = set()
duplicates = set()

for s in surnames:
    if s in seen:
        duplicates.add(s)
    else:
        seen.add(s)

for s in duplicates:
    count+=surnames.count(s)

print(count)