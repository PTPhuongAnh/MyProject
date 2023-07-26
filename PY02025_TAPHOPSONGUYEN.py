n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
i,j=0,0
c=[]
d=[]
while i<n and j<m:
    if a[i]==b[j]:
        print(a[i],end=' ')
        i+=1
        j+=1
        continue
    elif a[i]<b[j]:
        i+=1
        continue
    elif a[j]<b[i]:
        j+=1
        continue
print()

for i in a:
    if not(i in b):
        print(i,end=' ')
print()
for i in b:
    if not(i in a):
        print(i,end=' ')