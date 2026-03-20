def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[matrix[i][j] for i in range(n)] for j in range(m)]
    matrix.clear()
    matrix.extend(transposed)

matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)