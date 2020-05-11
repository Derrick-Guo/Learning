# Tip: A string can be permuted to form a palindrome if and only if 
# the number of chars whose occurence is odd is at most 1.
import collections

def can_form_palindrome(s):
	res=collections.Counter(s)
	counter=0
	for num in res.values():
		if num%2!=0:
			counter+=1
	if counter>1:
		return False
	return True
# Optimized version:
def can_form_palindrome(s):
	return sum(v%2 for v in collections.Counter(s).values())<=1
# Time complexity: O(n). Space complexity: O(c), which c is the number of distinct chars appearing in the string.

# Test
s='hellooehi'
print(can_form_palindrome(s))



