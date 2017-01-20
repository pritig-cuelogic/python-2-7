class Node:
	def __init__(self,val):
		self.l_child = None
		self.r_child = None
		self.data = val

def insert(root,node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.l_child is None:
				root.l_child = node
			else:
				insert(root.l_child,node)
		else:
			if root.r_child is None:
				root.r_child = node
			else:
				insert(root.r_child,node)


file_obj = open('result.txt','r+')
i = 0
for numbers in file_obj.readlines():
	if i == 0:
		r = Node(numbers)
	else:
		insert(r,Node(numbers))
	i += 1
file_obj.close()
