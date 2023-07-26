n,m=[int(x) for x in input().split()]
x=0
y=10**6
ok=0
a=[[0]]*n
for i in range(n):
    a[i]=[int(x) for x in input().split()]

for i in range(n):
    for j in range(m):
        if(a[i][j]>x):
            x=a[i][j]

for i in range(n):
    for j in range(m):
        if(a[i][j]<y):
            y=a[i][j]

for i in range(n):
    for j in range(m):
        if(a[i][j]==x-y):
            ok=1

if ok==0:
    print('NOT FOUND')
else:
    print(x-y)
for i in range(n):
    for j in range(m):
        if(a[i][j]==x-y):
            print('Vi tri [',i,'][',j,']',sep='')