numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers, key=abs, reverse=True)
print(*sorted_numbers)