t=int(input())
while(t>0):
   # t-=1
    x=int(input())
    f=[2,3,5,9]
    for i in range(4,x+1):
        if(i%2==0):
            a=f[i-1]+i
            f.append(int(a))

        else:
            a=f[i-1]+i-1
            f.append(int(a))
    print(f[x-1])