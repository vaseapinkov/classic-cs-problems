from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1
    last_v: int = 0
    next_v: int = 1
    for _ in range(1, n):
        last_v, next_v = next_v, last_v + next_v
        yield next_v

