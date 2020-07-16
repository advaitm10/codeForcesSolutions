t= int(input())
for _ in range(t):
    x, y, n= list(map(int, input().split()))
    ans= (x)*(n//x)+y
    while(ans>n):
        ans-=x
    print('*', ans) 