from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    for i in range(n):
        nums1[-i - 1] = nums2[i]
    nums1.sort()
