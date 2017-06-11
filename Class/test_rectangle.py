# -*- coding: utf8 -*-
from rectangle import rectangle

# a = input('Nhap chiều rộng: ')
# b = input('Nhập chiều dài: ')

r1 = rectangle(10, 5)

print 'Chiều rộng là: ', r1.chieuRong
print 'Chiều dài là: ', r1.chieuDai
print 'Phươn thức gán chiều rộng', r1.getHight()
print 'Diện tích là: ', r1.tinhDienTich()
