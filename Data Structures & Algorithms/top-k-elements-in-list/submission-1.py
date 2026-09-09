class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Number of occurences to number
        freq = [[] for _ in range(len(nums))]

        # Number to number of occurences
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        for key,value in counts.items():
            freq[value-1].append(key)
        
        # Get the result
        res = []
        for f in reversed(freq):
            res += f
            if len(res) >= k:
                break
        return res[:k]