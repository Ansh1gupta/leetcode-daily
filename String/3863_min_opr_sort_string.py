class Solution:
    def minOperations(self, s: str) -> int:
        if list(s) == sorted(s):
            return 0
        min1=min(s)
        max1=max(s)
        if s[0] == min1 or s[-1]==max1:
            return 1
        l=len(s)
        if l == 2 and s[1] < s[0]:
            return -1
        for i in range(1,l-1):
            if s[i]==min1 or s[i]==max1:
                return 2
        return 3