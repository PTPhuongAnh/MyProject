


def tn(n):
    str1=str(n)
    str2=str1[::-1]
    if(str1==str2):
        return True
    else:
        return False

def dai(n):
    kq=0
    cnt=0
    while n>10:
        kq+=n%10
        cnt+=1
        n/=10
    if cnt%2!=0:
        return False
    else: return True
def cs(n):
    while n>0:
        if n%10!=0 or n%10!=2 or n%10!=4 or n%10!=6 or n%10!=8:
            return False
        n=n/10
    return True
         
t=int(input())
while t>0:
    t-=1
    n=int(input())
    for i in range (22,n):
        if(tn(i) and dai(i) and cs(i)):
            print(i,end=" ")
        print(" ")
           

