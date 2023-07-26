t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=({int(x) for x in input().split()})
    maxx=max(a)
    minn=min(a)
    print(maxx-minn+1-len(a))
