print "Let's practice everything."
print "this \n is right thing \\n with u ",
print "\t and \\t using escape sequence"

x = """
this is use of tripple
     codes and 
we will see result 
"""

print x

def test_function():
	x = 2
	y = 3
	z = 4
	return x,y,z

val1, val2, val3 = test_function()

print "we have value1 = %d \n value2 = %d \n value3 = %d" % (
    test_function()
	)
