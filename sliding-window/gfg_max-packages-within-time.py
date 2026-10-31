class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        l=0
        r=0
        count=0
        temp=0
        l1=len(arr)
        while r<l1:
            if totalTime!=0:
                temp+=arr[r]
                r+=1
                totalTime-=1
                count=max(count,temp)
            else:
                temp-=arr[l]
                l+=1
                totalTime+=1
        return count