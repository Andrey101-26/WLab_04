"""Подготовка списков для сравнения сортировок."""

from random import Random

KINDS = ("random", "ascending", "descending", "nearly_sorted", "duplicates")


def make_dataset(kind: str, size: int, seed: int | None = None) -> list[int]:
    """Создаёт список указанного вида без изменения глобального генератора."""
    if type(size) is not int or size < 0:
        raise ValueError("Размер должен быть неотрицательным целым числом")
    if kind not in KINDS:
        raise ValueError(f"Неизвестный вид набора: {kind}")

    rng = Random(seed)
    if kind == "random":
        values = []
        for _ in range(size):
            values.append(rng.randint(-size, size))
        return values
    if kind == "duplicates":
        values = []
        for _ in range(size):
            values.append(rng.randint(0, 4))
        return values
    if kind == "descending":
        return list(range(size - 1, -1, -1))

    values = list(range(size))
    if kind == "nearly_sorted" and size > 1:
        for _ in range(max(1, size // 100)):
            i = rng.randrange(size - 1)
            values[i], values[i + 1] = values[i + 1], values[i]
    return values
