"""Алгоритм Евклида в двух вариантах."""


def _validate(a: int, b: int) -> None:
    """Проверяет, что переданы целые числа и хотя бы одно ненулевое."""
    if type(a) is not int or type(b) is not int:
        raise TypeError("НОД принимает два целых числа")
    if a == b == 0:
        raise ValueError("НОД двух нулей не определён в этом пакете")


def gcd_iterative(a: int, b: int) -> int:
    """Вычисляет НОД, обновляя пару чисел в цикле."""
    _validate(a, b)
    a = abs(a)
    b = abs(b)
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def _euclid(a: int, b: int) -> int:
    """Передаёт новую пару следующему вызову до нулевого остатка."""
    if b == 0:
        return a
    remainder = a % b
    return _euclid(b, remainder)


def gcd_recursive(a: int, b: int) -> int:
    """Проверяет аргументы и вычисляет НОД рекурсивно."""
    _validate(a, b)
    return _euclid(abs(a), abs(b))
