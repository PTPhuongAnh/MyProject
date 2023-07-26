def tich(n):
    kq=1
    for i in n:
        if(int(i)!=0):
            kq*=int(i)
    return kq
    

t=int(input())
while t>0:
    t-=1
    s=input()
    print(tich(s))
    #print("")
