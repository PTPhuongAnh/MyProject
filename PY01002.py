import math
def nt(b):
    a=int(b)
    if a<2:
        return False
    for i in range (2,int(math.sqrt(a)+1)):
        if (a%i==0):
            return False
    return True

def tn(a):
    b=a
    s=b[::-1]
    if(s==a and nt(s)):
        return True
    return False

def tong(a):
    sum=0
    b=int(a)

    while b>0:
        sum+=b%10
        b//=10
    if(nt(sum)):
        return True
    else:
        return False

def cs(a):
    for i in  range(0,len(a)):
        if nt(int(a[i])):
            return True
        return False
t =int(input())
while t>0:
    t-=1
    s=input()
   # print(cs(s))
    if nt(s) and tn(s) and cs(s) :
        print("Yes")
    else:
        print("No")


import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
    
def check(n) :
    m = 0
    s = 0
    x = n
    while n != 0 :
        k = n % 10
        if nto(k) == False : return False
        m = m * 10 + k
        s += k
        n = int(n / 10)
    if nto(s) and nto(x) and nto(m) : return True
    return False
t = int(input())
for i in range(t) :
    n = int(input())
    if check(n) == True : print("Yes")
    else : print("No")