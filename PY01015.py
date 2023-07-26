def KG(a):
    for i in (0,len(a)-1):
        if i>i+1:
            return False
        return True

t=int(input())
while(t>0):
    t-=1
    a=input()
    if(KG(a)):
        print("YES")
    else:
        print("NO")