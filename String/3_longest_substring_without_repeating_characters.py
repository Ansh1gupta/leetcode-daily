class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1=len(s)
        dict1=dict()
        l=0
        r=0
        max1=0
        while l<l1 and r<l1:
            if s[r] not in dict1:
                dict1[s[r]]=r
                max1=max(max1,(r-l+1))
                r+=1
            else:
                if l>dict1[s[r]]:
                    dict1[s[r]]=r
                    max1=max(max1,(r-l+1))
                    r+=1
                else:
                    l=dict1[s[r]]+1
                    dict1[s[r]]=r
                    max1=max(max1,(r-l+1))
                    r+=1
        return max1