def palindrome(s):
    cleaned_string = s.lower().replace(" ", "")
    if cleaned_string == cleaned_string[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"

print(palindrome('А роза упала на лапу Азора'))
print(palindrome('Палиндром'))