def tong(n):
    s=0
    for i in n:
      s+=int(i)
    if(s%3!=0):
        return 0
    return 1
t=int(input())
while t>0:
    t-=1
    s=input()
    if(tong(s)==1):
        print("YES")
    else:
        print("NO")
