class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer = 0

        for x in nums:
            if x != 0:
                nums[pointer] = x
                pointer += 1
        for i in range(pointer, n):
            nums[i] = 0
