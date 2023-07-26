import math
def snt(s):
   if(int(s)<2):
    return 0
    for i in range(2,int(math.sqrt(s)+1)):
        if s%i==0:
            return 0
    return 1

def kiemtra(s):
    tong=0
    for i in s:
        tong+=int(i)
    if(snt(str(tong))==0):
        return 0
    else:
        for i in range(0,len(s)):
            if(int(i)%2==0):
                if(int(s[i])%2!=0):
                    return 0
            else:
                if(int(s[i])%2==0):
                    return 0
    return 1
                
            

t=int(input())
while t>0:
    t-=1
    a=input()
    if(kiemtra(a)==1):
        print("YES")
    else:
        print("NO")