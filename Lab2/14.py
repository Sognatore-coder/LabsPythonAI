queens = []
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

def check_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            
            # Проверка: одна горизонталь, вертикаль или диагональ
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return "YES"  
    return "NO"

print(check_queens(queens))