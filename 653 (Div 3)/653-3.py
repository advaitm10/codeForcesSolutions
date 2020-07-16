def check(l):
    evens= 0
    odds= 0
    for i in l:
        if(i=='('):
            evens+=1
        else:
            odds+=1
        if(odds>evens):
            return False
    return True

def findBadBrack(l):
    evens= 0
    odds= 0
    for i in range(len(l)-1, -1, -1):
        if(l[i]=='('):
            evens+=1
        else:
            odds+=1
        if(evens>odds):
            return i

t= int(input())
for _ in range(t):
    crap= input()
    seq= list(input())
    count= 0
    while(not check(seq)):
        index= findBadBrack(seq)
        seq.pop(index)
        seq.insert(0, '(')
        count+=1
    print('*',count)