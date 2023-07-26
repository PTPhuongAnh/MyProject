class VanToc:
    def __init__(self,ten,dvi,dich):
        self.ten=ten
        self.dvi=dvi
        self.dich=dich
        self.ma=''
        self.vantoc=0

    def Ma(self):
        a=[i[0] for i in ten.split()]
        b=[i[0] for i in dvi.split()]
        self.ma=''.join(b)+''.join(a)

    def VT(self):
        self.vantoc=(120/((int(dich[0])- 6+int(dich[1])/60)))
    def __str__(self):
        return f"{self.ma} {self.ten} {self.dvi} {round(self.vantoc)} Km/h "

n=int(input())
a=[]
for i in range(n):
    ten=input()
    dvi=input()
    dich=input().split(':')
    a.append(VanToc(ten,dvi,dich))
    a[i].Ma()
    a[i].VT()

a.sort(key=lambda x:(-x.vantoc),reverse=False)
for i in a:
    print(i)



