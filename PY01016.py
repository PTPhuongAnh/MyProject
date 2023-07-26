t=int(input())
while t>0:
    t-=1
    s=input()
    res=''
    for i in s:
        if(i.isdigit()== True):
            print(res*int(i),end='')
        else:
            res=i
    print()

#t = int(input())
#for i in range(t) :
   # s = input()
   # for i in range(0, len(s), 2) :
      #  for j in range(0, int(s[i+1])) :
           # print(s[i], end ="")
    #print()