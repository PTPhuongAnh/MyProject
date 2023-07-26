class TS:
    def __init__(self,ma,ten,diem,dantoc,kv):
        self.ma="TS{:02d}".format(ma)
        self.ten=self.Name(ten)
        self.diem=diem
        self.dantoc=dantoc
        self.kv=kv
        self.tong=0
        self.tt=''

    def Name(self,ten):
        ten=ten.lower().split()
        for i in range(len(ten)):
            ten[i]=ten[i][0].upper()+ten[i][1:]
        return ' '.join(ten)
    

    def chuan(self,ten):
        ten=ten.lower().split()
        for i in range(len(ten)):
            ten[i]=ten[i][0].upper()+ten[i][1:]
        return ' '.join(ten)
        
    def KQ(self):
        kv=0
        dt=0
        if self.kv=='1':
            kv=1.5
        elif self.kv=='2':
            kv=2
        elif self.kv=='3':
            kv=0

        if self.dantoc=='Kinh':
            dt=0
        else:
            dt=1.5
        
        self.tong=self.diem+kv+dt
        if self.tong>=20.5:
            self.tt='Do'
        else:
            self.tt='Truot'
    
    def __str__(self):
        return f"{self.ma} {self.ten} {round(self.tong,1)} {self.tt}"
n=int(input())
a=[]
for i in range(n):
  ten=input()
  diem=float(input())
  dt=input()
  kv=input()
  a.append(TS(i+1,ten,diem,dt,kv))
  a[i].KQ()
a.sort(key=lambda x:(-x.tong,x.ma),reverse=False)
for i in a:
    print(i)
