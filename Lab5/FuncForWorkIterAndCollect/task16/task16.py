from functools import reduce
import math
numbers = list(map(int, input().split()))
gcd_all = reduce(math.gcd, numbers)
print(gcd_all)