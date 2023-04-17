def lengthOfLastWord(s: str) -> int:
    s_list = s.strip().split()
    return len(s_list[-1])
