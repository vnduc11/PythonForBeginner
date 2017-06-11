# -*- coding: utf8 -*-
class Person:
    'Lop Person: name, age, gender'

    def __init__(self, name, age =20, gender = "Male"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def showInfo(self):
        print "Name: ", self.name
        print 'Age: ', self.age
        print 'Gender: ', self.gender

