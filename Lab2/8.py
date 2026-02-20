word = input()
n = len(word)
middle = n // 2

if n % 2 ==1:
    for i in range(middle+1):
        left = word[middle-i]
        if i == 0:
            print(' ' * middle + left)
        else:
            right = word[middle+i]
            space_before = ' ' * (middle - i)
            space_between = ' ' * (2 * i - 1)
            print(space_before + left + space_between + right)
else:
    for i in range(middle):
        left = word[middle - 1 - i]
        right = word[middle + i]
        spaces_before = ' ' * (middle - 1 - i)
        spaces_between = ' ' * (2 * i + 1)
        print(spaces_before + left + spaces_between + right)