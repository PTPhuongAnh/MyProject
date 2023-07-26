#f=[]




t=int(input())
while(t>0):
    t-=1
    x=int(input())
    f=[0,2,5,9]
   
    for i in range(4,x+1):
        d=f[i-1]+i+1
        f.append(int(d))

    print(int(f[x-1]))