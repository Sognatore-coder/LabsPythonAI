N = int(input())
i = 1
row_len = 1
while i <= N:
    for _ in range(row_len):
        if i > N:
            break
        print(i, end=" ")
        i += 1
    print()
    row_len += 1