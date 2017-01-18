stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print stuff['height']

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['OR'] = 'yyyyy'
print '_' * 10
print "OR state has %r city" % cities['OR']

print '_' * 10
print "Michigan has: ", cities[states['California']]

print '_' * 10
for abbrev,city in cities.items():
	print "%s has the city %s" % (abbrev, city)

list_ex = [2, 5, 8]
print list_ex[1]
list_ex[2] = 8
print "%r" % list_ex
print type(states)
print type(list_ex)
