def russian_letters():
    start = ord('а')
    for i in range(32):
        yield chr(start + i)

for letter in russian_letters():
    print(letter, end=' ')