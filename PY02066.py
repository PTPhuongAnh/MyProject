n=int(input())
a=[]
ok=0
while True:
 
 a.extend(int(x) for x in input().split()) 
 
 if len(a)==n:
    break
 
m=a[len(a)-1]

for i in range(1,m+1):
    if not(i in a):
        ok=1
        print(i)

if(ok==0):
    print('Excellent!')