class Solution:
    def nextLargerElement(self, arr):
        l=len(arr)
        ans=[-1]*l
        stack=[]
        for i in range(l-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans
        