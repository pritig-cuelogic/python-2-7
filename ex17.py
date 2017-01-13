from sys import argv
from os.path import exists

script, file1, file2, file3 = argv
print "Copying file from %s to %s" % (file1, file2)
fileObj = open(file1)
fileData = fileObj.read()
print "%s file data %d bytes long" % (file1, len(fileData))
print "file2 exist? %r" % exists(file2)
fileObj1 = open(file2, 'w')
fileObj1.write(fileData)
fileObj1.close()
fileObj.close()

fileObj2 = open(file2)
print fileObj2.read()
fileObj2.close()

print "%s file exist %r" % (file3, exists(file3))
fileObj3 = open(file3, 'w')
print "%s file exist %r" % (file3, exists(file3))
fileObj3.write("Hello")
fileObj3.close()
