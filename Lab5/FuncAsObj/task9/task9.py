def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()
    vowels = set('aeiouy')
    login_consonants = [ch for ch in login if ch not in vowels]
    pass_vowels = [ch for ch in password if ch in vowels]
    pass_consonants = [ch for ch in password if ch not in vowels]

    vowel_ok = len(pass_vowels) == 3
    cons_ok = pass_consonants == login_consonants

    if vowel_ok and cons_ok:
        success(login)
    elif not vowel_ok and not cons_ok:
        failure(login, "Everything is wrong")
    elif not vowel_ok:
        failure(login, "Wrong number of vowels")
    else:
        failure(login, "Wrong consonants")

def main(login, password):
    def success(login):
        print(f"Привет, {login}!")
    def failure(login, err):
        print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {err.upper()}.")
    ask_password(login, password, success, failure)

main("anastasia", "nsyatos")