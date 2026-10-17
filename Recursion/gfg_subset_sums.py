class Solution:
    def solve(self,arr,index,subset,result,n):
        if index>=n:
            sum2=sum(subset)
            result.append(sum2)
            return
        subset.append(arr[index])
        self.solve(arr,index+1,subset,result,n)
        subset.pop()
        self.solve(arr,index+1,subset,result,n)
	def subsetSums(self, arr):
		result=[]
		subset=[]
		n=len(arr)
		self.solve(arr,0,subset,result,n)
		return result
		