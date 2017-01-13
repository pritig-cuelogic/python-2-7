def add_number(a, b = 2):
	print "First No = %d" % a
	print "second No = %d" % b
	print "Sum = %d" % (a+b)
	print "Function End !"

print "First type function calling \n"
add_number(3, 2)

a = 8
b = 10
print "Second type function calling \n"
add_number(a, b)

print "Third type function calling \n"
add_number(3+2, 2*3)

print "fourth type function calling \n"
add_number(16/a, b/2)

print "Next type function calling \n"
add_number(16/a)
