class MaxTri:
    def __init__(self,n,m,a):
        self.n=n
        self.m=m
        self.a=a
    def mul(self):
        for i in range(self.n):
            for j in range(self.n):
                x=0
                for k in range(self.m):
                    x+=(self.a[i][k]*self.a[j][k])
                print(x,end=" ")
            print()
t=int(input())

while t>0:
    t-=1
    n,m=[int(x) for x in input().split()]
    #a=[[0]]*n
    a=[]
    for i in range(n):
        #a[i]=[int(x) for x in input().split()]
        a.append([int(x) for x in input().split()])
    mt=MaxTri(n,m,a)
    mt.mul()



