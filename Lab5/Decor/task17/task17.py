def check_password(func):
    def wrapper(*args, **kwargs):
        pwd = input("Введите пароль: ")
        if pwd == "secret":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None
    return wrapper

@check_password
def show_secret():
    print("Секретная информация")

show_secret()