def kiemtra(s):
    if(len(s)%2==0):
        return 0
    else:
        if(s[0]==s[1]):
            return 0
        else:
            for i in range(2,len(s),2):
                if(s[i]!=s[i-2]):
                    return 0
    return 1

t=int(input())
while t>0:
    t-=1
    s=input()
    if(kiemtra(s)==1):
        print("YES")
    else:
        print("NO")


