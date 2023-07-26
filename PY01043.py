def tn(n):
    m=n[::-1]
    if m!=n:
        return 0
    else:
        if(len(n)%2!=0):
            return 0
        else:
            for i in n:
                if int(i)%2!=0:
                    return 0
    return 1

t=int(input())
while t>0:
    t-=1
    s=int(input())
    for i in range(22,s,2):
        if(tn(str(i))==1):
            print(i,end=" ")       
    print("")   
