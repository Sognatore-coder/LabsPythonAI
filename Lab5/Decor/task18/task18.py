def check_password(required_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pwd = input("Введите пароль: ")
            if pwd == required_password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None
        return wrapper
    return decorator

@check_password("12345")
def make_burger(meat, withOnion=False, withTomato=True):
    print(f"Готовим бургер с {meat}, лук: {withOnion}, томат: {withTomato}")

make_burger("Телятина")