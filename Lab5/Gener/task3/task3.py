def square_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a * a
        a, b = b, a + b

for sq in square_fibonacci(7):
    print(sq, end=' ')