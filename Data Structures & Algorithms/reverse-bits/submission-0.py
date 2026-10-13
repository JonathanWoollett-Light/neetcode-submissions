def reverse(n: int, bits: int = 32) -> int:
    if bits == 0: return 0
    # Take the lowest bit, move it to the mirrored position,
    # then recurse on the remaining higher bits.
    return ((n & 1) << (bits - 1)) | reverse(n >> 1, bits - 1)

class Solution:
    def reverseBits(self, n: int) -> int:
        return reverse(n)