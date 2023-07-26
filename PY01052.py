import math


def snt(n):
    if(n<2):
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return 1

def check(m):
    tong=0
    for i in m:
        tong+=int(i)
    if(snt(tong))==1:
        return 1
    return 0

t=int(input())
while t>0:
    t-=1
    s=input()
    if check(s)==1:
        print("YES")
    else:
        print("NO")
