letters = (chr(ord('а') + i) for i in range(32))
for letter in letters:
    print(letter, end=' ')