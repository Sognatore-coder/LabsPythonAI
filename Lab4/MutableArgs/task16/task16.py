def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
# Используем append для изменения исходного списка
# sequence = sequence + [next_element] - это создавало новый список и теряло ссылку на старый.

sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)

sequence2 = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence2, 0)
print(*sequence2)