class Solution:
    def solve(self,candidates,target,index,total,subset,result):
        if index>=len(candidates):
            if total==target:
                result.append(subset.copy())
            return
        if total==target:
            result.append(subset.copy())
            return
        if total>target:
            return
        subset.append(candidates[index])
        sum1=total+candidates[index]
        self.solve(candidates,target,index,sum1,subset,result)
        subset.pop()
        self.solve(candidates,target,index+1,total,subset,result)
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        subset=[]
        self.solve(candidates,target,0,0,subset,result)
        return result