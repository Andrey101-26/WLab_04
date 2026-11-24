"""Пузырьковая сортировка и сортировка слиянием."""


def _validate(values: list[int]) -> None:
    """Вызывает TypeError, если вход не является списком целых чисел."""
    if not isinstance(values, list):
        raise TypeError("Ожидается список")
    for value in values:
        if type(value) is not int:
            raise TypeError("Список должен содержать целые числа")


def bubble_sort(values: list[int]) -> list[int]:
    """Возвращает новый список, переставляя соседние элементы."""
    _validate(values)
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Объединяет два отсортированных списка в один."""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def _merge_sort(values: list[int]) -> list[int]:
    """Сортирует половины отдельно и объединяет их."""
    if len(values) <= 1:
        return values.copy()
    middle = len(values) // 2
    left = _merge_sort(values[:middle])
    right = _merge_sort(values[middle:])
    return _merge(left, right)


def merge_sort(values: list[int]) -> list[int]:
    """Возвращает новый список, отсортированный слиянием."""
    _validate(values)
    return _merge_sort(values)
