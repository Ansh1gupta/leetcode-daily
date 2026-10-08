class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr=[]
        arr1=[]
        str1=""
        l=len(s)
        for i in range(l):
            if s[i]=="(":
                if len(arr)==0:
                    arr.append(s[i])
                else:
                    arr1.append(s[i])
                    str1+=s[i]
            elif s[i]==")":
                if len(arr1)==0:
                    arr.pop()
                else:
                     arr1.pop()
                     str1+=s[i]
        return str1
            