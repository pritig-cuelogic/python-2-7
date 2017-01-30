def flatten_dict(a,obj=None, result=None):
	if result is None:
		result = {}
	for key, val in a.iteritems():
		if isinstance(val, dict):
			flatten_dict(val, key, result)
		else:
			if obj is not None:
				temp_var = obj+"."+key
				result[temp_var] = val
			else:
				result[key] = val
			
	return result
    
print "%r" % flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
