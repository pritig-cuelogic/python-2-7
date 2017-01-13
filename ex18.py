x = 55
print x
def first_function(*arg):
	arg1, arg2 = arg
	y = 99
	print y
	print "First argument is %s and second is %s" % (arg1, arg2)
	print x

print "End function 1"

def second_function(arg1, arg2):
	print "First argument is %s and second is %s" % (arg1, arg2)

def third_function(arg1):
	print "%s !" % arg1

first_function("hi", "hello")
# print y
second_function("hittt", "hellooooooo")
third_function("Hello")
