class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        characters = set()
        for i in range(len(s)):
            while s[i] in characters:
                characters.remove(s[start])
                start += 1
            characters.add(s[i])
            longest = max(longest, i - start + 1)
        return longest
