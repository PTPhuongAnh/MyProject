def tich(s):
    tich=1
    for i in range(0,len(s),2):
        if(int(s[i])!=0):
            tich*=int(s[i])
    return tich

def tong(s):
    tong=0
    for i in range(1,len(s),2):
        tong+=int(s[i])
    return tong

t=int(input())
while t>0:
    t-=1
    s=input()
    print(tich(s),end=" ")
    print(tong(s))