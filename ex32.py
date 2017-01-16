counts = [1, 2, 3]
fruits = ["apple", "mango", "papaya", "orange"]
change = [1, "night", 78, "umbrella"]
i = 0;

for number in counts:
	print "This is count %d" % number

print "Below is my fruit list \n"
for fruit in fruits:
	i += 1
	print "%d: %s \n" % (i, fruit)

for changes in change:
	print "i got %r" % changes

list_element = []
for num in range(1, 7):
	print "Adding %d to the list." % num
	list_element.append(num)

for i in list_element:
	print "List element %d" % i
