t=int(input())
a = [float(x) for x in input().split()]

sum=0
cnt1=0
cnt2=0


ln=max(a)
nn=min(a)
for i in a:
    sum+=i
    if(i==ln): cnt1+=1
    if(i==nn): cnt2+=1
print("{:.2f}".format((sum-cnt1*ln-cnt2*nn)/(t-cnt1-cnt2)))
    
