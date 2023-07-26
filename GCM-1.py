import math


n=int(input())
a=[int(x) for x in input().split()]
max=1
for i in range(n):
    for j in range(i+1,n):
        k=math.gcd(a[i],a[j])
        if max<k:
            max=k
print(max)