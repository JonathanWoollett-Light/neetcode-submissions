class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        while a < b:
            c = numbers[a] + numbers[b]
            if c == target:
                return [a + 1,b + 1]
            elif c > target:
                b -= 1
            elif c < target:
                a += 1
                
