from functools import lru_cache


@lru_cache(maxsize=None)  # Decorator that allow to cache function returned values of a function
def fib4(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case
