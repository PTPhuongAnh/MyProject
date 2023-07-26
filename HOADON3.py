class MATHANG:
    tong=0
    def __init__(self,ma,ten,sl,gia,ck):
        self.ma=ma
        self.ten=ten
        self.sl=sl
        self.gia=gia
        self.ck=ck
        self.tong=self.sl*self.gia-self.ck
    def __str__(self):
        return self.ma+" "+self.ten+" "+str(self.sl)+" "+str(self.gia)+" "+str(self.ck)+" "+str(self.tong)
n=int(input())
a=[]
for i in range(n):
    ma=input()
    ten=input()
    sl=int(input())
    gia=int(input())
    ck=int(input())
    a.append(MATHANG(ma,ten,sl,gia,ck))
a=sorted(a,key=lambda x:-x.tong)

for i in a:
    print(i)
