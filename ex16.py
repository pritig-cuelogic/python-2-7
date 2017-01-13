from sys import argv

script, fileName = argv

print "Reading %s File" % fileName
fileObj = open(fileName, 'w+')

print "truncate file..."
fileObj.truncate()

line1 = raw_input("enter line1 to input> ")
fileObj.write(line1)
fileObj.write("\n")
line2 = raw_input("enter line2 to input> ")
fileObj.write(line2)
fileObj.write("\n")
line3 = raw_input("enter line3 to input> ")
fileObj.write(line3)
fileObj.write("\n")
fileObj.close()

print fileName
fileObj1 = open(fileName, 'r')
print fileObj1.read()
fileObj1.close()
