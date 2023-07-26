def tn(n):
    n=str(n)
    if len(n)>1 and n==n[::-1]:
        return True
    return False

n,m=[int(x) for x in input().split()]
a=[[0]]*n
x=0
for i in range(n):
    a[i]=[int(x) for x in input().split()]

for i in range(n):
    for j in range(m):
        if tn(a[i][j]) and (a[i][j])>x:
            x=a[i][j]

if x==0:
    print('NOT FOUND')
else:
    print(x)

for i in range(n):
    for j in range(m):
        if(a[i][j]==x):
            print('Vi tri [',i,'][',j,']',sep='')
