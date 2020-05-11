import collections
def is_letter_constructible_from_magazine(letter,magazine):
	letter_counter=collections.Counter(letter)
	for c in magazine:
		if c in letter_counter:
			letter_counter[c]-=1
			if letter_counter[c]==0:
				del letter_counter[c]
	if letter_counter:
		return False
	return True
# Time complexity: O(m+n),which m and n are the number of chars in the letter and magazine, respectively.
# Space complexity: O(l), where l is the number of distinct chars appearing in the letter.

# Pythonic solution:
def is_letter_constructible_from_magazine(letter,magazine):
	return (not collections.Counter(letter)-collections.Counter(magazine))

# Test
letter='hello'
magazine='hella'
print(is_letter_constructible_from_magazine(letter,magazine))