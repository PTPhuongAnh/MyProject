#bài 5
s=input()
for i in range(0,len(s)):
    if s[i]=='a':
        print(i,end=' ')
print()
print(s.count('a'))
#bài 6
s=input()
b=s.split()
print(len(b))
for i in b:
    print(i)

#bài 8
s=input()
s.strip()
for i in s.split():
    print(i,end=' ')
#bài 9
a=input()
b=input()
ok=1
for i in s:
    if(s.count(i)!=b.count(i)):
        print("No")
        ok=1
if ok==1:
    print("Yes")


#bài thuc hanh 8
#bài 1

a=[1,1]
n=int(input())
for i in range(2,n):
    x=a[i-1]+a[i-2]
    a.append(int(x))
print(a[n-1])
#bài 3
n=int(input())
a=[]
k=0
while n!=0:
    a.append(int(n%2))
    n//=2
for i in range(len(a)-1,-1,-1):
    print(a[i],end=' ')
#bài 4
n,v=map(int,input().split())
a=[]
a=list(map(int,input().split()))
if a.count(v)==0:
    print("NO")
else:
    print("YES")
print(a.index(v)+1)
#bài 5
n,i=map(int,input().split())
a=[]
a=list(map(int,input().split()))
a.pop(i)
for i in range(0,len(a)):
    print(a[i],end=' ')
#bài 6
n,i,v=map(int,input().split())
a=[]
a=list(map(int,input().split()))
a.insert(i,v)
for i in range(0,len(a)):
    print(a[i],end= ' ')
#bài 7
n=int(input())
a=[]
a=list(map(int,input().split()))
a.sort()
for i in range(0,len(a)):
    print(a[i],end= ' ')
#bài 8
n=int(input())
a=list(map(int,input().split()))
d=1
maxx=1
ind=0
st=0
for i in range (1,n):
    if a[i]*a[i-1]<0:
        d+=1
        if maxx<d:
            maxx=d
            st=ind
        else:
            d=1
            ind=i
print(maxx)
for i in range(st,st+maxx):
    print(a[i],end=' ')
#bài 9
n=int(input())
a=[1,1]
res=[]
for x in range(2,1000):
    a.insert(x,a[x-1]+a[x-2])
x=100
while n!=0:
    if a[x]<=n:
        if a[x]==n:
            res.insert(0,a[x-1])
            res.insert(0,a[x-2])
            break
        n-=a[x]
        res.insert(0,a[x])
    x-=1
for i in range(0,len(res)):
    if res[i]<1000000000:
        print(res[i],end=' ')


