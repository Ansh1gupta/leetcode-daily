
class Solution:
    def solve(self, n):
        sum1 = 0
        while n > 0:
            d = n % 10
            sum1 += d
            n //= 10
        return sum1

    def minSwaps(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            arr.append((self.solve(i), i))

        sorted_arr = sorted(arr)
        count = 0
        pos = {value: i for i, value in enumerate(arr)}

        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                count += 1
                j = pos[sorted_arr[i]]

                pos[arr[i]] = j
                pos[arr[j]] = i
                arr[i], arr[j] = arr[j], arr[i]

        return count
