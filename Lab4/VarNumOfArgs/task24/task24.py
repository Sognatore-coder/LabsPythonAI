def partial_sums(*args):
    sums = [0]
    for x in args:
        sums.append(sums[-1] + x)
    return sums

print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))