prev_word = input()
while True:
    current_word = input()
    if current_word[0].lower() != prev_word[-1].lower():
        print(current_word)
        break
    prev_word = current_word