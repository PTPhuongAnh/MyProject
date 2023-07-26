n=int(input())
a=[int(x) for x in input().split()]
a=sorted(a)
a1=a[-1]*a[-2]*a[-3]
a2=a[-1]*a[-2]
a3=a[0]*a[1]
a4=a[0]*a[1]*a[-1]
print(max(a1,a2,a3,a4))
