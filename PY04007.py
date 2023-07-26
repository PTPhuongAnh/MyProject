class Maxtri:
    def __init__(self,m,n,a):
        self.m=m
        self.n=n
        self.a=a
    def mul(self):
        for i in range(self.n):
            for j in range(self.n):
                x=0
                for k in range(self.m):
                    x+=(self.a[i][k]*self.a[j][k])
                print(x,end=" ")
            print()
#n*m m*n 
t=int(input())
while t>0:
    t-=1
    n,m=[int(x) for x in input().split()]
    a=[[0]]*n
    for i in range(n):
        a[i]=[int(x) for x in input().split()]
    mt=Maxtri(n,m,a)
    mt.mul()
