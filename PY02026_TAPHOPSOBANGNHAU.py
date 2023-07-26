n,m=[int(x) for x in input().split()]
a={int(x) for x in input().split()}
b={int(x) for x in input().split()}

a=sorted(a)
b=sorted(b)
ok=0
for i in a:
    if not(i in b):
        ok=1
if ok==0:
    print('YES')
else:
    print('NO')
    