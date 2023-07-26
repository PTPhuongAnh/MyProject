import math


n,k=[int(x) for x in input().split()] 
dem=0
for i in range(10**(k-1),10**k):
    if(math.gcd(i,n)==1):
        dem+=1
        print(i,end=' ')
    if dem==10:
      print()
      dem=0