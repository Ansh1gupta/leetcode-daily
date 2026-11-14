class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        count=0
        middle=nums[mid]
        for i in nums:
            count+=abs(middle-i)
        return count