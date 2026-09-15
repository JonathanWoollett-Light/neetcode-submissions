def fib_pair(k):  # returns (F(k), F(k+1))
    if k == 0: return 0, 1
    a, b = fib_pair(k // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    return (d, c + d) if k % 2 else (c, d)

class Solution:
    def climbStairs(self, n: int) -> int:
        return fib_pair(n+1)[0]