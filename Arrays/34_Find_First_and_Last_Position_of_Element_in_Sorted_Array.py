class Solution:
  def lower(self,nums,target):
    l=0
    lb=-1
    r=len(nums)-1
    while(l<=r):
      mid=(l+r)//2
      if (nums[mid]==target):
        lb=mid
        r=mid-1
      elif(nums[mid]>target):
        r=mid-1
      else:
        l=mid+1
    return lb
  def upper(self,nums,target):
    l=0
    r=len(nums)-1
    ub=len(nums)
    while(l<=r):
      mid=(l+r)//2
      if (nums[mid])>target:
        ub=mid
        r=mid-1
      else:
        l=mid+1
    return ub
  def searchRange(self, nums: list[int], target: int) -> list[int]:
        l1=self.lower(nums,target)
        if l1==-1:
          return([-1,-1])
        else:
          l2=self.upper(nums,target)
          return([l1,l2-1])