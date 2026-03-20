def tic_tac_toe(field):
    lines = []
    # строки
    lines.extend(field)
    # столбцы
    for col in range(3):
        lines.append([field[row][col] for row in range(3)])
    # диагонали
    lines.append([field[i][i] for i in range(3)])
    lines.append([field[i][2 - i] for i in range(3)])
    
    for line in lines:
        if line[0] != '-' and all(x == line[0] for x in line):
            print(f"{line[0]} win")
            return
    print("draw")

data = """- 0 -
x x x
0 0 -"""
field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)