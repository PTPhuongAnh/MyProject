def tg(str):
    if len(str) <3:
        return 'NO'
    i=1
    while i<len(str) and str[i]>str[i-1]:
        i+=1
    while i<len(str) and str[i] <str[i-1]:
        i+=1
    if (i==len(str)):
        return 'YES'
    else:
        return 'NO'
t=int(input())
while t>0:
    t-=1
    s=input()
    print(tg(s))