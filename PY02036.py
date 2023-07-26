import math


n=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
for i in a:
    for j in a:
        if(i<j and math.gcd(i,j)==1):
            print(i,j)