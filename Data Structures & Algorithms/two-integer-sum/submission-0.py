class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashset:
                return [hashset[diff], i]
            hashset[num] = i