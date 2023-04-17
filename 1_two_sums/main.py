from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for first_idx, num in enumerate(nums):
        for second_num in nums[first_idx+1:]:
            if num + second_num == target:
                return [first_idx, nums.index(second_num, first_idx+1)]
            
def twoSum_2(nums: List[int], target: int) -> List[int]:
    numbers_map = {num: idx for idx, num in enumerate(nums)}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in numbers_map and numbers_map[diff] != idx:
            return [idx, numbers_map[diff]]

