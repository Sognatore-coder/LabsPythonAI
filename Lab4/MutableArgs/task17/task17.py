def mirror(arr):
    mirrored_part = arr[::-1] # # Создаем новый список - перевернутую копию arr
    arr += mirrored_part
# reverse() изменяет список "на месте" и возвращает None. Нужно создать копию перевернутого списка, не изменяя исходный

arr = [1, 2]
mirror(arr)
print(*arr)

arr2 = [1]
mirror(arr2)
print(*arr2)