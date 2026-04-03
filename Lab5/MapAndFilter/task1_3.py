numbers = [10, 18, 20, 30, 5]
result = list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers)))
print(result)