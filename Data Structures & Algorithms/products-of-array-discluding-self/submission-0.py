class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]
        for i in range(len(nums) - 1):
            prods.append(nums[i] * prods[i])
        postfix = 1
        for i in reversed(range(len(nums))):
            prods[i] *= postfix
            postfix *= nums[i]
        return prods