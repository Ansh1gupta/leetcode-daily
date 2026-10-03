class Solution:
    def findMin(self, nums: list[int]) -> int:
        min1=float("inf")
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)//2
            min1=min(min1,nums[mid])
            if nums[mid]<=nums[h]:
                h=mid-1
            else:
                if nums[l]<=nums[h]:
                    min1=min(min1,nums[l])
                    break
                else:
                    l=mid+1
        return min1

        