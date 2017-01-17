ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

new_list =  ten_things.split(" ")
new_list.append(4)
print new_list
new_list.append([44, 78, "knee"])
print new_list

for item in new_list:
	print "%r" % item

list1 = [3, 4, 5]
print list1.extend([11, 33])
print list1
list1.insert(3, "position")
print list1
list1.remove(11)
print list1.pop(1)
print new_list.index([44, 78, "knee"])

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

for i in matrix:
	print "matrix element: %r" % i
