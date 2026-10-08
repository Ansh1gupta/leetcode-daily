class Solution:
    def solve(self,index,subset,result,s):
        if index>=len(s):
            if subset:
                result.append("".join(subset))
            return result
        subset.append(s[index])
        self.solve(index+1,subset,result,s)
        subset.pop()
        self.solve(index+1,subset,result,s)
    def powerSet(self, s):
        subset=[]
        result=[]
        self.solve(0,subset,result,s)
        return result
       