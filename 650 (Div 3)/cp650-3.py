t= int(input())
for _ in range(t):
    tables, dist= list(map(int, input().split()))
    s= str(input())
    ans= 0
    tInd= [x for x in range(len(s)) if s[x]=='1']
    if(len(tInd)==0):
        ans= ((tables-1)//(dist+1))+ 1
        print(ans)
        continue
    else:
        if(tInd[0]!= 0 and (tInd[0]-dist)>=1):
            ans+= ((tInd[0]- dist)- 1)//(dist+1) + 1
        if(tInd[-1]!= len(s)-1 and (tables-1-tInd[-1])-dist>=1):
            ans+= ((tables-1-tInd[-1]-dist)- 1)//(dist+1) + 1
        if(len(tInd)>1):
            for i in range(len(tInd)-1):
                i1= tInd[i]
                i2= tInd[i+1]
                ans+= ((i2-i1-1-(2*dist))-1)//(dist+1) + 1
        print(ans)