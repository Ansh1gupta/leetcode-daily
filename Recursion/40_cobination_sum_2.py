class Solution:
    def solve(self,index,total,subset,result,candidates,n):
        if index>=n:
            if total==0:
                result.append(subset.copy())
            return
        if total==0:
            result.append(subset.copy())
            return 
        if total<0:
            return
        for i in range(index,n):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            else:
                subset.append(candidates[i])
                sum1=total-candidates[i]
                self.solve(i+1,sum1,subset,result,candidates,n)
                subset.pop()
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        subset=[]
        candidates.sort()
        l=len(candidates)
        self.solve(0,target,subset,result,candidates,l)
        return result
 """
    Approach:
    1. Sort the candidates array to bring duplicate elements together.
    2. Use recursion and backtracking to generate combinations.
    3. If total becomes 0, store a copy of the current subset.
    4. If total becomes negative, stop exploring that path.
    5. Skip duplicate candidates at the same recursion level
       to avoid generating duplicate combinations.
    6. Use index + 1 in recursion so each candidate is used
       at most once.
    7. Backtrack by removing the last element after recursion.

    Time Complexity: O(2^n * n)
    - There can be O(2^n) possible subsets.
    - Copying a subset can take O(n) time.
    - Sorting takes O(n log n) time.

    Space Complexity: O(n) auxiliary space for the recursion
    stack and current subset, excluding the output.
 """