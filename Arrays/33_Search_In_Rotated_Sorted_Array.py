class Solution:
    def binary(self,nums,target,l,h):
        if l>h:
            return -1
        else:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:
                if nums[mid]>=target>=nums[l]:
                    return self.binary(nums,target,l,mid-1)
                else:
                    return self.binary(nums,target,mid+1,h)
            else:
                if nums[mid]<=target<=nums[h]:
                    return self.binary(nums,target,mid+1,h)
                else:
                    return self.binary(nums,target,l,mid-1)
    def search(self, nums: list[int], target: int) -> int:
        h=len(nums)-1
        index=self.binary(nums,target,0,h)
        return index
        