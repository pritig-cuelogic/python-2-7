from sys import argv

script, first, second, third = argv
s = raw_input("who r u? ")
print "The script is called:", script
print "Your first variable is: %s, %s" % (first, s)
print "Your second variable is:", second
print int(s) * 3
print s * 3
