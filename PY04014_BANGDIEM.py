class BangDiem:
    def __init__(self,ma,ten,tb):
     self.ma="HS{:02d}".format(ma)
     self.ten=ten
     self.tb=round(tb/10/1.2,1)
     self.xl=''
    
    def setXL(self):
        if self.tb>=9:
            self.xl='XUAT SAC'
        elif self.tb>=8:
            self.xl='GIOI'
        elif self.tb>=7:
            self.xl='KHA'
        elif self.tb>=5:
            self.xl='TB'
        elif self.tb<5:
            self.xl='YEU'
    
    def __str__(self):
        self.tb=format(self.tb,'.1f')
        return f"{self.ma} {self.ten} {self.tb} {self.xl}"
n=int(input())
a=[]
for i in range(n):
    ten=input()
    b=[float(x) for x in input().split()]
    cnt=0
    cnt+=b[0]*2+b[1]*2
    for j in range(2,10):
        cnt+=b[j]
    a.append(BangDiem(i+1,ten,cnt))

for i in a:
    i.setXL()

a.sort(key=lambda x: (-x.tb,x.ma),reverse=False)

for i in a:
    print(i)

