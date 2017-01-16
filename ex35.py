def printNo(i):
	if(i == 1):
		while i < 5:
			print i
			i += i
	else:
		print "i value not equal to 1"

printNo(1)
printNo(2)

def take_input():
	print "take 1 input :"
	a = raw_input("> ")
	print "take 2 input :"
	b = raw_input("> ")
	a = int(a)
	b = int(b)
	if a > b:
		return a - b
	elif a < b:
		return b - a
	else:
		return a + b

print take_input()
