
import math


def snt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n,m=[int(x) for x in input().split()]

a=[[0]]*n
x=0
for i in range(n):
    a[i]=[int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if snt(a[i][j]) and a[i][j]>x:
            x=a[i][j]
if x==0:
    print('NOT FOUND')
else:
    print(x)

for i in range(n):
    for j in range(m):
        if a[i][j]==x:
            print('Vi tri [', i, '][', j, ']',sep = '') 