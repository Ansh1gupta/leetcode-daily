class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        dict1=dict()
        l1=len(fruits)
        l=0
        r=0
        count=0
        while r<l1:
            dict1[fruits[r]]=dict1.get(fruits[r],0)+1
            while len(dict1)>2:
                dict1[fruits[l]]-=1
                if dict1[fruits[l]]==0:
                    del dict1[fruits[l]]
                l+=1
            if len(dict1)<=2:
                count=max(count,(r-l+1))
                r+=1
        return count
            
                