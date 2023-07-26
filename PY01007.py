import math


t=int(input())
while t>0:
    t-=1
    n,x,m=[float(x) for x in input().split()]
    x/=100
    s=math.log(m/n,1+x)
    if s!=int(s):
        s=s+1
    print(int(s))