"""Замер времени сортировок и запись результатов в CSV."""

import argparse
import csv
from collections.abc import Callable
from pathlib import Path
from statistics import median
from time import perf_counter

from algorithm.datasets import KINDS, make_dataset
from algorithm.sorting import bubble_sort, merge_sort


def measure(
    sort: Callable[[list[int]], list[int]], source: list[int], repeats: int
) -> list[float]:
    """Возвращает длительность каждого запуска в миллисекундах."""
    times = []
    for _ in range(repeats):
        values = source.copy()
        start = perf_counter()
        result = sort(values)
        elapsed = perf_counter() - start
        times.append(elapsed * 1000)
        del result
    return times


def run_benchmark(
    output: Path, sizes: list[int], repeats: int = 5, seed: int = 42
) -> None:
    """Записывает результаты повторов и медиану для каждого набора."""
    if repeats < 5 or not sizes or any(size < 1 for size in sizes):
        raise ValueError("Нужны положительные размеры и не менее пяти повторов")

    with output.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        header = ["algorithm", "kind", "size", "repeats", "seed", "median_ms"]
        for number in range(1, repeats + 1):
            header.append(f"run_{number}_ms")
        writer.writerow(header)

        sorts = {"bubble_sort": bubble_sort, "merge_sort": merge_sort}
        for size in sizes:
            for kind in KINDS:
                source = make_dataset(kind, size, seed)
                for name, sort in sorts.items():
                    times = measure(sort, source, repeats)
                    row = [name, kind, str(size), str(repeats), str(seed)]
                    row.append(f"{median(times):.6f}")
                    for time in times:
                        row.append(f"{time:.6f}")
                    writer.writerow(row)


def main() -> None:
    """Читает параметры замера из командной строки."""
    parser = argparse.ArgumentParser(description="Сравнение времени сортировок")
    parser.add_argument("--sizes", type=int, nargs="+", default=[100, 1000, 10000])
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=Path("benchmark.csv"))
    args = parser.parse_args()
    try:
        run_benchmark(args.output, args.sizes, args.repeats, args.seed)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(f"Результаты записаны в {args.output}")


if __name__ == "__main__":
    main()
