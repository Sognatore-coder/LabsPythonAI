def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

for f in factorials(7):
    print(f, end=' ')