class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result=[]
        l=len(nums)
        for i in range(l):
            if nums[i]==target:
                result.append(i)
        return result