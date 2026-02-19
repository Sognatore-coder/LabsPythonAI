n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
mx = max(a,b,c)
mn = min(a,b,c)
mid = (mx + mn) / 2
if mid == (a+b+c-mx-mn):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")