class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l1=len(nums)
        l=0
        r=0
        zeroes=0
        max1=0
        while r<l1:
            if nums[r]==0:
                zeroes+=1
            while zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            max1=max((r-l+1),max1)
            r+=1
        return max1