def bracket_check(test_string):
    balance = 0
    for ch in test_string:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                print("NO")
                return
    print("YES" if balance == 0 else "NO")

bracket_check("()")
bracket_check("((()(")
bracket_check("")