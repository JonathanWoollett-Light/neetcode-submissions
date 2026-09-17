class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totals = [0,0]
        for i in range(0,len(cost)-1):
            totals.append(min(totals[-1]+cost[i+1],totals[-2]+cost[i]))
        # print(totals)
        return totals[-1]
        # ->n = min(cost[n-1], cost[n-2])
        # ->n+1 = min(cost[n], cost[n-1])