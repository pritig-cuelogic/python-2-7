def first_n(n):
	num = 0
	while(num < n):
		print "before yield"
		yield num
		print num , "after return"
		num += 1
		print "after yield"
		yield num
		print num , "after return"


g = first_n(12)
print g.next()
print "next call"
print g.next()
print g.next()
