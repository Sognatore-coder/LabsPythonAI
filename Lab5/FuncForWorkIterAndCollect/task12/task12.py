points = [(1, 2), (3, 4), (0, 0), (2, 1)]
sorted_points = sorted(points, key=lambda p: (p[0]**2 + p[1]**2, p[0], p[1]))
print(sorted_points)