formatter = "%r %r %r %s"
print formatter % (1, 2, 3, 4)
print formatter % (
	'This.',
	'That',
	12,
	"\tneha")
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (True, False, False, True)
print 5,
print 6,
print 9
