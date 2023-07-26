from datetime import datetime
import pytz

print("nhập địa điểm :")
dc=input()
tz_x=pytz.timezone(dc)
datetime_x = datetime.now(tz_x)
print(f' Gio tai {dc}',datetime_x.strftime("%m/%d/%Y,%H:%M:%S"))

tz_VN=pytz.timezone('Asia/HoChiMinh')
datetime_VN=datetime.now(tz_VN)
print("Gio tại VN: ",datetime_VN.strftime("%m/%d/%Y,%H:%M:%S"))