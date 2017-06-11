class Player:

    def __init__(self,name ="Tom", age = 20):
        self.name = name
        self.age = age
    
    def showInfo(self):
        print "Name: ", self.name
        print "Age: ", self.age

player1 = Player("Duc", 23)


player1.showInfo()

#Tra ve gia tri cua thuoc tinh
print 'Tra ve gia tri cua thuoc tinh Name: ', getattr(player1,"name")

#Get gia tri vao thuoc tinh Age
setattr(player1, "age", 30)
print 'Set gia tri vao thuoc tinh Age:', player1.age

#Kiem tra co thuoc tinh address?
kq = hasattr(player1,"address")
if kq == True:
    print 'Co thuoc tinh address trong Object player1'
else:
    print  'Khong co thuoc tinh address trong Object player1'
    print 'Tao thuoc tinh Address cho Object player1'
    setattr(player1, 'address', "VN")
    print 'Address: ', player1.address

    delattr(player1,'address')
    print hasattr(player1, "address")

