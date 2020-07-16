# def gcd(a, b):
#     if a< b:
#         return gcd(b, a)
#     while b != 0:
#         (a, b)= (b, a%b)
#     return a

t= int(input())
for _ in range(t):
    n= int(input())
    if(n%2==0):
        print(int(n/2))
    else:
        print(int((n-1)/2))