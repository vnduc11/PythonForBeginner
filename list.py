#!/usr/bin/python
#-*- coding: utf8 -*-

#Day la vi du ve list

my_list = ['Toan hoc', 'Sinh hoc', 'Anh van', 'Van hoc']

#Them obj vao cuoi List
my_list.append('Lich su')

#Them noi dung vao cuoi list
my_list.extend(['Cong dan', 'Lich su'])

print (my_list)

#Them obj xuat hien bao nhieu lan
print my_list.count('Lich su')

#Xem chi muc (vi tri bat dau tu 0) cua obj
print my_list.index('Lich su')

#Chen obj voi chi muc chi dinh
my_list.insert(1,'Hoa hoc')

#Dao nguoc thu tu

my_list.reverse()
print my_list

#Sort theo thu tu
my_list.sort()
print "List : ", my_list

#Xoa ca obj co gia tri la Lich su
print my_list.remove('Lich su')

#Lay obj tai chi muc cuoi (mac dinh) hoac chi dinh va remove tat ca obj khac
print my_list.pop(2)

 
list1 =[]
list2 = [4]

list3 = list1 + list2 # Noi list
print 3*list3 # Lap list

print list1, type(list1)

#Them vao phan tu cuoui
list1.append(23)
print list1

#Xoa phan tu trong list
del list1[1]
print list1

a = len(list1)
b = 3 not in list1
print a, b

for x in list1:
    print x
