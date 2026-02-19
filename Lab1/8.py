count = 0
heights = []
while True:
    s = input()
    if s == "!":
        break
    h = int(s)
    if 150 <= h <= 190:
        count += 1
        heights.append(h)

print(count)
if heights:
    print(min(heights), max(heights))
else:
    print()