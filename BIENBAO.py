s=input()
a=[]
n=int(input())
for i in s:
     a.append(int(i))

a=sorted(a,reverse=False)

for i in s:
    print(str(a[i]))



