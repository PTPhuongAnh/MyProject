class XepHang:
    def __init__(self,ten,ac,sb):
        self.ten=ten
        self.ac=ac
        self.sb=sb

    def __str__(self):
        return f"{self.ten} {self.ac} {self.sb}"

n=int(input())
a=[]
for i in range(n):
    ten=input()
   # ac,sb=[int(x) for x in input().split()]
    ac,sb=map(int,input().split())
    a.append(XepHang(ten,ac,sb))
a.sort(key=lambda x:(-x.ac,x.sb,x.ten),reverse=False)
for i in a:
    print(i)