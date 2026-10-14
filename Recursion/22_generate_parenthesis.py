class Solution:
    def solve(self,index,total,arr,result,n):
        if index >= n:
            if total==0:
                result.append("".join(arr))
            return
        if total>n:
            return
        if total<0:
            return
        arr[index]="("
        self.solve(index+1,total+1,arr,result,n)
        arr[index]=")"
        self.solve(index+1,total-1,arr,result,n)
    def generateParenthesis(self, n: int) -> list[str]:
        arr=[""]*(2*n)
        result=[]
        self.solve(0,0,arr,result,2*n)
        return result