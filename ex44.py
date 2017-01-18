class Parent(object):

	def implicit(self):
		print "print implicit"
	
	def override(self):
		print "Parent override method"

class Child(Parent):
	
	def override(self):
		print "before child call"
		super(Child, self).override()
		print "after child call"
		print "Child override method"

dad = Parent()
dad.implicit()
son.implicit()
dad.override()
son.override()

class Other(object):

	def implicit(self):
		print "Other implicit"

	def override(self):
		print "other override"

# Composition example:

class Child(object):

	def __init__(self):
		self.other = Other()

	
	def override(self):
		self.other.implicit()
		print "child before override"
		self.other.override()
		print "child after override"

son = Child()
#son.implicit()
son.override()
