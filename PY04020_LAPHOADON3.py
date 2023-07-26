class HoaDon:
    def __init__(self,ma,ten,sl,gia,ck):
        self.ma=ma
        self.ten=ten
        self.sl=sl
        self.gia=gia
        self.ck=ck
        self.tong=0

    def Tong(self):
        self.tong=self.sl*self.gia-self.ck

    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.gia} {self.ck} {self.tong}"

n=int(input())
a=[]
for i in range(n):
    ma=input()
    ten=input()
    sl=int(input())
    gia=int(input())
    ck=int(input())
    a.append(HoaDon(ma,ten,sl,gia,ck))
    a[i].Tong()
a.sort(key=lambda x:(-x.tong),reverse=False)
for i in a:
    print(i)