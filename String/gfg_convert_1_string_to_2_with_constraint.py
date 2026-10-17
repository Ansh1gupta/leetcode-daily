class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        dict1=dict()
        dict2=dict()
        l1=len(s1)
        l2=len(s2)
        if l1!=l2:
            return False
        for i in range(l1):
            if s1[i]=="A" or s1[i]=="B":
                dict1[i]=s1[i]
        for j in range(l2):
            if s2[j]=="A" or s2[j]=="B":
                dict2[j]=s2[j]
        for (key1,value1),(key2,value2) in zip(dict1.items(),dict2.items()):
            if value1!=value2:
                return False
            if value1==value2=="A":
                if key1<key2:
                    return False
            if value1==value2=="B":
                if key1>key2:
                    return False
        return True
                
        
 