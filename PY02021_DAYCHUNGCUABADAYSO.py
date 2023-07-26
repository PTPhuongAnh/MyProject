def kq():
    n,m,p=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    i,j,k=0,0,0
    ok=0
    while i<n and j<m and k<p:
        if a[i]==b[j] and b[j]==c[k]:
            print(a[i],end='')
            i+=1
            j+=1
            k+=1
            ok=1
            continue
           # print(a[i],end='')
        elif a[i]<b[j] or a[i]<c[k]:
            i+=1
            continue
        elif b[j]<a[i] or b[j]<c[k]:
            j+=1
            continue
        elif c[k]<a[i] or c[k]<b[j]:
            k+=1
            continue
    if ok==0:
     print("NO",end=' ')
     print()
t=int(input())
while(t>0):
    t-=1
    kq()
