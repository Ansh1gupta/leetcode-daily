class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max1=0
        min1=prices[0]
        for i in prices:
            max1=max(max1,(i-min1))
            if i<min1:
                min1=i
        return max1