word = input()
result = ""

for i, letter in enumerate(word,1):
    result += letter * i
print(result)