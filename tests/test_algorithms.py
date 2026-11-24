"""Проверки алгоритмов, стека и генераторов."""

from random import Random

import pytest

from algorithm.datasets import KINDS, make_dataset
from algorithm.gcd import gcd_iterative, gcd_recursive
from algorithm.sorting import bubble_sort, merge_sort
from algorithm.stack import Stack


@pytest.mark.parametrize("sort", [bubble_sort, merge_sort])
@pytest.mark.parametrize("values", [[], [1], [1, 2, 3], [3, 2, 1], [-2, 3, -2, 0]])
def test_sort(sort, values):
    """Проверяет результат и сохранность исходного списка."""
    original = values.copy()
    result = sort(values)
    assert result == sorted(original)
    assert result is not values
    assert values == original


@pytest.mark.parametrize("sort", [bubble_sort, merge_sort])
def test_random_sort(sort):
    """Сравнивает результат с эталоном на нескольких случайных списках."""
    rng = Random(42)
    for size in (10, 30, 100):
        values = [rng.randint(-50, 50) for _ in range(size)]
        assert sort(values) == sorted(values)


@pytest.mark.parametrize("sort", [bubble_sort, merge_sort])
@pytest.mark.parametrize("bad_input", [(1, 2), [1, "2"], [True]])
def test_sort_type_error(sort, bad_input):
    """Проверяет, что неверный тип отклоняется."""
    with pytest.raises(TypeError):
        sort(bad_input)


@pytest.mark.parametrize("gcd", [gcd_iterative, gcd_recursive])
@pytest.mark.parametrize("a,b,expected", [(18, 12, 6), (13, 7, 1), (0, 8, 8), (-8, 12, 4)])
def test_gcd(gcd, a, b, expected):
    """Проверяет обычные случаи, ноль и отрицательные числа."""
    assert gcd(a, b) == expected


@pytest.mark.parametrize("gcd", [gcd_iterative, gcd_recursive])
def test_gcd_invalid(gcd):
    """Проверяет ошибки для неверного типа и двух нулей."""
    with pytest.raises(TypeError):
        gcd("1", 2)
    with pytest.raises(ValueError):
        gcd(0, 0)


def test_stack_lifo():
    """Проверяет порядок извлечения и просмотр без удаления."""
    stack = Stack()
    assert len(stack) == 0 and not stack
    stack.push("А")
    stack.push("Б")
    assert stack and stack.peek() == "Б" and len(stack) == 2
    assert stack.pop() == "Б"
    assert stack.pop() == "А"
    assert not stack and len(stack) == 0


@pytest.mark.parametrize("operation", ["pop", "peek"])
def test_empty_stack(operation):
    """Проверяет исключение при обращении к пустому стеку."""
    with pytest.raises(IndexError):
        getattr(Stack(), operation)()


@pytest.mark.parametrize("kind", KINDS)
def test_datasets(kind):
    """Проверяет размер и воспроизводимость каждого вида набора."""
    assert make_dataset(kind, 0, seed=42) == []
    first = make_dataset(kind, 100, seed=42)
    assert len(first) == 100 and first == make_dataset(kind, 100, seed=42)


def test_dataset_shapes():
    """Проверяет порядок, малое число перестановок и повторы."""
    assert make_dataset("ascending", 5) == [0, 1, 2, 3, 4]
    assert make_dataset("descending", 5) == [4, 3, 2, 1, 0]
    nearly = make_dataset("nearly_sorted", 100, seed=42)
    assert sorted(nearly) == list(range(100))
    assert sum(value != i for i, value in enumerate(nearly)) == 2
    assert len(set(make_dataset("duplicates", 100, seed=42))) <= 5


@pytest.mark.parametrize("kind", ["random", "nearly_sorted", "duplicates"])
def test_seed_changes_dataset(kind):
    """Проверяет, что разные фиксированные seed дают разные случайные наборы."""
    assert make_dataset(kind, 1000, seed=1) != make_dataset(kind, 1000, seed=2)
