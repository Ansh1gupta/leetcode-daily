class Solution:
    def solve(self,digits,index,subset,result,dict1):
        if index>=len(digits):
            result.append("".join(subset))
            return
        for ch in dict1[digits[index]]:
            subset.append(ch)
            self.solve(digits,index+1,subset,result,dict1)
            subset.pop()
    def letterCombinations(self, digits: str) -> list[str]:
        subset=[]
        result=[]
        dict1={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        self.solve(digits,0,subset,result,dict1)
        return result
        