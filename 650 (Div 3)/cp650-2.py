#Input
t= int(input())
inList= []
for temp in range(t):
    crap= input()
    inList.append(list(map(int, input().split())))

#Func
def solve(inList):
    count= 0
    moves= 0
    rList= inList
    for i in rList:
        if(i%2!=count%2):
            for j in range(len(rList)):
                if(j!= count and rList[j]%2!= rList[count]%2):
                    if((j%2!= rList[j]%2) and rList[j]%2==count%2):
                        temp= rList[j]
                        rList[j]= rList[count]
                        rList[count]= temp
                        moves+=1
        count+=1
    count2= 0
    for k in rList:
        if(k%2!=count2%2):
            return -1
        count2+=1
    return moves

#Main
for i in inList:
    print(solve(i))