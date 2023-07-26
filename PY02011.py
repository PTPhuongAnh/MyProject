import functools


def cmp(a,b):
    if(a<b):
        return 1
    else:
        return -1
t=int(input())
#a=[int(x) for x in input().split()]
a=[]
b=[]
c=[]
d=[0]*t
while True:
 x=[int(x) for x in input().split()]
 a+=x
 if len(a)==t:
    break
#b=[]
for i in range (t):
        if a[i]%2==1:
            b.append(a[i])
            d[i]=1
        else:
            c.append(a[i])
    
b=sorted(b)
c=sorted(c,key=functools.cmp_to_key(cmp))
for i in range(t):
        if d[i]==1:
            print(b[-1],end=" ")
            b.pop()
        else:
            print(c[-1],end=" ")
            c.pop()

    