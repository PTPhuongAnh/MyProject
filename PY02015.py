import math

while True:
    a = [int(x) for x in input().split()]
    dem = 0
    if a[0] == a[1] == a[2] == a[3] == 0:
           break
    while True:
        if a[0] == a[1] == a[2] == a[3]:
            print(dem)
            break
        mem = a[0]
        for i in range(0, len(a) - 1):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - mem)
        dem += 1


