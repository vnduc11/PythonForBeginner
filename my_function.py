def printinfo(my_var, *vartuple):
    "In mot tham so da tuyen"
    print 'Ket qua: '
    print my_var
    for var in vartuple:
        print var
    return

def my_smart_function(num1, num2, math_operation):
    "Tinh cong hoac tru 2 so"
    if math_operation == "phepCong":
        print 'Ket qua phep cong la: '
        print num1 + num2
    elif math_operation == "phepTru":
        print 'ket qua phep tru la: '
        print num1 - num2
    else:
        print "Moi nhap 'phepCong' hoac 'phepTru' de tinh toan"
    return

