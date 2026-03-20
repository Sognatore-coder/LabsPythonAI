def fractal_print(obj, depth=2):
    if depth == 0:
        return "[...]"
    if isinstance(obj, list):
        return "[" + ", ".join(fractal_print(x, depth - 1) for x in obj) + "]"
    return str(obj)

fractal = [3]
fractal.append(fractal)
res = fractal_print(fractal)
print(res)

fractal2 = [3]
fractal2.append(fractal2)
fractal2.append(2)
res2 = fractal_print(fractal2)
print(res2)
