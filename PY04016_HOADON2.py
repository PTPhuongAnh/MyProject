import datetime


class HoaDon:
    def __init__(self,ma,ten,phong,nhan,tra,them):
        self.ma="KH{:02d}".format(ma)
        self.ten=ten
        self.phong=phong
        self.nhan=nhan
        self.tra=tra
        self.them=them
        self.tong=0
        self.ngayo=0

    def soNgayO(self):
        t=datetime.datetime.strptime(self.nhan, "%d/%m/%Y")
        t1=datetime.datetime.strptime(self.tra,"%d/%m/%Y")
        self.ngayo= (t1-t).days+1
    
    def Tonng(self):
        gia=0
        if self.phong[0]=='1':
            gia=25
        elif self.phong[0]=='2':
            gia=34
        elif self.phong[0]=='3':
            gia=50
        elif self.phong[0]=='4':
            gia=80
        self.tong=self.ngayo*gia+self.them

    def __str__(self):
        return f"{self.ma} {self.ten} {self.phong} {self.ngayo} {self.tong}"


n=int(input())
a=[]
for i in range(n):
    ten=input().strip()
    phong=input().strip()
    nhan=input().strip()
    tra=input().strip()
    them=int(input())
    a.append(HoaDon(i+1,ten,phong,nhan,tra,them))
    a[i].soNgayO()
    a[i].Tonng()
a.sort(key=lambda x:(-x.tong),reverse=False)

for i in a:
    print(i)


