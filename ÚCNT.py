


import math
def check(a):
    if a<2: return False
    for k in range(2,a):
        if a%k==0: return False
    return True
def total(a):
    tong=0
    while a>0:
        tong+=a%10
        a//=10
    return tong
a=int(input())
while a>0:
    a-=1
    x,y=map(int,input().split())
    
    ucln=math.gcd(x,y)
    
    
    if check(total(ucln))==True:
        print("YES")
    else:
        print("NO")