import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        if n == 0: return 0
        count = 0
        for i in range(int(math.log2(n))+1):
            count += (n >> i) & 1
        return count