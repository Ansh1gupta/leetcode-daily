class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        l = len(nums)
        arr = [0] * l

        p = 0
        n = 1

        for i in range(l):
            if nums[i] < 0:
                arr[n] = nums[i]
                n += 2
            else:
                arr[p] = nums[i]
                p += 2

        return arr