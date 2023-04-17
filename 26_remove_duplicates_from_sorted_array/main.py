from typing import List


def removeDuplicates(nums: List[int]) -> int:
    for i in set(nums):
        count = nums.count(i)
        while count != 1:
            nums.remove(i)
            count -= 1

    return len(nums)
