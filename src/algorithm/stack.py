"""Стек на основе списка."""


class Stack:
    """Хранит элементы так, чтобы последний добавленный извлекался первым."""

    def __init__(self) -> None:
        """Создаёт пустой стек."""
        self._items: list[object] = []

    def push(self, item: object) -> None:
        """Кладёт элемент на верхушку."""
        self._items.append(item)

    def pop(self) -> object:
        """Извлекает верхний элемент. Пустой стек вызывает IndexError."""
        if not self._items:
            raise IndexError("Нельзя извлечь элемент из пустого стека")
        return self._items.pop()

    def peek(self) -> object:
        """Показывает верхний элемент. Пустой стек вызывает IndexError."""
        if not self._items:
            raise IndexError("Пустой стек не имеет верхушки")
        return self._items[-1]

    def __len__(self) -> int:
        """Возвращает число элементов."""
        return len(self._items)

    def __bool__(self) -> bool:
        """Возвращает True, если в стеке есть элементы."""
        return bool(self._items)
