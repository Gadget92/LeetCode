from typing import List

def romanToInt(s: str) -> int:
    roman_as_int = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    sum = 0
    idx = 0 
    while idx <= len(s) - 1:
        chr = s[idx]

        if idx+1 <= len(s) - 1:
            next_chr = s[idx+1]
            next_number = roman_as_int[next_chr]
        else:
            next_number = 0

        if roman_as_int[chr] < next_number:
            sum += (next_number - roman_as_int[chr])
            idx += 2
        else:
            sum += roman_as_int[chr]
            idx += 1

    return sum
            
def romanToInt_v2(s: str) -> int:
    roman_as_int = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    numbers = [roman_as_int[char] for char in s]

    return sum(numbers)

