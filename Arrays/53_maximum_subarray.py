class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max1 = float("-inf")
        total = 0
        l = len(nums)
        i = 0

        while i < l:
            total += nums[i]
            max1 = max(max1, total)

            if total < 0:
                total = 0

            i += 1

        return max1