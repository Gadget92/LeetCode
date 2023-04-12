from typing import List

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    valid_parentheses = ["()", "[]", "{}"]
    while s != "":
        if not any([parentheses in s for parentheses in valid_parentheses]):
            return False
        else:
            for parentheses in valid_parentheses:
                s = s.replace(parentheses, "")
    return True

def isValid_v2(s: str) -> bool:
    parentheses_pair = {"(": ")", "[": "]", "{":"}"}
    parentheses = []
    if len(s) % 2 != 0:
        return False
    
    for char in s:
        if char in parentheses_pair:
            parentheses += char
        elif len(parentheses) == 0:
            return False
        elif char != parentheses_pair[parentheses.pop()]:
            return False

    return len(parentheses) == 0



