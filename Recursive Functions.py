# fibonacci_cache = {}
#
# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     fibonacci_cache[n] = value
#     return value
#
# for n in range(1,1001):
#     print(n, ':', fibonacci(n))


from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,51):
    print(n, ":", fibonacci(n))
    print(fibonacci(n+1)/ fibonacci(n))
