t= int(input())
for _ in range(t):
    n= int(input())
    a= list(map(int, input().split()))
    count= 0
    for i in range(len(a)):
        for j in range(len(a)):
            if(i!=j and count<(n-1)):
                if(a[i]== 0 or a[j]==0):
                    continue
                if((a[i]+a[j])%2==0):
                    print(i+1, j+1)
                    a[i], a[j]= [0, 0]
                    count+=1