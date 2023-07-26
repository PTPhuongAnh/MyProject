import math


def snt(s):
    if((s)<2):
        return 0
    for i in range(2,int(math.sqrt(int(s)))+1):
        if (s)%i==0:
            return 0
    return 1

def kiemtra(s):
    for i in range(0,len(s)):
        if snt(i)!=snt(int(s[i])):
            return 0
    return 1

t=int(input())
while t>0:
    t-=1
    s=input()
    if(kiemtra(s)==1):
        print("YES")
    else:
        print("NO")            
