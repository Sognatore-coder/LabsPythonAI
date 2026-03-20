arr = [3, 1, 4, 1, 5]
print("Исходный:", arr)

sorted_arr = sorted(arr)  # возвращает новый список
print("sorted():", sorted_arr)
print("После sorted:", arr)  # исходный не изменился

arr.sort()  # изменяет исходный список
print("sort():", arr)