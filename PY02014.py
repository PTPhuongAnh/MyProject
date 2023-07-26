import math


a=[True]*10001
b=[]
a[0]=a[1]=False
for i in range(2,int(math.sqrt(10001))+1):
        if(a[i]):
            for j in range(i*i,10001,i):
                a[j]=False
            b.append(i)
n=int(input())
ans=0
c=[int(x) for x in input().split()]
for i in c:
    s=10**9
    for j in b:
        s=min(s,abs(i-j))
    ans=max(ans,s)
print(ans)
