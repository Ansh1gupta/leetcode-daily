class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result=x^y
        count=0
        for i in range(32):
            if (result & (1<<i))!=0:
                count+=1
        return count