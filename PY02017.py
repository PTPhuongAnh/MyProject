t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[0]*1000001
    for i in a:
        b[i]+=1
    for i in a:
        if(b[i]!=0 and b[i]%2!=0):
            print(i)
        b[i]=0