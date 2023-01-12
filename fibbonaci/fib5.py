def fib5(n: int) -> int:
    if n == 0: return n
    last_v: int = 0
    next_v: int = 1
    for _ in range(1, n):
        last_v, next_v = next_v, last_v + next_v
    return next_v
