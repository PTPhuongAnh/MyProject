import functools


class SV:
    def __init__(self,ten,ac,sb):
        self.ten=ten
        self.ac=ac
        self.sb=sb

    def p(a, b):
        if a.ac<b.ac: return 1
        elif a.ac==b.ac:
            if a.sb> b.sb:
             return 1
            elif a.sb==b.sb:
                if a.ten> b.ten:
                    return 1
                else: return -1
            else:
                return -1
        else:
            return -1

n=int(input())
a=[]
for i in range(n):
    ten=input()
    ac,sb=[int(x) for x in input().split()]
    a.append(SV(ten,ac,sb))
a=sorted(a,key=functools.cmp_to_key(p))
for i in a:
    print(i.ten, i.ac, i.submit)


