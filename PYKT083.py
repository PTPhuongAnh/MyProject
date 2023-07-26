
def Tuyen(self,ma,ten,lt,th):
    self.ma="TS{:02d}".format(ma)
    self.ten=ten
    self.tb=(lt+th)/2
    self.xl=''

def xepLoai(self):
    if self.tb<5:
        self.xl='TRUOT'
    elif self.tb>=5 and self.tb<8:
        self.xl='CAN NHAC'
    elif self.tb>=8 and self.tb<9.5:
        self.xl='DAT'
    elif self.tb>=9.5:
        self.xl='XUAT SAC'

def __str__(self):
    self.tb=format(self.format,".2f")
    return f"{self.ma} {self.ten} {self.tb} {self.xl}"

t=int(input())
a=[]
for i in range(t):
    s=input()
    d1=float(input())
    d2=float(input())
    if d1>10:
        d1=d1/10
    if d2>10:
        d2=d2/10
    a.append(Tuyen(i+1,s,d1,d2))
    a[i].xepLoai()

a.sort(key=lambda x:x.tb,reverse=True)

for i in a:
    print(i)
    

