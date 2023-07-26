n=int(input())
a=[]
for i in range(n):
    a.append(list(int(x) for x in input().split()))
k=int(input())
tren=0
duoi=0
for i in range(n-1):
    for j in range(i+1,n):
        tren+=a[i][j]
for i in range(1,n):
    for j in range(0,i):
        duoi+=a[i][j]
if abs(tren - duoi) <=k:
    print("YES")
else:
    print("NO")
print(abs(tren - duoi))
