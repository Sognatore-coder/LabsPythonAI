s = input()
mid = (len(s) + 1) // 2
result = s[mid:] + s[:mid]
print(result)