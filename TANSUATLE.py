t=int(input())
while(t>0):
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    cnt={}
    for i in (a):
        if(i in cnt): cnt[i]+=1
        else: cnt[i]=1

    for i in cnt:
        if(cnt[i]%2==1):
            print(i)
            break