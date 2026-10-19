class Solution:
    def solve(self,arr,index,k,n,total,result,subset):
        if total==n and len(subset)==k:
            result.add(tuple(sorted(subset)))
            return
        if total>n:
            return
        if index>=9:
            if total==n and len(subset)==k:
                result.add(tuple(sorted(subset)))
            return
        subset.append(arr[index])
        self.solve(arr,index+1,k,n,total+arr[index],result,subset)
        subset.pop()
        self.solve(arr,index+1,k,n,total,result,subset)
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr=[1,2,3,4,5,6,7,8,9]
        result=set()
        subset=[]
        self.solve(arr,0,k,n,0,result,subset)
        output=[]
        for i in result:
            output.append(list(i))
        return output
        