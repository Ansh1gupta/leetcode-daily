class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        result=float("inf")
        total=0
        l=len(arr)
        for i in arr:
            total+=i
            result=min(result,total)
            if total>0:
                total=0
        return result
       
            
                
                
                
