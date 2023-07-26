
t=int(input())
while(t>0):
    t-=1
    s=input()
    s=s+"abc"
    res=""
    kq=-1000
    for i in range (0,len(s)):
        if(s[i].isdigit()):
            res+=s[i]
        else:
            if(res!=""):
             kq=max(kq,int(res))
             res=""
    print(kq)

