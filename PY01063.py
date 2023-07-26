def kq(s,k):
    res=""
    cnt=0
    for i in range(0,len(s)):
        if(len(s)!=len(k)):
          res+=s[i]
        else:
          if(int(res)==int(k)):
            cnt+=1
            res=""
    return cnt

t=int(input())
while t>0:
    t-=1
    s=input()
    k=input()
   # print(kq(s,k))
    res=""
    cnt=0
    for i in range(0,len(s)):
        if(len(s)!=len(k)):
          res+=s[i]
        else:
          if(int(res)==int(k)):
            cnt+=1
            print(res,end=" ")
    res=""
        
