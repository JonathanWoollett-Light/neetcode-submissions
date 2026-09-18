import bisect

class Solution:
    # n log n
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort() # n log n
        while (len(stones) > 1):
            stones, [lower,upper] = stones[:-2], stones[-2:]
            if upper > lower:
                val = upper - lower
                indx = bisect.bisect_left(stones, val) # log n
                stones.insert(indx,val)
        return stones[0] if (stones) else 0