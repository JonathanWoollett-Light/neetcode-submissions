class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Range start -> Range end
        lower_bounds = {}
        # Range end -> Range start
        upper_bounds = {}
        # Lenght of longest range
        length = 0
        # Set of discovered elements
        duplicates = set()
        for num in nums:
            # Skip duplicates
            if num in duplicates:
                continue
            duplicates.add(num)
            
            start = num + 1
            end = num - 1
            match (start in lower_bounds, end in upper_bounds):
                # In this case we are joining 2 sequences.
                case (True, True):
                    lower = upper_bounds[end]
                    upper = lower_bounds[start]
                    lower_bounds[lower] = upper # Update lower
                    upper_bounds[upper] = lower # Update upper
                    length = max(length, upper - lower + 1) # Update max length
                    continue
                # In this case we are decrementing a sequences lower bound
                case (True, False):
                    upper = lower_bounds[start] # Get upper bound
                    lower_bounds[num] = upper # Add new lower bound
                    upper_bounds[upper] = num # Update upper bound to point to new lower bound
                    length = max(length, upper - num + 1) # Update max length
                    continue
                # In this case we are incrementing a sequences upper bound
                case (False,True):
                    lower = upper_bounds[end] # Get lower bound
                    upper_bounds[num] = lower # Add new upper bound
                    lower_bounds[lower] = num # Update lower bound to point to new upper bound
                    length = max(length, num - lower + 1) # Update max length
                    continue
                case (False,False):
                    upper_bounds[num] = num
                    lower_bounds[num] = num
                    length = max(length, 1)
                    continue
        return length