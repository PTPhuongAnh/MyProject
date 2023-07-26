n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
d=[0]*n
maxx=-1
ok=0
res=-1
ln=-1
for i in a:
    d[i]+=1

for i in range(1,n+1):
        maxx=max(d[a[i]],maxx)

for i in range(1,n+1):
    if d[i]!=maxx:
        ln=max(ln,d[a[i]])
        res=a[i]
        ok=1
if ok==0:
    print("NONE")
else:
    print(res)
    
