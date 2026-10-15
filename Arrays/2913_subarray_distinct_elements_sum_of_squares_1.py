class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            set1=set()
            for j in range(i,n):
                set1.add(nums[j])
                count+=(len(set1)**2)
        return count
                