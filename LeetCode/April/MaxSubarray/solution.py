class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        sub = 0

        for x in nums:
            sub += x
            ans = max(sub, ans)
            sub = max(sub, 0)

        return ans
