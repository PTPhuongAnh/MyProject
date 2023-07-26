import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist
from datetime import datetime
list_hour = ['Tý','Sửu','Sửu','Dần','Dần',"Mão","Mão",'Thìn','Thìn','Tị','Tị','Ngọ','Ngọ','Mùi','Mùi','Thân','Thân','Dậu','Dậu','Tuất','Tuất','Hợi','Hợi', 'Tý']

def ngay_duong_sang_am(ngay,thang,nam):
    time = datetime(year=nam,month=thang,day=ngay)
    lunar = Converter.Solar2Lunar(time)
    print("ngày âm lịch được chuyển đổi là:")
    print(lunar.day, lunar.month, lunar.year)

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

while(True):
    print("Nhập lựa chọn: ")
    print("0. Để kết thúc chương trình.")
    print("1. Đổi ngày dương lịch sang âm lịch.")
    print("2. Đổi ngày và giờ dương lịch sang âm lịch.")
    print("3. Đổi ngày âm lịch sang dương lịch.")
    print("4. Đổi ngày và giờ âm lịch sang dương lịch.")
    nhap = int(input())
    if nhap==0: 
        break
    while(nhap not in range(0,6)):
        print("Nhập sai lựa chọn, vui lòng nhập lại!")
        nhap = int(input())
    if nhap==0: 
        break
    else:
        if nhap == 1:
            print("Nhập ngày, tháng, năm:")
            try:
                [ngay,thang,nam]=(int (x) for x in input().split())
                ngay_duong_sang_am(ngay,thang,nam)
            except:
                print("Nhập lỗi! Vui lòng thử lại.")
        elif nhap == 2:
            print("Nhập giờ, phút, giây, ngày, tháng, năm:")
            try:
                [gio, phut, giay, ngay,thang,nam]= (int (x) for x in input().split())
                ngay_gio_duong_sang_am(gio,phut,giay,ngay,thang,nam)
            except:
                print("Nhập lỗi! Vui lòng thử lại.")
        elif nhap == 3:
            print("Nhập ngày, tháng, năm:")
            try:
                [ngay,thang,nam]=(int (x) for x in input().split())
                ngay_am_sang_duong(ngay,thang,nam)
            except:
                print("Nhập lỗi! Vui lòng thử lại.")
        elif nhap == 4:
            print("Nhập giờ (Tý, Sửu, Dần,...) có dấu:")
            gio = input()
            while(gio not in list_hour):
                print("nhập sai giờ, vui lòng nhập lại.")
                gio = input()
            print("Nhập ngày, tháng, năm:")
            try:
                [ngay,thang,nam]=(int (x) for x in input().split())
                ngay_va_gio_am_sang_duong(gio,ngay,thang,nam)
            except:
                print("Nhập lỗi! Vui lòng thử lại.")
            

    print("Tiếp tục chuyển đổi không?")
    print("1: Yes\nKhác: No")
    tieptuc=input()
    if(tieptuc!='1'):  break