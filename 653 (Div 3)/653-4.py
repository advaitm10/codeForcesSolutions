def check(l, k):
    for i in l:
        if(i%k!=0):
            return False
    return True

t= int(input())
for _ in range(t):
    n, k= list(map(int, input().split()))
    a= list(map(int, input().split()))
    d= dict()

    if(check(a, k)):
        print(0)
        continue

    for i in a:
        if(i%k!=0):
            d[k-i%k]= d.get(k-i%k, 0) + 1

    maxrep= 0
    reps= 0

    for x,y in d.items():
        if(y==reps and x>maxrep):
            maxrep= x
        elif(y>reps):
            reps= y
            maxrep= x

    print((reps-1)*k+maxrep+1)