import math


def nho(n):
    n=n+"abc"
    res=""
    nho=10000000000
    for i in n:
        if(i.isdigit()):
            res+=i
        else:
           if(res!=""):
            nho=min(nho,int(res))
            res=""
    return nho


t=int(input())
while t>0:
    t-=1
    s=input()
    print(nho(s))

t = int(input())
while t > 0:
    p, q = [str(x) for x in input().split()]
    list = []
    while True:
        for x in input().split():
            list.append(str(x))
        if len(list) == 2:
            break
    x1 = list[0]
    x2 = list[1]