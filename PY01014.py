
import math
def Tong(a):
    sum=0
    while(a>0):
        sum+=a%10
        a=a//10
    return sum
def CS(a):
    for i in range(0,len(a)-2):
       if int(a[i])>int(a[i+1]):
        return False
    return True
t=int(input())
while t>0:
    t-=1
    s=input()
    if(CS(s) ):
        print("YES")
    else:
        print("NO")
    


