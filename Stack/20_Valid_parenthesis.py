class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        l=len(s)
        for i in range(l):
            if( (s[i]=="(") or (s[i]=="[") or (s[i]=="{")):
                arr.append(s[i])
            else:
                if s[i]==")":
                    if len(arr)!=0 and arr[-1]=="(":
                        arr.pop()
                    else:
                        return False
                elif s[i]=="]":
                    if  len(arr)!=0 and arr[-1]=="[":
                        arr.pop()
                    else:
                        return False
                elif s[i]=="}":
                    if len(arr)!=0 and arr[-1]=="{":
                        arr.pop()
                    else:
                        return False                
        k=len(arr)
        if k==0:
            return True
        else:
            return False