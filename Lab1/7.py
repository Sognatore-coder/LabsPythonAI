n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

digits = [a, b, c, d]
digits.sort()

# Наименьшее четырёхзначное число
if digits[0] == 0:
    for i in range(1, 4):
        if digits[i] != 0:
            digits[0], digits[i] = digits[i], digits[0]
            break

result = digits[0]*1000 + digits[1]*100 + digits[2]*10 + digits[3]
print(result)