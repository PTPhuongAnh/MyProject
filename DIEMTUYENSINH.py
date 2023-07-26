class ThiSinh:
    def chuanHoa(s):
      s = str(s)
      s = s.strip().lower()
      l = [str(x) for x in s.split()]
      t = ''
      for i in l:
        t += str(i[0].upper()) + str(i[1:])
        t += ' '
        return t.strip()
    def __init__(self,ten,diem,dt,kv):
        self.ten=ten
        self.diem=diem
        self.dt=dt
        self.kv=kv
    
    def ut(self):
        kv=0
        if(self.kv==1):
            kv=1.5
        elif(self.kv==2):
            kv=1
        elif(self.kv==3):
            kv=0
       # return kv
        
    def dt(self):
        dt=0
        if(self.kv=="Kinh"):
            dt=0
        else:
            dt=1.5
       # return dt
    def tt(self):
        if(self.diem+ut+dt())
    
    
