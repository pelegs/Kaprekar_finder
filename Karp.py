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
    return max - min


if __name__ == "__main__":
    num_digits: int = int(argv[1])
    max_num: int = 10**num_digits
    # max_num = 10

    # Generate an integer of repeating 1s to eliminate all its multiples
    # (i.e. numbers with a single repeating digit)
    repeat_1s: int = int("1" * num_digits)

    # Accumulating final values
    final_values: set[int] = set()

    # Actual main stuff
    for i in range(max_num):
        print(f"{i}\n=================")
        if i % repeat_1s != 0:
            current_num: int = i
            previous_num: int = current_num
            while current_num := step(current_num, num_digits):
                print(previous_num, current_num)
                if current_num in final_values or previous_num == current_num:
                    final_values.add(current_num)
                    break
                previous_num = current_num
        print("\n")
    print(f"\n=================")
    print(f"Final value(s): {final_values}")
