from sys import argv

script, file_name = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_one_line(c_line, f):
	print c_line, f.readline()

fileObj = open(file_name)
print "print whole file"
print_all(fileObj)

print "take file pointer at top of file"
rewind(fileObj)

print "print line no with every line"
current_line = 1
print_one_line(current_line, fileObj)
current_line += 1
print_one_line(current_line, fileObj)
current_line += 1
print_one_line(current_line, fileObj)