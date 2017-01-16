print  "Enter ur choice 1 or 2?"

choice = raw_input(">")

if choice == 1:
	print  "What do you do?"
	print "1: Take the cake."
	print "2. Scream at the bear"
	bear = raw_input("?? ")
	if bear == 1:
		print "The bear eats your face off"
	elif bear == 2:
		print "The bear eats your legs off."
	else:
		print "You enter wrong choce."
elif choice == 2:
	print "You stare into the endless"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	instint = raw_input("> ")
	if instint ==2 or instint == 1:
		print "Your body survives powered by a mind of jello"
	elif instint == 3:
		print "entered 3"
	else:
		print "The insanity rots your eyes into a pool of muck"
else:
	print "You stumble around and fall on a knife and die"
