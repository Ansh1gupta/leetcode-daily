class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        l=len(nums)
        ans=[-1]*l
        stack=[]
        for i in range(l-1,-1,-1):
            stack.append(nums[i])
        for i in range(l-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums[i])
        return ans
        