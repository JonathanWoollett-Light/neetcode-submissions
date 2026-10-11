import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        # 1,0,1,0 = 10, log2(10) = 3 
        # 0,0,1,0 = 2, log2(1) = 1
        output = [0]
        for i in range(1, n+1):
            count = 0
            while(i > 0):
                i &= ~(1<<int(math.log2(i)))
                count += 1
            output.append(count)
        return output