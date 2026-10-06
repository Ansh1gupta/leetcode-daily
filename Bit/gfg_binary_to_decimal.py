class Solution:
    def decToBinary(self, n):
        result=""
        while(n>0):
            num=n%2
            if num==0:
                result+="0"
            else:
                result+="1"
            n=n//2
        return(result[::-1])
        