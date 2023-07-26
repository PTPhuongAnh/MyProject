from math import ceil


class TB:
    def __init__(self,ma,ten,d1,d2,d3):
        self.ma="SV{:02d}".format(ma)
        self.ten=self.Name(ten)
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.diem=(self.d1*3+self.d2*3+self.d3*2)/8
        self.th=None

    def Name(self,ten):
        ten=ten.lower().split()
        for i in range(len(ten)):
            ten[i]=ten[i][0].upper()+ten[i][1:]
        return ' '.join(ten)

    def __str__(self):
        return f"{self.ma} {self.ten} {ceil(self.diem*100)/100} {self.th}"

n=int(input())
a=[]
for i in range(n):
    ten=input().strip()
    d1=float(input())
    d2=float(input())
    d3=float(input())
    a.append(TB(i+1,ten,d1,d2,d3))
a.sort(key=lambda x: (-x.diem,x.ma),reverse=False)
a[0].th=1
for i in range(1,len(a)):
    if a[i].diem==a[i-1].diem:
     a[i].th=a[i-1].th
    else:
        a[i].th=i+1
print(*a,sep='\n')

