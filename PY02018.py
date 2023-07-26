n=int(input())
a=[int(x) for x in input().split()]
ok=0
abc=-100
cnt=[0]*30001
nn=10000000000
for i in a:
    abc=max(abc,i)

for i in a:
    cnt[i]=1
for i in range(1,abc+2):
    if(cnt[i]==0):
        nn=min(i,nn)
print(nn)

