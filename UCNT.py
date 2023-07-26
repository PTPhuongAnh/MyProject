import math


def gcd(a,b):
    if b==0:
        return 1
    return gcd(b,a%b)

def nto(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n+1))):
        if(n%i==0):
            return False
    return True
def tong(n):
    kq=0
    while n>0:
        kq+=int(n)%10
        n/=10
    return kq

def kq(a,b):
    if(nto(tong(gcd(a,b)))):
        return True
    else:
        return False
t=int(input())
while t>0:
    t-=1
    a=int(input())
    b=int(input())
    if(kq(a,b)):
        print("YES")
    else:
        print("NO")
    
