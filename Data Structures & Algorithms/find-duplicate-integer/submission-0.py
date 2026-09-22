class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = dict([(i,False) for i in range(1,10_000+1)])
        for num in nums:
            if temp[num]: return num
            temp[num] = True