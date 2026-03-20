def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
print("До defractalize:", fractal)
defractalize(fractal)
print("После defractalize:", fractal)