class Solution:
    def countDaysTogether(self, arriveAlice: str, arriveAlic: str, arriveBob: str, leaveBob: str) -> int:
        dict1=dict()
        dict1[1]=31
        dict1[2]=28
        dict1[3]=31
        dict1[4]=30
        dict1[5]=31
        dict1[6]=30
        dict1[7]=31
        dict1[8]=31
        dict1[9]=30
        dict1[10]=31
        dict1[11]=30
        dict1[12]=31
        am1=int(arriveAlice[:2])
        am2=int(arriveBob[:2])
        ad2=int(arriveBob[3:5])
        ad1=int(arriveAlice[3:5])
        lm1=int(arriveAlic[:2])
        ld1=int(arriveAlic[3:5])
        lm2=int(leaveBob[:2])
        ld2=int(leaveBob[3:5])
        ans=[]
        days=0
        if am1==am2:
            cam=am1
            cad=max(ad1,ad2)
        else:
            if am1>am2:
                cam=am1
                cad=ad1
            else:
                cam=am2
                cad=ad2
        if lm1==lm2:
            clm=lm1
            cld=min(ld1,ld2)
        else:
            if lm1<lm2:
                clm=lm1
                cld=ld1
            else:
                clm=lm2
                cld=ld2
        i=cam
        while(i<=clm):
            ans.append(i)
            i+=1
        for j in ans:
            days+=dict1[j]
        days-=cad-1
        days-=dict1[clm]
        days+=cld
        if days<0:
            return 0
        else:
            return days
        
