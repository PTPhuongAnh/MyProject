import math


def snt(n):
    if(n<2): return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=[int(x) for x in input().split()]
b=[]
c=[]
d=[0]*n
for i in a:
    if(snt(i)):
        b.append(i)
    else:
        c.append(i)

b=sorted(b)
for i in b:
    d[i]=1
g,h=0,0
for i in range(n):
    if d[i]==1:
        print(b[g],end=' ')
        g+=1
    else:
        print(c[h],end=' ')
        h+=1


