#while True:
#	print "priti"

def printStr(str):
	print str
	return

def change( mylist ):
	mylist.append([1,2,3,4])
	print "Values inside the function: ", mylist

def changeme( mylist ):
	mylist = [1,2,3,4]
	print "Values inside the function: ", mylist

def printinfo( name, age ):
	print "Name: ", name
	print "Age ", age

def printValue(name, age = 34):
	print "Name: " , name
	print "Age: " , age

def addNumbers(*vars):
	for i in vars:
		print "Number is : %d" % i

addNumbers(34,56)
addNumbers(55, 56, 57, 58, 59, 60)
print printStr("Calling printstr function")
mylist = [10,20,30]
changeme(mylist)
print "Values outside the function: ", mylist
printStr("This print an string")
change([2, 33, 55])
printinfo( age=50, name="miki" )
printValue(age = 30, name = "Priti")
printValue("Neha")
printValue(name = "Priti")
