class TrungTuyen:
    def __init__(self,ma,tenGV,MaXt,tin,chuyen):
        self.ma="GV{:02d}".format(ma)
        self.tenGV=tenGV
        self.MaXt=MaXt
        self.tin=tin
        self.chuyen=chuyen
        self.tong=0
        self.mon=''
        self.tt=''

    def Mon(self):
        if self.MaXt[0]=='A':
            self.mon='TOAN'
        elif self.MaXt[0]=='B':
            self.mon='LY'
        elif self.MaXt[0]=='C':
            self.mon='HOA'

    def Tong(self):
        ut=0
        if self.MaXt[1]=='1':
            ut=2.0
        elif self.MaXt[1]=='2':
            ut=1.5
        elif self.MaXt[1]=='3':
            ut=1.0
        elif self.MaXt[1]=='4':
            ut=0.0
        self.tong=self.tin*2+self.chuyen+ut
        if (self.tong)<18:
            self.tt='LOAI'
        elif (self.tong)>=18:
            self.tt='TRUNG TUYEN'

    def __str__(self) :
       return f"{self.ma} {self.tenGV} {self.mon} {self.tong} {self.tt}"

n=int(input())
a=[]
for i in range(n):
   tenGV=input()
   MaXt=input()
   tin=float(input())
   chuyen=float(input())
   a.append(TrungTuyen(i+1,tenGV,MaXt,tin,chuyen))
  # a[i].TrangThai()
   a[i].Mon()
   a[i].Tong()
a.sort(key=lambda x:(-x.tong), reverse=False)

for i in a:
    print(i)
       


        

