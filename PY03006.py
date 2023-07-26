t=int(input())
map={}
for i in range(t):
    s=input().tolower()
    for i in range(len(s)):
        if not s[i].isalpha():
            s=s.replace(s[i],' ')
    
    for i in s.split():
        if i in map:
            map[i]+=1
        else:
            map[i]=1

map=sorted(map.items(),key=lambda x: (-x[1],x[0]))
for i in map:
    print(*i)

