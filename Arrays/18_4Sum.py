class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        set1=set()
        arr=sorted(nums)
        result=[]
        l=len(nums)
        temp=0
        for i in range(l):
            if i!=0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1,l):
                if j !=i+1 and arr[j]==arr[j-1]:
                    continue
                k=j+1
                p=l-1
                while(k<p):
                    temp = (arr[i]+arr[j]+arr[k]+arr[p])
                    if temp>target:
                        p-=1
                    elif temp<target:
                        k+=1
                    else:
                        temp1=[arr[i],arr[j],arr[k],arr[p]]
                        set1.add(tuple(temp1))
                        k+=1
                        p-=1
                        while(k<p and arr[k]==arr[k-1]):
                            k+=1
                        while(k<p and arr[p]==arr[p+1]):
                            p-=1
        for i in set1:
            result.append(list(i))
        return result
