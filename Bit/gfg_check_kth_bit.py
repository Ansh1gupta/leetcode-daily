class Solution:
    def DecToBin(self,n:int)->str:
        result=""
        while(n>0):
            num=n%2
            if num==0:
                result+=str(0)
            else:
                result+=str(1)
            n=n//2
        return result[::-1]
    def checkKthBit(self, n, k):
        result=self.DecToBin(n)
        if k>=len(result):
            return False
        elif result[-(k+1)]=="1":
            return True
        else:
            return False
        
        