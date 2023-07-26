t=int(input())
while t>0:
   t-=1
   n=int(input())
   a=[int(x) for x in input().split()]
   cnt=0
   kq=0
   for i in range(0,len(a)):
    for j in range(0,i+1):
        if a[j]<=a[i]:
            cnt+=1
        else:
            if(cnt!=0):
              kq=cnt
              print(kq,end=' ')
   cnt=0
   kq=0
