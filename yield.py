from collections.abc import Iterable


def f_range(start: int, stop: int, step: float) -> Iterable:
    x = start
    while x < stop:
        yield x
        x += step


print([x for x in f_range(0, 10, 0.5)])
