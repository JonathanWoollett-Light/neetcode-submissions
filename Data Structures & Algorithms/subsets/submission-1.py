class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [(i, (x,)) for i, x in enumerate(nums)]
        covered = set([tuple([])])
        while(stack):
            i, x = stack.pop()
            # print(f"x: ({i}){x}")
            covered.add(x)

            for j in range(i+1,len(nums)):
                y = (*x, nums[j])
                # print(f"y: ({j}){y}")
                if y not in covered:
                    stack.append((j,y))
        return [list(x) for x in covered]
                
        