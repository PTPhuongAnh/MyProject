def tong(s):
    tong=0
    for i in range(0,len(s),2):
        tong+=int(s[i])
    return tong

def tich(s):
    tich=1
    tong=0
    for i in range(1,len(s),2):
        tong+=int(s[i])
    if(tong==0): return 0
    else:
        for i in range(1,len(s),2):
            if(int(s[i])!=0):
                tich*=int(s[i])
    return tich


t=int(input())
while t>0:
    t-=1
    s=input()
    print(tong(s),end=' ')
    print(tich(s))
