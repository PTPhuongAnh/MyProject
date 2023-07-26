import math


a=[True] * 10001
def sang():
    a[0]=a[1]=False
    for i in range(2,int(math.sqrt(10001))+1):
        if(a[i]):
            for j in range(i*i,10001,i):
                a[j]=False

n,x=[int(x) for x in input().split()]
sang()
b=[]
cnt=x
for i in range(2,10001):
    if a[i]:
       b.append(i)
    if len(b)==n:
        break

print(x)
for i in b:
    x += i
    print(x, end = ' ')
    


