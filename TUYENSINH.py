class TuyenSinh:
    def __init__(self, stt, hoten, diemthi, dantoc, khuvuc):
        self.maTS = "TS{:02d}".format(stt)
        self.hoten = hoten
        self.diemthi = diemthi
        self.dantoc = dantoc
        self.khuvuc = khuvuc
        self.status = ''

    def setDiemthi(self):
        if self.khuvuc == 1:
            self.diemthi += 1.5
        if self.khuvuc == 2:
            self.diemthi += 1
        if self.dantoc != 'Kinh':
            self.diemthi += 1.5
    
    def setStatus(self):
        if self.diemthi < 20.5:
            self.status = 'Truot'
        else:
            self.status = 'Do'

    def chuanHoa(self):
      s = self.hoten.strip().lower()
      l = [str(x) for x in s.split()]
      t = ''
      for i in l:
        t += str(i[0].upper()) + str(i[1:])
        t += ' '
      self.hoten = t.strip()
 
    def __repr__(self):
        self.diemthi = '{0:.1f}'.format(self.diemthi)
        return f'{self.maTS} {self.hoten} {self.diemthi} {self.status}'

t = int(input())

l = []
for i in range(0, t):
    l.append(TuyenSinh(i + 1, input(), float(input()), input(), int(input())))
    l[i].setDiemthi()
    l[i].setStatus()
    l[i].chuanHoa()

l.sort(key=lambda x: (-x.diemthi, x.maTS), reverse=False)

for i in l:
    print(i)
