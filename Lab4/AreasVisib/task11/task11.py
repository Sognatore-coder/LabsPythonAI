one = 5
two = 4
three = 0

def to_roman(num):
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(vals)):
        while num >= vals[i]:
            result += syms[i]
            num -= vals[i]
    return result

def roman():
    global three
    three = one + two
    print(f"{to_roman(one)} + {to_roman(two)} = {to_roman(three)}")

roman()