t=int(input())
while t>0:
    t-=1
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    maxx=max(a)
    b=[]
    c=[]
    for i in range(n):
        if a[i]==maxx:
            a.insert(i,m)
            break
    for i in a:
        if i<0: b.append(i)
        else:
            c.append(i)

    for i in b:
        print(i,end=" ")
    for i in c:
        print(i,end=" ")
    print()