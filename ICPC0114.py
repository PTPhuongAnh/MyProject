import math


def snt(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return 0
    return 1

def check(n):
    if(snt(int(n))==0):
        return 0
        dao=n[::-1]
        if snt(int(dao))==0:
            return 0
        tong=0
        for i in n:
            if(snt(int(i)))==0:
                return 0
            tong+=i
        if snt(tong)==0:
            return 0
        return 1
        

