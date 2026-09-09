# [1,2,3]
#  0 1 2
# -3-2-1


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = [-1000-i for i in range(k)]
        self.nums = nums
        for x in nums:
            for i in reversed(range(k)):
                if x > self.kth[i]:
                    self.kth.insert(i+1,x)
                    self.kth.pop(0)
                    break

    def add(self, val: int) -> int:
        self.nums.append(val)
        for i in reversed(range(len(self.kth))):
            if val > self.kth[i]:
                self.kth.insert(i+1,val)
                self.kth.pop(0)
                break
        return self.kth[0]
