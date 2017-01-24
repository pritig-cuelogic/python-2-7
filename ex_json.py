def json_encode(data):
	if isinstance(data,bool):
		if data:
			return "true"
		else:
			return "false"
	elif isinstance(data,(int,float)):
		return str(data)
	elif isinstance(data,str):
		return '"'+ escape_string(data) + '"'
	elif isinstance(data,list):
		return "[" + ", ".join(json_encode(d) for d in data) + "]"
	else:
		raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
	s = s.replace('"', '\\"')
	s = s.replace("\t", "\\t")
	s = s.replace("\n", "\\n")
	return s

print "%r" % json_encode({
    "name": "Advanced Python Training",
    "date": "October 13 2012",
    "completed": False
}
)
