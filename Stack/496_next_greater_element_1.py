class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        dict1=dict()
        l=len(nums2)
        for i in range(l-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                dict1[nums2[i]]=stack[-1]
            else:
                dict1[nums2[i]]=-1
            stack.append(nums2[i])
        l2=len(nums1)
        ans=[]
        for i in nums1:
            ans.append(dict1[i])
        return ans
        
