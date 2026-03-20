def solve(*coefficients):
    if len(coefficients) == 3:
        a, b, c = coefficients
        if a == 0:
            return solve(b, c)
        d = b**2 - 4*a*c
        if d < 0:
            return []
        if d == 0:
            return [-b / (2*a)]
        return sorted([(-b - d**0.5) / (2*a), (-b + d**0.5) / (2*a)])
    elif len(coefficients) == 2:
        b, c = coefficients
        if b == 0:
            return ["all"] if c == 0 else []
        return [-c / b]
    elif len(coefficients) == 1:
        c = coefficients[0]
        return ["all"] if c == 0 else []
    else:
        return None
    
print(sorted(solve(1, 2, 1)))
print(sorted(solve(1, -3, 2)))
print(solve(0, 0, 0)) 
print(solve(0, 0, 5)) 