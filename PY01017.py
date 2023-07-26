
import math
def nt(b):
    a=int(b)
    if a<2:
        return False
    for i in range (2,int(math.sqrt(a))+1):
        if (a%i==0):
            return False
    return True

def tn(a):
    b=a
    s=b[::-1]
    if(s==a ):
        return True
    return False

def tong(a):
    if(len(a)%2==0):
        return True
    else:
        return False

def cs(b):
    a=int(b)
    for i in  range(0,len(a)):
        if int(a[i])==0 or int(a[i])==2 or int(a[i])==4 or int(a[i])==6 or int(a[i])==8:
            return True
    return False
t =int(input())
while t>0:
    t-=1
    s=int(input())
    for i in range(0,s):
      if tn(i)  and cs(i):
        print(i,end=' ')