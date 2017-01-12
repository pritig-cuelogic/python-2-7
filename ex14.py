import sys

script, user_name = sys.argv
prompt = '?'
print "Hi %s, I'm the %s script." % (user_name, script)
print "Do you like me %s?" % user_name
like = raw_input(prompt)
print "Where do you live %s?" % user_name
stay = raw_input(prompt)
print "What kind of computer do you have?"
comp = raw_input(prompt)
print "%s lives in %s, like me %s and have %s computer" % (
	  user_name, stay, like, comp)
print """
      Alright, so you said %r about liking me.
      You live in %r.  Not sure where that is.
      And you have a %r computer.  Nice.
      """ % (like, stay, comp)
