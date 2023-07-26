f=open('vd.inp','r') #mở tệp để đọc
g=open('vd.out','w') #mở tệp để ghi
s=f.readline()#đọc một dòng trong tệp và trả về chuỗi
tong=0
a=list(map(int,s.split()))
for i in range(0,len(a)):
    tong+=a[i]
kq=str(tong)
g.write(kq)#ghi 1 chuỗi vào tệp
f.close()#đóng tệp
g.close()