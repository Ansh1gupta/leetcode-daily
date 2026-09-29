class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set1=set()
        longest=0
        count=0
        for i in nums:
            set1.add(i)
        for i in set1:
            if i-1 not in set1:
                count=1
                u=i
                while u+1 in set1:
                    count+=1
                    u+=1
                longest=max(longest,count)
        return longest
        
        