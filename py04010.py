class thiSinh:
    def __init__ (self,ten,ns,d1,d2,d3):
        self.ten=ten
        self.ns=ns
        self.d1=d1
        self.d2=d2
        self.d3=d3


    def tong(self):
        self.tong=self.d1+self.d2+self.d3
    
    def inp(self):
        return self.ten+" "+self.ns+" "+format(self.tong, ".1f")

ten=input()
ns=input()
d1=float(input())
d2=float(input())
d3=float(input())
t=thiSinh(ten,ns,d1,d2,d3)
print(t.inp)
