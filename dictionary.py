my_dict = {'Name': 'Duc', 'Age': 23, 'Class':'Junior'}
print my_dict
print my_dict['Name']

#Update key 'Age'
my_dict['Age'] = 8
print my_dict['Age']

#Create new key
my_dict['School'] = 'HCMUT'
print  my_dict['School']

print my_dict
print my_dict['Name']

#*****
#Methods with Description

#Adds dictionary dict2's key-values pairs to dict
my_dict12 = {'MS': 1123}
my_dict.update(my_dict12)

print "My dict: %s" % my_dict

#returns a list of dict's (key, value) tuple pairs
print "Demo: %s" % str(my_dict)
print "Demo: %s" % my_dict.items()


#returns value or default if key not in dictionary
print "Value: %s" % my_dict.get('Name')
print "Value: %s" % my_dict.get('IQ','150')

#Retue
#Return true if a given key is available in the dictionary, otherwise it returns a false
print "Value: %s" % my_dict.has_key('Age')

#Create a new dictionary with keys from seq and values set to value.
seq = ('name', 'age','sex')
my_dict2 = dict.fromkeys(seq)
print "New dict: %s " % str(my_dict2)

my_dict2 = dict.fromkeys(seq, 10)
print "New dict: %s " % str(my_dict2)


#Returns a shall copy of dictionary
print "Old dict: %s" % str(my_dict)
my_dict1 = my_dict.copy()
print "New dict: %s " % str(my_dict1)


#Removes all element of dictionary
print "Do dai dict",len(my_dict)
my_dict.clear()
print "Do dai dict",len(my_dict)





#Delete key 'Class'
del my_dict['Class']
print my_dict, type(my_dict)

#Delete dictionary
del my_dict
print my_dict


