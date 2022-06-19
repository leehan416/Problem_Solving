from math import factorial
n, m = map(int, input().split())
value = factorial(n) // (factorial(m) * factorial(n - m))
print(value)