#Take inputs
t= int(input())
bList= []
for temp in range(t):
    bList.append(str(input()))

#Function
def solve(inString):
    temp= ''
    for k in range(0, len(inString), 2):
        sub= inString[k:k+2]
        if(k< len(inString)-2):
            temp+= sub[0]
        else:
            temp+=sub
    return temp


#Main
for i in bList:
    print(solve(i))