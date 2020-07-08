def swap_case(s):
	#here, I used 'List Comprehemsion'
	s = [char.lower() if char.isupper() else char.upper() for ch in s]
	return ''.join(s)