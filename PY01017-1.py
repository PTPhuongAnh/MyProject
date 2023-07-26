t=int(input())
while t>0:
    t-=1
    s=input()
    s=s+" "
    dem=0
    for i in range(0,len(s)-1):
        
        if(s[i]==s[i+1]):
             dem+=1
        else:
            print(str(dem+1)+s[i],end='')
            dem=0
    print()