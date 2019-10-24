from functools import lru_cache

def fibonacci(n):

    if type(n) != int:
        raise TypeError("n must be positive int")
    if n < 1:
       raise TypeError("n must be positive int")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n - 2)

for n in range(1,20):
    print(fibonacci(n))
