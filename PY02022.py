import math


def snt(n):
    if int(n)<2:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if int(n)%i==0:
            return False
    return True

t=int(input())
a=[int(x) for x in input().split()]
b=[]
c=[0]*1000001
for i in a:
    if(snt(i)):
        b.append(i)
for i in b:
    c[i]+=1

for i in b:
    if(c[i]!=0):
        print(i,c[i])
        c[i]=0
