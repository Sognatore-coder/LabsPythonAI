n = int(input())
m = int(input())
symb = input()

for i in range(n):
    if i == 0 or i == n - 1:
        print(symb * m)
    else:
        print(symb + " " * (m - 2) + symb)