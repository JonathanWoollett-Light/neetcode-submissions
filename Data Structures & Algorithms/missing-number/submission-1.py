class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum the set and subtract the arithmetic sum
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        