class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for x in nums:
            i ^= x
        return i
