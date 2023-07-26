import math


def snt(s):
    if(int(s)<2):
        return 0
    for i in range(2,int(math.sqrt(int(s)))+1):
        if int(s)%i==0:
            return 0
    return 1

def kq(s):
    s=s[::-1]
    res=""
    for i in range(0,4):
        res+=s[i]
    res=res[::-1]
    if(snt(res)):
        return 1
    else:
        return 0
    
t=int(input())
while t>0:
    t-=1
    s=input()
    if(kq(s)):
        print("YES")
    else:
        print("NO")