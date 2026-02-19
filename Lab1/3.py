login = input()
email = input()
if "@" not in login and "@" in email:
    print("Корректно")
else:
    print("Некорректно")