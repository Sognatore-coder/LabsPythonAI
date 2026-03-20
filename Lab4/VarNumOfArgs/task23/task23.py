def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a] * m for _ in range(n)]

print("matrix():")
rows = matrix()
for row in rows:
    print(*row)

print("matrix(2):")
rows = matrix(2)
for row in rows:
    print(*row)

print("matrix(2, 3, 5):")
rows = matrix(2, 3, 5)
for row in rows:
    print(*row)