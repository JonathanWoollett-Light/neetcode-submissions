import bisect

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        items = []
        stack = [(0,target,[])]
        while stack:
            start, remaining, combo = stack.pop()
            if remaining == 0:
                items.append(combo)
                continue
            for i in range(start, len(nums)):
                if nums[i] > remaining: break
                stack.append((i, remaining - nums[i], combo + [nums[i]]))
        return items
