i = 0
num = []

while i < 6:
	print "At the top i is %d" % i
	num.append(i)
	i += 1
	print "Numbers now: " , num
	print "At the bottom i is %d" % i

print "The numbers: "
for numbers in num:
	print numbers

print num.count(4)
num.reverse()
print num
print num.index(3)
num.extend([11, 9, 88, 8])
print num
num.extend("priti")
print num
num.reverse()
print num
num.insert(1, 100)
print num
