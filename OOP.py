#hàm khởi tạo
#class Xe:
 #   def __init__(self):
  #      print("Ham khoi tao")
#x1=Xe()
#x2=Xe()
#hàm khởi tạo truyền tham số
#class Student:
   # name=''
    #age=0
    #def __init__(self,name,age):
    #    self.name=name
     #   self.age=age
#c=Student("N V C",32)
#print(c.name)
#print(c.age)
# Tạo getter và setter theo cách thông thường
#class className:
    #thuộc tính name
 #   __name='' #dang ở chế độ private
    #setter cho name
  #  def setName(self,name):
   #     self.__name=name
    #Getter cho name
    #def getName(self):
     #   return self.__name
#Sử dụng
#c=className()
#c.setName(input())
#print(c.getName())
##Để khai báo 1 hàm là setter thì ta sử dụng từ khóa @name.setter, còn getter thì ta
##sử dụng từ khóa @property,cả hai đều được đặt phía trước khai báo hàm
class Freetuts:
    #thuộc tính
    __domain=''
    #Getter
    @property
    def domain(self):
        print("GETTER được gọi")
        return self.__domain
    #Setter
    @domain.setter
    def domain(self,domain):
        print("SETTER được gọi")
        self.__domain=domain
    #sử dụng
c=Freetuts()
c.domain="aaaa"
print(c.domain)

