# -*- coding: utf8 -*-
class rectangle():
    'Đây là lớp Rectangle'

    #Phương thức tạo đối tượng(Contructor)
    def __init__(self, chieuRong, chieuDai):
        self.chieuRong = chieuRong
        self.chieuDai = chieuDai

    #Method get chieuRong
    def getHight(self):
        return self.chieuRong
    #Method tinh Area
    def tinhDienTich(self):
        return self.chieuDai * self.chieuRong