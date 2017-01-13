from sys import argv

scriptName, fileName = argv
print "%s script is exicuting" % scriptName
fileObj = open(fileName)
print "this file content is printing %s" % fileName
print fileObj.read()

otherFileName = raw_input("Give another file name")
print "Other file u input is %s" % otherFileName
fileObj1 = open(otherFileName)
print "this is %s file content" % otherFileName
print fileObj1.read()
