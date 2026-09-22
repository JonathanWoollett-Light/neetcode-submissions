class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # If `len(nums) < n` then traversing `nums[nums[nums[0]]]` will form a directed graph
        # maybe cycles? unique values can form a cycle, e.g. nums[2,_,0,..]
        # duplicate values force a cycle as 2 pointers point to the same node
        # if all numbers are unique then up to n it forms an arithmetic sequence e.g. (n/2) * (2*1+(n-1)*1)
        # 
        # this problem basically requires knowledge of Floyd's cycle finding algorithm, or deriving it from scratch which seems unlikely
        
        slow = nums[0]
        fast = nums[0]

        # Find the cycle
        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow: break

        # Find the start of the cycle
        # Move slow from the start until it enters the cycle, move fast through the cycle
        slow = nums[0]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow
            

