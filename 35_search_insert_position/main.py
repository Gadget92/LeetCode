from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)

    nums.append(target)
    nums.sort()
    return nums.index(target)
