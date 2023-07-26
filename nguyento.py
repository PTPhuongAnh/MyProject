#import datetime
from datetime import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist
#from datetime import datetime
def ngay_duong_sang_am(ngay,thang,nam):
    time = datetime(year=nam,month=thang,day=ngay)
    lunar = Converter.Solar2Lunar(time)
    print("ngày âm lịch được chuyển đổi là:")
    print(lunar.day, lunar.month, lunar.year)

   
list_hour = ['Tý','Sửu','Sửu','Dần','Dần',"Mão","Mão",'Thìn','Thìn','Tị','Tị','Ngọ','Ngọ','Mùi','Mùi','Thân','Thân','Dậu','Dậu','Tuất','Tuất','Hợi','Hợi', 'Tý']
def ngay_gio_duong_sang_am(gio,phut,giay,ngay,thang,nam):
    time = datetime(year=nam,month=thang,day=ngay,hour=gio, minute=phut, second=giay)
    lunar = Converter.Solar2Lunar(time)
    print("ngày và giờ âm lịch được chuyển đổi là:")
    print('Giờ', list_hour[time.hour], end = " ngày ")
    print(lunar.day, lunar.month, lunar.year)


def ngay_am_sang_duong(ngay,thang,nam):
    time = datetime(year=nam,month=thang,day=ngay)
    lunar = Lunar(nam, thang, ngay)
    solar = Converter.Lunar2Solar(lunar)
    print("ngày dương lịch được chuyển đổi là:")
    print(solar.day, solar.month, solar.year)

def ngay_va_gio_am_sang_duong(gio,ngay,thang,nam):
    gio1=list_hour.index(gio)
    gio2=0
    for a in range(len(list_hour)):
        if gio == list_hour[a]:
            gio2 = a
    time = datetime(year=nam,month=thang,day=ngay)
    lunar = Lunar(nam, thang, ngay)
    solar = Converter.Lunar2Solar(lunar)
    print("ngày và giờ dương lịch được chuyển đổi là:")
    if gio == "Tý":
        print("Từ", gio2, "giờ đến", gio1+1, "giờ", sep=" ", end=" ngày " )
    else:
        print("Từ", gio1, "giờ đến", gio2+1, "giờ", sep=" ", end=" ngày " )
    print(solar.day, solar.month, solar.year)