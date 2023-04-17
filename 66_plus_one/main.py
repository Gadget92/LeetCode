from typing import List


def plusOne(digits: List[int]) -> List[int]:
    values = int("".join(list(map(str, digits)))) + 1
    return [int(char) for char in str(values)]
