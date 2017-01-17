import module

print "Module example"
module.printName("Priti")
print module.x

class MyTest:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def printValues(self):
		x = 9
		print "X = %r" % self.x
		print "Y = %r" % self.y
		print "local variable = %r" % x

mytest = MyTest(5, 6)
mytest.printValues()

mytest1 = MyTest(55, 66)
mytest1.printValues()
