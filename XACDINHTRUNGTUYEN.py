class TRUNGTUYEN:
    def __init__(self,maGV,ten,maXT,tin,chuyen):
        diem=0;
        self.maGV="GV{:02d}".format(maGV)
        self.ten=ten
        self.maXT=maXT
        self.tin=tin
        self.chuyen=chuyen
        self.diem=tin*2+chuyen
        self.status=""
        self.mon=""

    def setMon(self):
        s=self.maXT[0:1]
        if(s=='A'):
            self.mon='TOAN'
        elif(s=='B'):
            self.mon='LY'
        elif(s=='C'):
            self.mon='HOA'
    def setDiem(self):
        s=self.maXT[1::]
        if(s==1):
            self.diem+=2
        elif(s==2):
            self.diem+=1.5
        elif(s==3):
            self.diem+=1
        else:
            self.diem+=0
    
    def setStatus(self):
        if(self.diem<18):
            self.status='TRUOT'
        else:
            self.status='TRUNG TUYEN'

    def __repr__(self):
        self.Diem='{0:.1f}'.format(self.diem)
        return f'{self.maGV} {self.ten} {self.mon} {self.diem} {self.status}'

t=int(input())

l=[]
for i in range(0,t):
    l.append(TRUNGTUYEN(i+1,input(),input(),float(input()),float(input())))
    l[i].setDiem()
    l[i].setMon()
    l[i].setStatus()

l.sort(key=lambda x: -x.diem)
for i in l:
    print(i)



