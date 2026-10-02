class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index=len(nums)
        r=index-1
        l=0
        while(l<=r):
            mid=(l+r)//2
            if target<=nums[mid]:
                index=mid
                r=mid-1
            else:
                l=mid+1
        return index
