class IterateMain(object):

	def __init__(self,n):
		self.n = n

	def __iter__(self):
		return IterateCo(self.n)

class IterateCo(object):

	def __init__(self,n):
		self.n = n
		self.i = 0

	def __iter__(self):
		return self

	def next(self):
		if self.i < self.n:
			i = self.i +1
			self.i += 1
			return i
		else:
			raise StopIteration()

i1 = IterateMain(5)

print list(i1)
print list(i1)
print list(i1)
i2 = IterateMain(10)
print list(i2)
for x in i1:
	print x
for y in i2:
	print y
