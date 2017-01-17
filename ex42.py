class Animal(object):
	pass

class Dog(Animal):

	def __init__(self, name):
		self.name = name

	def printName(self):
		pass

class Cat(Animal):

	def __init__(self, name):
		self.name = name

class Person(object):

	def __init__(self, name):
		self.name = name
		self.pet = None

rover = Dog("Rover")
#print "rover %r" % rover
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
rover.printName()
