def check(s):
    if(len(s)<4):
        return 0
    for i in s:
        if i.isdigit():
            if int(i)<0 or int(i)>255:
                return 0
        else:
            return 0

    return 1

t=int(input())
while t>0:
    t-=1
    s=input().split('.')
    if(check(s)==1):
        print('YES')
    else:
        print('NO')
