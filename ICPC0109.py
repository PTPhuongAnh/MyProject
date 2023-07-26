
import math


t=int(input())
while t>0:
    t-=1
    n=int(input())
    b=[int(x) for x in input().split()]
    a=[]
    cnt=[0]*1000001
    abc=-10
    ok=0
    for i in b:
      a.append(i)
        
    for i in a:
        cnt[i]+=1
        abc=max(cnt[i],abc)

    for i in range(1000001): 
        if(cnt[i]==abc and cnt[i]>int(n/2)):
            print(i)
            ok=1
            break
    if(ok==0):
        print("NO")
        
            
    
