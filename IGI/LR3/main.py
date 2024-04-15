import math
x=0.1
n = 0
term = (math.factorial(2 * n) / (2 ** (2 * n) * (math.factorial(n) ** 2))) * (x ** (2 * n + 1) / (2 * n + 1))
print(term)