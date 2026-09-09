from itertools import chain
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = {c: 0 for c in chain(s,t)}
        for c in s:
            hashset[c] += 1
        for c in t:
            hashset[c] -= 1
        return all([v == 0 for v in hashset.values()])
