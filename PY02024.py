def cmp(n):
    sum=1
    n=str(n)
    for i in n:
        sum*=int(i)
    return (sum,int(n))
t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    b=sorted(a,key=cmp)
    for i in b:
        print(i,end=' ')
    print()