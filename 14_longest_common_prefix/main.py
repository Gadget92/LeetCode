from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    for word in zip(*strs):
        if len(set(word)) == 1:
            result += word[0]
        else:
            break
    return result

def longestCommonPrefix_v2(strs: List[str]) -> str:
    base_str = strs[0]
    idx = 1

    while idx <= len(base_str):
        char_in_strs = [str_item.startswith(base_str[:idx]) for str_item in strs[1:]]

        if all(char_in_strs):
            idx += 1
        else:
            break

    return base_str[:idx-1]



