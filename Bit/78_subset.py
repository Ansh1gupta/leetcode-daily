class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        l=len(nums)
        result=[]
        index=2**l
        for i in range(index):
            ls=[]
            for j in range(l):
                if (i & (1<<j))!=0:
                    ls.append(nums[j])
            result.append(ls)
        return result
        

