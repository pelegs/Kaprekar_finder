"""
File: Karp.py
Author: Peleg Sapir
Date: 7/2025
Description: A very simple Kaprekar's constant calculator because I was bored.
Todo: implement a general stopping condition which is not dependant on known constants
(and can potentially find oscillations and/or no-stop cases).
"""

from sys import argv

stop_dict: dict[int, int] = {3: 495, 4: 6174}


def get_sorted(n: int, p: int = 4) -> tuple[int, int]:
    fmt: str = f"0{p}d"
    n_str: str = f"{n:{fmt}}"
    ascending: int = int("".join(sorted(n_str)))
    decending: int = int("".join(sorted(n_str)[::-1]))
    return (ascending, decending)


def minmax(a: int, b: int) -> tuple[int, int]:
    return (min(a, b), max(a, b))


def step(n: int, digits: int = 4) -> int:
    ascending: int
    decending: int
    ascending, decending = get_sorted(n, digits)
    min: int
    max: int
    min, max = minmax(ascending, decending)
    new_val: int = max - min
    print(f"{max}-{min}={new_val}")
    if new_val != stop_dict[digits]:
        return new_val
    return 0


if __name__ == "__main__":
    digits: int = int(argv[1])
    repeat_1s: int = int("1" * digits)
    for n in range(10**digits):
        print(f"{n}\n=================")
        if n % repeat_1s != 0:
            new: int = n
            while new := step(new, digits):
                pass
        print("\n")
