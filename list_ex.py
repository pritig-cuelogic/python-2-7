a = [1, 2, 3, 4, 9, 11]
b = [5, 6]

print a + b
print a * 3

print a[1:4]
print a[1:-2]

x = range(12)
print x
print x[1:11:2]
print x[::-1]
print 4 in x

print zip(["neetu", 1, [1,2]], [[4,5], "riya", 67, 8, 9])

for key, val in zip(["neetu", 1, [1,2]], [[4,5], "riya", 67, 8, 9]):
	print key, val

print sum(a)

a = [2, 10, 4, 3, 7]
a.sort()
print a

b = [4, 3, 5, 9, 2]
print sorted(b)
print b

print [x+y for x,y in zip([2, 3, 5, 88], [6, 8, 90])]
print [x+y for x in [4,5,6] for y in [1, 2, 3] if (x+y) < 7 and (x+y) != 6]
print map(lambda x: x*2, [2,3,5])
print filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
double = lambda x: x*2
print double(11)
