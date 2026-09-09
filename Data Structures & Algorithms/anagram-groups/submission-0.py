OFFSET = 97
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Set annagram hashsets
        n = len(strs)
        csets = [[0 for _ in range(26)] for _ in range(n)]
        for i, string in enumerate(strs):
            for c in string:
                csets[i][ord(c) - OFFSET] += 1
        # Compare all strings to annagrams
        result = [[strs[i]] for i in range(n)]
        skip = set()
        for i in range(n):
            if i in skip:
                continue
            for j in range(n):
                if i == j:
                    continue
                if csets[i] == csets[j]:
                    result[i].append(strs[j])
                    skip.add(j)
        return [r for i,r in enumerate(result) if i not in skip]
