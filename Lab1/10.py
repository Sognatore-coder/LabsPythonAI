import math

def factorial(n):
    if n < 0:
        return None
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

result = None
while True:
    data = input().split()
    if not data:
        continue
    num1 = int(data[0])
    if len(data) == 1:
        # Команда только с числом, значит это первое число операции
        op = input().strip()
        if op == "!":
            res = factorial(num1)
            if res is not None:
                print(res)
            continue
        elif op == "x":
            print(num1)
            break
        else:
            num2 = int(input())
    else:
        op = data[1]
        if op == "!":
            res = factorial(num1)
            if res is not None:
                print(res)
            continue
        elif op == "x":
            print(num1)
            break
        else:
            num2 = int(data[2])

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 != 0:
            print(num1 // num2)
    elif op == "%":
        if num2 != 0:
            print(num1 % num2)