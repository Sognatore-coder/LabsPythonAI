numbers = range(10, 100)
result = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0, numbers)))
print(result)