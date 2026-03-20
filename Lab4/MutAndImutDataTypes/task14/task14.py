numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
 if number % 2 == 0:
    even.append(number)
 else:
    odd.append(number)

print("Чётные:", even)
print("Нечётные:", odd)

# Ошибка была в строке: odd = even = []
# Так делать нельзя для изменяемых объектов, потому что odd и even начинают указывать на один и тот же список, изменяя один, мы меняем и другой