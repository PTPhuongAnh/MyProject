import math


def pt(n):
   # dem=0
    print("1",end='')
    for i in range(2,int(math.sqrt(n))+1):
        dem=0
        while n%i==0:
            dem+=1
            n=n/i
        if dem!=0:
          print(" * ",str(i)+ "^"+str(dem),end='')
    if n!=1:
        print(" * " + str(int(n)) + "^1",end='')
    print()

        
t=int(input())
while t>0:
    t-=1
    n=int(input())
    pt(n)
