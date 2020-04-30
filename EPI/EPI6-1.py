# Tips:
# To convert an integer x to a character, use 'chr(ord('0')+x)'
# To convert a character x to an integer, use 'string.digits.index(x)'
def int_to_string(x):
	res=[]
	is_negative=False
	if x<0:
		x, is_negative= -x, True
	while x:
		res.append(chr(ord('0')+x%10))
		x//=10
	return ('-' if is_negative else '')+''.join(reversed(res))

################################################################
import functools,string
def string_to_int(s):
	return functools.reduce(
		lambda partial_sum,c: partial_sum*10+string.digits.index(c),
		s[s[0]=='-':],0) * (-1 if s[0]=='-' else 1)


print(int_to_string(-324))
print(string_to_int('-324'))
