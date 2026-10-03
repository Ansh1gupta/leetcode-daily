class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)//2
            if nums[mid]==target:
                return True
            elif nums[mid]==nums[l]==nums[h]:
                l+=1
                h-=1
            elif nums[mid]>=nums[l]:
                if nums[mid]>=target>=nums[l]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1    
        return False
