numbers = list(map(int,input().split()))
uniq = []
for num in numbers:
    if numbers.count(num) == 1:
        uniq.append(num)
print(uniq)