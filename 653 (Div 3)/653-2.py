t= int(input())
for _ in range(t):
    n= int(input())
    count= 0
    while(n!=1):
        if(not(n%6==0 or n%6==3)):
            count= -1
            break
        if(n%6!= 0):
            n*= 2
            count+=1
        else:
            n/= 6
            count+=1
    print(count)